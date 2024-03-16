import pyautogui
import time
from pynput.mouse import Listener
import json

votos_filename = 'votos.json'
# Função para ler a contagem de votos do arquivo
def ler_votos():
    try:
        with open(votos_filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"votos": 0}

# Função para atualizar a contagem de votos no arquivo
def atualizar_votos(votos):
    with open(votos_filename, 'w') as file:
        json.dump(votos, file)


# Solicitar ao usuário o número de cliques que deseja contar
def user():
   return int(input("Quantos clicks você deseja contar?:"))

max_clicks = user()
clicks_coordinates = []  # Lista para armazenar as coordenadas

def on_click(x, y, button, pressed):
    if pressed:
        clicks_coordinates.append((x, y))  # Adicionar coordenadas à lista
        print(f'Coordenadas do click {len(clicks_coordinates)}: {x}, {y}')
        if len(clicks_coordinates) == max_clicks:
            return False  # Parar de ouvir os cliques quando atingir o limite

# Iniciar listener para coletar cliques
listener = Listener(on_click=on_click)
listener.start()
listener.join()
votos = ler_votos()



# Realizar os cliques conforme as coordenadas coletadas
while True:
    for idx, (x, y) in enumerate(clicks_coordinates, start=1):
        time.sleep(2.5)
        pyautogui.click(x=x, y=y)
        print(f'Click {idx} executado em ({x}, {y})!') 
        time.sleep(1.5)
        # Incrementar a contagem de votos após cada ciclo de cliques e atualizar o arquivo
    votos["votos"] += 1
    atualizar_votos(votos)
    

