import requests
import gzip
from io import BytesIO
import os

urls = [
    "https://ps.calameoassets.com/260921232441-ba99575b84a4f4c14d9359fd188ebbe2/p1.svgz?_token_=exp=1790129136~acl=%2F260921232441-ba99575b84a4f4c14d9359fd188ebbe2%2F%2A~hmac=902c3c62553fe8adc8ec9500e0496d8a2a947c80611adb0cec47caf6236dc76a",
]

for i, url in enumerate(urls, start=1):
    response = requests.get(url)

    with open(f"pagina_{i}.svgz", "wb") as arquivo:
        arquivo.write(response.content)

    print(f"Página {i}")






""" Script para facilitar o download das versões svgz dos Flips """