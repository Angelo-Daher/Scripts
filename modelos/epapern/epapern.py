import requests
from PIL import Image
from io import BytesIO
import os

# Prefixo para as URLs (deve ser preenchido ou removido)
base_url = "https://epapern.novavaga.co.ao/"  # Se não for necessário, pode remover esta variável


# Lista de URLs
urls_graph1024 = [
    "https://eu1-bcdn.newsmemory.com/eebrowser/ipad/html5.check.23120413/ajax-request.php?action=loadImage&type=graph1024&pSetup=novojornal&issue=20260925&crc=SWdGTlZSUFBlc3dIc0U5R1IzRm5pZz09&edition=Novo%20Jornal&verCdn=0&mtime=5D389336",
]
# Geração das URLs de texto (substitui "graph1024" por "text1024")
urls_text = [url.replace("type=graph1024", "type=text1024") for url in urls_graph1024]

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta exceção em caso de erro
    return Image.open(BytesIO(response.content))

output_folder = "imagens"
os.makedirs(output_folder, exist_ok=True)

combined_counter = 1

for i in range(len(urls_graph1024)):
    try:
        graph1024_url = urls_graph1024[i]
        graph1024_image = download_image(graph1024_url)
        graph1024_image.save(os.path.join(output_folder, f"graph1024_{i}.png"))  # Salvar a imagem do gráfico

        # Baixar a imagem do texto
        text_url = urls_text[i]
        text_image = download_image(text_url)
        text_image.save(os.path.join(output_folder, f"text_{i}.png"))  # Salvar a imagem do texto

        if text_image.mode != 'RGBA':
            text_image = text_image.convert('RGBA')

        # Combinar as imagens (sobrepor o texto sobre o gráfico)
        combined_image = Image.new("RGBA", graph1024_image.size)
        combined_image.paste(graph1024_image.convert('RGBA'), (0, 0))
        combined_image.paste(text_image, (0, 0), text_image)

        combined_path = os.path.join(output_folder, f"{combined_counter}.png")
        combined_image.save(combined_path)
        print(f"Imagem combinada {combined_counter} salva em {combined_path}")

        if i > 0 and i < len(urls_graph1024) - 1:
            width, height = combined_image.size
            half_width = width // 2

            left_half = combined_image.crop((0, 0, half_width, height))
            right_half = combined_image.crop((half_width, 0, width, height))

            left_half_path = os.path.join(output_folder, f"{combined_counter}_left.png")
            right_half_path = os.path.join(output_folder, f"{combined_counter}_right.png")
            left_half.save(left_half_path)
            right_half.save(right_half_path)
            print(f"Imagem cortada salva como {left_half_path} e {right_half_path}")

            combined_counter += 1  # Incrementa o contador para a próxima imagem

        combined_counter += 1  # Incrementa o contador para a próxima combinação

    except Exception as e:
        print(f"Erro ao baixar ou combinar as imagens para o índice {i}: {e}")
