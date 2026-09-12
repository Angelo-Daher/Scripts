import requests               # Ferramenta que Conversa com a internet através de requisições HTTP
from PIL import Image         # Biblioteca para manipulação de imagens
from io import BytesIO        # Módulo do Python para trabalhar com entrada e saída de dados.
import os                     # Ajuda o Python a trabalhar com arquivos, pastas e caminhos do sistema.

urls_graph1024 =[
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260911&crc=QU5iT0dIUHdURWowTEpJTHdCOHprZz09&edition=Novo%20Jornal&verCdn=0&mtime=5D2A9171",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260911&crc=MUNKK1I0MUZnNVBPcU03cWRUV1d6ZzR4OUVUUHArZ2NJRExpalQydzNpQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D2A9171",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260911&crc=QU40bUkzbXE0U2wydUZTVWJBdUhHMlQwbnZLeWhVQ2p5RjlWdWJLV1dxaz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D2A9171"
]
response = requests.get(urls_graph1024[0:3]) # Faz uma requisição HTTP GET para a URL especificada e armazena a resposta na variável 'response'
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida (código 200)

imagem = BytesIO(response.content)  # Cria um objeto BytesIO a partir do conteúdo da resposta
imagem = Image.open(imagem)  # Abre a imagem usando a biblioteca PIL
imagem.save("imagem_baixada.png")  # Salva a imagem em um arquivo chamado "imagem_baixada.png"

def download_images(urls, folder):
    """
    Função para baixar imagens de uma lista de URLs e salvá-las em uma pasta especificada.
    
    Parâmetros:
    urls (list): Lista de URLs das imagens a serem baixadas.
    folder (str): Caminho da pasta onde as imagens serão salvas.
    """
    if not os.path.exists(folder):  # Verifica se a pasta existe
        os.makedirs(folder)  # Cria a pasta se não existir

    for i, url in enumerate(urls):  # Itera sobre a lista de URLs
        try:
            response = requests.get(url)  # Faz uma requisição HTTP GET para a URL
            response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
            imagem = BytesIO(response.content)  # Cria um objeto BytesIO a partir do conteúdo da resposta
            imagem = Image.open(imagem)  # Abre a imagem usando a biblioteca PIL
            image_path = os.path.join(folder, f"imagem_{i + 1}.png")  # Define o caminho do arquivo de imagem
            imagem.save(image_path)  # Salva a imagem no caminho especificado
            print(f"Imagem {i + 1} salva em: {image_path}")  # Imprime mensagem de sucesso
        except Exception as e:  # Captura qualquer exceção que ocorra durante o download ou salvamento da imagem
            print(f"Erro ao baixar a imagem {i + 1}: {e}")  # Imprime mensagem de erro