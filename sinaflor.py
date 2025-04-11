import pyautogui
import pytesseract
from PIL import Image
import time
import os
from tqdm import tqdm

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\alisson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Lista de códigos CAR
car_list = [
    "SP-3520707-E6349343AEBE494EBD7A3E687C7A3B14",
    "SP-3550308-A5AE102CF6464D6C8813681C5318DCD4",
    "SP-3531902-BB4D124D0CC54E8FA49F0ACE575A65A5",
    "SP-3554201-FA1D78F603EF46B5BF0A4A90EBFB5FE0",
]

# Caminho do arquivo de saída
caminho_txt = r"C:\Alisson_vs\resultado.txt"
linhas_txt = []

# Tempo de espera entre as ações
TEMPO_ESPERA = 0.6

# Coordenadas do campo onde o código CAR será inserido
COORDENADA_CAR = (549, 255)

# Coordenadas para crop da imagem (ajuste conforme necessário)
AREA_CROP = (65, 300, 165, 685)

# Barra de progresso
bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"

def melhorar_resolucao(imagem, fator=2):
    """Aumenta a resolução da imagem para melhorar OCR"""
    largura, altura = imagem.size
    nova_imagem = imagem.resize((largura * fator, altura * fator), Image.LANCZOS)
    return nova_imagem

try:
    time.sleep(1)  # Tempo para abrir a tela do navegador manualmente, se necessário

    with tqdm(total=len(car_list), desc="Consultando CARs", unit="CAR", dynamic_ncols=True, mininterval=0.1, bar_format=bar_format) as pbar:
        for codigo_car in car_list:
            pbar.set_description(f"Processando: {codigo_car[:15]}")

            # Clicar no campo de inserção
            pyautogui.click(*COORDENADA_CAR)
            time.sleep(TEMPO_ESPERA)

            # Selecionar e limpar qualquer texto anterior
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            time.sleep(0.5)

            # Digitar o código CAR
            pyautogui.write(codigo_car)
            pyautogui.press("enter")
            time.sleep(1.4)  # Tempo para carregar o resultado

            # Capturar a tela inteira
            screenshot = pyautogui.screenshot()

            # Recortar a área desejada
            cropped_image = screenshot.crop(AREA_CROP)

            # Melhorar resolução (dobrando o tamanho)
            imagem_melhorada = melhorar_resolucao(cropped_image, fator=2)

            # OCR com Tesseract
            texto_extraido = pytesseract.image_to_string(imagem_melhorada, config='--psm 6').strip()
            texto_formatado = texto_extraido.replace("\n", "$")

            # Formatar e salvar resultado
            linha_final = f"{codigo_car}${texto_formatado}"
            linhas_txt.append(linha_final)

            pbar.update(1)

except Exception as e:
    print(f"\n❌ Erro encontrado: {e}")
    print("⚠️ Interrompendo processamento e salvando dados parciais...")

finally:
    if linhas_txt:
        with open(caminho_txt, "w", encoding="utf-8") as f:
            for linha in linhas_txt:
                f.write(linha + "\n")
        print(f"\n💾 Dados salvos em '{caminho_txt}'.")
    else:
        print("\n⚠️ Nenhum dado foi salvo pois a lista está vazia.")
