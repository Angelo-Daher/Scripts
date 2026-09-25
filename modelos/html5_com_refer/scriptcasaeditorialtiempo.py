import requests
from PIL import Image
from io import BytesIO

urls = [
    #Mudar escala da imagem para melhor resolução.
    "https://online.fliphtml5.com/ndhqc/3264/files/large/1b4b806e1257a2262a5ae25b10173def.webp?1790227183",
]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:155.0) Gecko/20100101 Firefox/155.0",
    "Referer": "https://casaeditorialeltiempo.pressreader.com/"
}

for i, url in enumerate(urls, start=1):

    response = requests.get(url, headers=headers)

    print(f"\nPágina: {i}")
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Tamanho:", len(response.content))

    if response.ok:
        imagem = BytesIO(response.content)
        image = Image.open(imagem)

        print("Dimensões:", image.size)

        image.save(f"{i:03}.png")