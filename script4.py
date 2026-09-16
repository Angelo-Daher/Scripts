import requests
import gzip
from io import BytesIO
import os

urls = [
    'https://ps.calameoassets.com/260915140317-828f9e6dde81ca5a197ffd930c7b508f/p1.svgz?_token_=exp=1789612539~acl=%2F260915140317-828f9e6dde81ca5a197ffd930c7b508f%2F%2A~hmac=90c0c3402d738e8a95f9bdb15483e3645815121b190c2c39c98c85024f4d11b2',
    'https://ps.calameoassets.com/260915140317-828f9e6dde81ca5a197ffd930c7b508f/p2.svgz?_token_=exp=1789612539~acl=%2F260915140317-828f9e6dde81ca5a197ffd930c7b508f%2F%2A~hmac=90c0c3402d738e8a95f9bdb15483e3645815121b190c2c39c98c85024f4d11b2',
    'https://ps.calameoassets.com/260915140317-828f9e6dde81ca5a197ffd930c7b508f/p3.svgz?_token_=exp=1789612539~acl=%2F260915140317-828f9e6dde81ca5a197ffd930c7b508f%2F%2A~hmac=90c0c3402d738e8a95f9bdb15483e3645815121b190c2c39c98c85024f4d11b2'
]

for i, url in enumerate(urls, start=1):
    response = requests.get(url)

    with open(f"pagina_{i}.svgz", "wb") as arquivo:
        arquivo.write(response.content)

    print(f"Página {i}")

""" Script para facilitar o download das versões svgz dos Flips """
