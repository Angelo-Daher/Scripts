import requests               # Ferramenta que Conversa com a internet através de requisições HTTP
from PIL import Image         # Biblioteca para manipulação de imagens
from io import BytesIO        # Módulo do Python para trabalhar com entrada e saída de dados.
import os                     # Ajuda o Python a trabalhar com arquivos, pastas e caminhos do sistema.

for i in range(1, 24):
    url = f"https://tribunadonorte.com/digital/app/editions/flip/2026-09-24-Tribuna-do-Norte-24092026-QUINTA-CDA-1/Pages/page_CDA_{i}.jpg"
    response = requests.get(url)

    imagem = BytesIO(response.content) #Coloca na variavel imagem o conteudo da resposta, que é a imagem em bytes.
    image = Image.open(imagem) #abre a imagem usando a biblioteca PIL

    #image.save(f"00{i}.png")

    aux = str(i) #funçao para transformar o numero em string, para que seja possivel usar a funçao rjust, que adiciona zeros a esquerda.
    image.save(f"{aux.rjust(3, '0')}.png") #funçao para ordenaçao de pag com zeros a esquerda, para que o sistema leia na ordem correta. Ex: 001, 002, 003...