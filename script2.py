import requests               # Ferramenta que Conversa com a internet através de requisições HTTP
from PIL import Image         # Biblioteca para manipulação de imagens
from io import BytesIO        # Módulo do Python para trabalhar com entrada e saída de dados.
import os                     # Ajuda o Python a trabalhar com arquivos, pastas e caminhos do sistema.

for i in range(1, 85):
    url = f"https://cdn-assets.ziniopro.com/var/issues/722967/a1156d1d5ec1f6569ed4f0dae32b350b/preview_image/page-{i:05d}.jpg"
    response = requests.get(url)

    imagem = BytesIO(response.content) #Coloca na variavel imagem o conteudo da resposta, que é a imagem em bytes.
    image = Image.open(imagem) #abre a imagem usando a biblioteca PIL

    #image.save(f"00{i}.png")

    aux = str(i) #funçao para transformar o numero em string, para que seja possivel usar a funçao rjust, que adiciona zeros a esquerda.
    image.save(f"{aux.rjust(3, '0')}.png") #funçao para ordenaçao de pag com zeros a esquerda, para que o sistema leia na ordem correta. Ex: 001, 002, 003...