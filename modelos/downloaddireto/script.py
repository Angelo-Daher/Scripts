import requests               # Ferramenta que Conversa com a internet através de requisições HTTP
from PIL import Image         # Biblioteca para manipulação de imagens
from io import BytesIO        # Módulo do Python para trabalhar com entrada e saída de dados.
import os                     # Ajuda o Python a trabalhar com arquivos, pastas e caminhos do sistema.

urls_graph1024 =[

    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=SWdGTlZSUFBlc3dIc0U5R1IzRm5pZz09&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=bldVN2ZIeE9GVkNBYlpkNklmTmRoNGRrWTB2YnZtZFJhT2xGdWZhdzZGbz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=b3R6T29DY3RwMXdqYVFQcXpaUFZTRzNDQTJ1K01wODIrSEF3NzgwdEIydz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=NEVGcnZoOWN2ZmRwMHJrVGo4U2hXbEpVWERZSHY2UkU4aFJjWGowWEpiUT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=ekl4RkFmOWo2UENSTGxSL3BFTnhSN1JWYWFqOXV1WWVOZ0Fra3I4MnhyMD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=M0dlMGpVTVRMUmxUZ1dGVXdXaDBYbE1xUTlkaVVLM3BteWpMOFhoSkFCMD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=OTBxUk1BNmV4RWFEdDl3dzdDUFM0dGpwWnRzOEMzU28rS0hxeUs4eXJiYz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=b044YXNjQ3gyNVVxR25KNDlURmQ3NDdBYXZVbFk4VmU5T0ZmYlBXU0w5RT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=bENycnRsZ0hDZndSaGdlMmdBcmppczgxSVNTVkxDQ0pGeWl6Q1hSeFdsQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=b1RTU2tmcTByNFJCWVJUT0UyT2NEZkVOTnk1L2xqMDl4aGFtbWI3bFVlYz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=WVBsT0RtNTFHOVBQRFpQZWNZZFY4YTYwMm9nR2wrV2hvR0tSb2o0a3QvTT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=VW93bTZjVFltQVJ6Z1JmdWpNeHNVU1V4VFBpcGxWQ3BDaHAvQ2k2bnZQdz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=UjZQbjMyRnJGc055V0ZpRFdXdFhXMUVlV0p3U1RzUDQvM2VOSlRyK0p5az0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=TXpwSFgraEhCQ2F4MCtacEIzMVkvUFo0Sm5oc2VNZkEwbEhycE1nWmtTbz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=MndQYzAyREtaekVzQ3pFdk5RMGYrNnBwMmhqTFY5UGEvMUpSelRqU3pkMD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=TjdSTlVtaExnVjQrdWU2WXdkcU9PSG16dUlOTEozZFNkS0YxRWI0emFpWT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=anc1MENxMk1Ob2I2YXZqdzBCMERtUzRIVXc1U3BUZWQ5dU9kUGpNVFBqYz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=dHAvanh6ejhzRkdkYXVrRTliWGJpU1BPdHNPVnhJeEgzUGJveWtuTStZQT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=OHIyR01wL1Q3SWJMTUppUmhZNS9PejAxRWQrUWR6anpxZDgyYjVsb0ozcz0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=YmpXUjFPM0hDM1hTT0NSNmh0RXozZCswdlZLU3o3SEJyU1lMeDVrU0VxND0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=Y0drWDc3bnBQVnpSZ1lnQzVnQ2ZHMzB1UFdKUTFIS3plTitpVFNrSjVxMD0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=cHNLVW9EVlpMcnBOckVZV2RQWFBjRGZJVjUvUm9CM2w5TkJkUFpDWHMvTT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=NDRvT2NYZFZnNnJLWnlYNW1IdGdCZUxoM29wRldmQkxiK0h4cXBZS096UT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=NEN6NUE1a2lNemxpZzh5d3hZSVlRMGpmdjNOVlpHWi9Ba1hJaHBhdWU3WT0=&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=low&pSetup=novojornal&issue=20260925&crc=b29qK1JJZGRUMXc5UHJGUlFBbTkvQT09&edition=Novo%20Jornal&verCdn=0&mtime=5D389336"
]

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

download_images(urls_graph1024, "imagens_graph1024")