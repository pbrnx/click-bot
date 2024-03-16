from pynput.mouse import Listener

i = 0
def user():
   return int(input("Quantos clicks você deseja contar?:"))

max_clicks = user()

def on_click(x, y, button, pressed):
    global i
    if pressed:
        i += 1
        print(f'Coordenadas do click {i}: {x}, {y}')
        if i == max_clicks:
            return False

listener = Listener(on_click=on_click)
listener.start()
listener.join()