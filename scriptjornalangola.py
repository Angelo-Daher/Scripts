import requests
from PIL import Image
from io import BytesIO
import os

# Prefixo para as URLs (deve ser preenchido ou removido)
base_url = "https://epapern.novavaga.co.ao/"  # Se não for necessário, pode remover esta variável


# Lista de URLs
urls_graph1024 = [
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=NXV2RHRjczNXTFhGS09GREtMUEtaUT09&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=dVRleVBKUFFxclRnbE5xMGZqRkwwK1g4bkUyNmdVcUtDbGswMGJ0aXV5MD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=emhiVDNvbkxyb1BKQ1krbWIvSFJvajdiMExKVndyMTJkM0NkRCtGMTh2MD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=V253SWxCVXE1QkxVUi95OElteWNxU2ErUnorODFySEt4aUVlYzFzV2JNVT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=cnFoK0RzSlZhN0NJTE94Q2w2cDVDN0hqS0lvUGpOd3lBMytsRFptMS9qWT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=UGpZVHB2UlhqaFYvbjc2cmZLUVpYMVFNWjJrM01NNlB5UDZsaGFQRG9zVT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=cElVMmI5ajV2Z1c0aW9WdS9nYkZhRUVkQmQxSzBDYlZYWnNsUkNRT2wyQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=bENTclNRQ0tYMDY3UlJQYjYvclg5Smg1SzNQZ2FGejdrMUpzSWtKV3ZsVT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=R09HTGdycm1xaHowZkJjQW5TSHp1cXNYemlkcys4VlBaZUUxU09SYnRQUT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=L0tvK3hmVzJyekRxbysxRmFsMFRwZzdFVm4rNU55L3FweGpVaURmd0Q3Zz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=WmdNeDBLUFVNZVNtK2ZvYVo5Qm9Nc085WmFFYURmdmUxTUY5RitXczNHbz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=Rkd6QzUwSzhMUHZYck5TalIxNzRQY2Q2RlVvNHdWdGIwVnN4aUkzYVVJdz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=dWVPZ2o5dE1uZ2tZaHBpcllOWndHaEsxaWV2ZHlxV0Ixb0Q3TndOcnRaQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=c0piV2c2NjhkaVBUc1FqcmxYK0tkMEowb3hFdzIwbVZZNitvOGJZdXU1az0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=R2NJaU1sYWRRalRTek5mVXFIVmlVYytzY2sxcjQ3Ykc5ZFZZdnBWaldWST0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=eEEzblFLK2RrZGlHSzN5ZG1wNmgwRVNGcUZSZlFENUVFMUVEOGR3SG5aWT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=RERzdSt5MXlSa3BieHFkWE41UGFuZWlmRktyR1kxMjhQdTFUY2U1Z0FFQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=T0Ntd0JIQjBOSjNqdXc2bnhKVWEyS3FkZDhNSkUrYmRZbnp0UDMvSnFJOD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=Q3NXd1FNVXN2NVF1T2hjZFd2cjB3a2N4NVQybCtTcG9ZbU12VWpoSEF4MD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=TVNQaEJFWDRWc2NjRitiZjBwNHA2TGtjNnc4emt0UmVHcUhkMzNGNUE1cz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=UUIvc25COWtMcngvb290bXdFTThIaHVQZHRQYWxzMUhmc1B4ZmJPRis4MD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=Z1A1aVZmbmJSVG9PNWc5ZVZpb051NUhDVngvdUNacVVQWFJBeHdmRkx6VT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=c3N6YjVjdDJEY3FqWmhpeUgyb0Z2Wm95a1V3Y2NCVUx5NG43RGgzeTcvVT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=Tm5VMjF0SUMxMEVVU3EvYUxheEovdmkyWFU5RFhZVHh6TEpVeFVnUlpEUT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260918&crc=dUdLcGY3UkFQOGRLcmNpdWowWlVBZz09&edition=Novo%20Jornal&verCdn=0&mtime=5D319835",
]
# Geração das URLs de texto
urls_text = [
    url.replace("type=graph1024", "type=text1024")
    for url in urls_graph1024
]


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))


output_folder = "imagens"
os.makedirs(output_folder, exist_ok=True)

contador = 1


for i in range(len(urls_graph1024)):
    try:
        # Baixar gráfico
        graph1024_image = download_image(urls_graph1024[i])

        # Baixar texto
        text_image = download_image(urls_text[i])

        if text_image.mode != "RGBA":
            text_image = text_image.convert("RGBA")

        # Combinar gráfico + texto
        combined_image = Image.new(
            "RGBA",
            graph1024_image.size
        )

        combined_image.paste(
            graph1024_image.convert("RGBA"),
            (0, 0)
        )

        combined_image.paste(
            text_image,
            (0, 0),
            text_image
        )

        # Primeira imagem = capa
        if i == 0:
            caminho = os.path.join(
                output_folder,
                f"{contador}.png"
            )

            combined_image.save(caminho)

            print(f"Capa salva: {contador}.png")

            contador += 1

        # Demais páginas = esquerda + direita
        else:
            width, height = combined_image.size
            metade = width // 2

            esquerda = combined_image.crop(
                (0, 0, metade, height)
            )

            direita = combined_image.crop(
                (metade, 0, width, height)
            )

            # Salvar lado esquerdo
            esquerda.save(
                os.path.join(
                    output_folder,
                    f"{contador}.png"
                )
            )

            print(f"Página salva: {contador}.png")
            contador += 1

            # Salvar lado direito
            direita.save(
                os.path.join(
                    output_folder,
                    f"{contador}.png"
                )
            )

            print(f"Página salva: {contador}.png")
            contador += 1

    except Exception as e:
        print(
            f"Erro na página {i + 1}: {e}"
        )
