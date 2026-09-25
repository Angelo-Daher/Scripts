import os
import requests
from PIL import Image
from loguru import logger

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ==============================================================================
# CONFIGURAÇÃO DA REVISTA
# ==============================================================================
URL_REVISTA = "https://online.fliphtml5.com/nfbp/jornal-1181-oeste_site/"
NOME_PDF_FINAL = "jorbairro.pdf"
PASTA_TEMPORARIA = "bairro_html5_"
# ==============================================================================

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": URL_REVISTA
}

def extrair_lista_paginas_com_selenium(url_base):
    logger.info("Iniciando navegador em segundo plano (Selenium)...")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={HEADERS['User-Agent']}")

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)

    paginas = None
    try:
        driver.get(url_base)
        driver.implicitly_wait(5)
        
        logger.info("Extraindo array de páginas da memória JavaScript...")
        # Adicionado htmlConfig para cobrir mais versões do FlipHTML5
        paginas = driver.execute_script(
            "return (window.fliphtml5_pages || "
            "        (window.bookConfig ? window.bookConfig.fliphtml5_pages : null) || "
            "        (window.htmlConfig ? window.htmlConfig.fliphtml5_pages : null) || "
            "        (window.config ? window.config.fliphtml5_pages : null));"
        )
    except Exception as e:
        logger.error(f"Erro ao interagir com o navegador: {e}")
    finally:
        driver.quit()
        
    return paginas

def baixar_paginas(paginas_config, url_base):
    if not os.path.exists(PASTA_TEMPORARIA):
        os.makedirs(PASTA_TEMPORARIA)
        
    if not url_base.endswith('/'):
        url_base += '/'

    imagens_salvas = []
    total = len(paginas_config)
    logger.success(f"Configuração resolvida! Total de páginas detectadas: {total}")

    for i, pag in enumerate(paginas_config):
        num_pagina = i + 1
        
        # Busca inteligente: tenta as chaves 'n' (normal), 'l' (large) ou 't' (thumb)
        hash_imagem = pag.get("n") or pag.get("l") or pag.get("t")
        
        if isinstance(hash_imagem, list):
            hash_imagem = hash_imagem[0] if hash_imagem else None
            
        if not hash_imagem:
            logger.error(f"Caminho não localizado para a página {num_pagina}. Dump JS: {pag}")
            continue

        caminho_relativo = str(hash_imagem).strip().lstrip("/")
        
        # Se o site só entregou o thumb, forçamos o download da imagem grande
        if "thumb" in caminho_relativo:
            caminho_relativo = caminho_relativo.replace("thumb", "large")

        url_imagem = f"{url_base}{caminho_relativo}"
        
        caminho_arquivo = os.path.join(PASTA_TEMPORARIA, f"pagina_{str(num_pagina).zfill(3)}.webp")
        
        if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 5000:
            logger.info(f"Página {num_pagina} já existe localmente. Pulando...")
            imagens_salvas.append(caminho_arquivo)
            continue

        try:
            logger.debug(f"[{num_pagina}/{total}] Baixando: {url_imagem}")
            r = requests.get(url_imagem, headers=HEADERS, timeout=20)
            
            if r.status_code == 200:
                with open(caminho_arquivo, "wb") as f:
                    f.write(r.content)
                imagens_salvas.append(caminho_arquivo)
            else:
                logger.error(f"Falha na pág {num_pagina} | Status HTTP: {r.status_code} | URL: {url_imagem}")
        except Exception as e:
            logger.error(f"Erro na conexão da página {num_pagina}: {e}")
            
    return sorted(imagens_salvas), total

def converter_para_pdf(lista_imagens, total_esperado):
    if not lista_imagens:
        logger.critical("Nenhuma imagem foi baixada. PDF cancelado.")
        return

    if len(lista_imagens) < total_esperado:
        logger.warning(
            f"Atenção: A captura terminou com {len(lista_imagens)} imagens, mas o esperado eram {total_esperado}."
        )

    logger.info(f"Compilando as {len(lista_imagens)} páginas no PDF final...")
    try:
        primeira_img = Image.open(lista_imagens[0]).convert('RGB')
        restante_imagens = [Image.open(img).convert('RGB') for img in lista_imagens[1:]]
        
        primeira_img.save(NOME_PDF_FINAL, save_all=True, append_images=restante_imagens)
        logger.success(f"PDF final gerado com sucesso: {NOME_PDF_FINAL}")
        
        for img in lista_imagens:
            os.remove(img)
        os.rmdir(PASTA_TEMPORARIA)
        logger.info("Pasta temporária limpa com sucesso.")
    except Exception as e:
        logger.critical(f"Erro na conversão para PDF: {e}")

if __name__ == "__main__":
    paginas_config = extrair_lista_paginas_com_selenium(URL_REVISTA)
    if paginas_config:
        imagens, total_paginas = baixar_paginas(paginas_config, URL_REVISTA)
        converter_para_pdf(imagens, total_paginas)
    else:
        logger.critical("Não foi possível capturar a estrutura de páginas via Selenium.")