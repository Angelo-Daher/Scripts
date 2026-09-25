import requests
from PIL import Image
from io import BytesIO
import os


url = [
    "https://online.fliphtml5.com/qiuuf/4947/files/large/c4a43ea470cb9272c02da9c5df240345.webp?1790317922",
]


for i in range(len(url)):
    response = requests.get(url[i])
    imagem = BytesIO(response.content)
    image = Image.open(imagem)
    image.save(f"{i+1}.webp")