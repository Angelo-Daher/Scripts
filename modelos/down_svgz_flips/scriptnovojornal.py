import requests
import gzip
import cairosvg
from PIL import Image
from io import BytesIO

urls = [
    "https://ps.calameoassets.com/260921232441-ba99575b84a4f4c14d9359fd188ebbe2/p1.svgz?_token_=exp=1790129136~acl=%2F260921232441-ba99575b84a4f4c14d9359fd188ebbe2%2F%2A~hmac=902c3c62553fe8adc8ec9500e0496d8a2a947c80611adb0cec47caf6236dc76a",
]

for i, url in enumerate(urls, start=1):

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro na página {i}: HTTP {response.status_code}")
        continue

    conteudo = response.content

    # Verifica se o arquivo está realmente gzipado
    if conteudo[:2] == b"\x1f\x8b":
        conteudo = gzip.decompress(conteudo)

    try:
        # SVG -> PNG
        png = cairosvg.svg2png(
            bytestring=conteudo
        )

        # PNG -> JPG
        imagem = Image.open(BytesIO(png))
        imagem = imagem.convert("RGB")

        imagem.save(
            f"pagina_{i}.jpg",
            "JPEG",
            quality=95
        )

        print(f"Página {i} convertida!")

    except Exception as erro:
        print(f"Erro na página {i}: {erro}")