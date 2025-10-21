import time
# import threading
import pyautogui
from pynput import mouse, keyboard

# Variables para almacenar datos
recording = False
playing = False
actions = []  # Lista de acciones: (tipo, datos, timestamp, delay)
# tipo puede ser 'click' o 'text'
# datos será (x,y) para clicks o el texto para escritura

def on_click(x, y, button, pressed):
    """ Registra clics solo si estamos en modo grabación. """
    global recording, actions
    if recording and pressed:
        timestamp = time.time()
        if len(actions) > 0:
            delay = timestamp - actions[-1][2]
        else:
            delay = 0
        actions.append(('click', (x, y), timestamp, delay))

def on_press(key):
    """ Maneja eventos de teclado. """
    global recording, playing, actions

    try:
        # Detectar teclas especiales
        if key == keyboard.Key.right:  # Flecha derecha para grabar
            if not recording:
                actions.clear()
                print("Grabación iniciada...")
            else:
                print("Grabación finalizada.")
            recording = not recording
            
        elif key == keyboard.Key.left:  # Flecha izquierda para reproducir
            if not recording and actions:
                print("Ejecutando acciones grabadas...")
                playing = True
                play_actions()
                playing = False
                print("Reproducción finalizada.")
        
        elif key == keyboard.Key.esc:  # Esc para salir
            print("Saliendo...")
            recording = False
            playing = False
            keyboard_listener.stop()
            mouse_listener.stop()
            return False
            
        # Grabar texto normal durante la grabación
        elif recording and hasattr(key, 'char'):  # Si es un carácter imprimible
            timestamp = time.time()
            if len(actions) > 0:
                delay = timestamp - actions[-1][2]
            else:
                delay = 0
            actions.append(('text', key.char, timestamp, delay))

    except AttributeError:
        pass

def play_actions():
    """ Ejecuta las acciones grabadas con los tiempos guardados. """
    for i, (action_type, data, timestamp, delay) in enumerate(actions):
        if i > 0:  # Esperar el delay para todas las acciones excepto la primera
            # time.sleep(delay)
            time.sleep(0.1)
            
        if action_type == 'click':
            x, y = data
            pyautogui.click(x, y)
            print(f"Clic en ({x}, {y}) después de {delay:.2f}s")
        elif action_type == 'text':
            pyautogui.write(data)
            print(f"Escribiendo '{data}' después de {delay:.2f}s")

print("Iniciando el programa...")
print("Presiona FLECHA DERECHA para iniciar/detener la grabación")
print("Presiona FLECHA IZQUIERDA para reproducir")
print("Presiona ESC para salir")

# Configurar listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Ejecutar en segundo plano
mouse_listener.start()
keyboard_listener.start()

try:
    # Mantener el programa corriendo
    mouse_listener.join()
    keyboard_listener.join()
finally:
    # Asegurar que los listeners se detengan incluso si hay una excepción
    mouse_listener.stop()
    keyboard_listener.stop()
