import time
import threading
import pyautogui
from pynput import mouse, keyboard

# Variables para almacenar datos
recording = False
playing = False
clicks = []

def on_click(x, y, button, pressed):
    """ Registra clics solo si estamos en modo grabación. """
    global recording, clicks
    if recording and pressed:
        timestamp = time.time()  # Momento exacto del clic
        if len(clicks) > 0:
            delay = timestamp - clicks[-1][2]  # Tiempo desde el último clic
        else:
            delay = 0  # Primer clic sin retraso
        clicks.append((x, y, timestamp, delay))
        # print(clicks)

def on_press(key):
    """ Maneja eventos de teclado. """
    global recording, playing, clicks

    try:
        if key.char.lower() == 's':  # Tecla para iniciar/detener grabación
            if not recording:
                clicks.clear()
                print("Grabación iniciada...")
            else:
                print("Grabación finalizada.")
            recording = not recording

        elif key.char.lower() == 'p':  # Tecla para iniciar la reproducción
            if not recording and clicks:
                print("Ejecutando acciones grabadas...")
                playing = True
                play_actions()
                playing = False
                print("Reproducción finalizada.")
        
        elif key.char.lower() == 'q':
            # Tecla para salir del programa
            print("Saliendo...")
            recording = False
            playing = False
            # Detener los listeners de forma segura
            keyboard_listener.stop()
            mouse_listener.stop()
            # Esperar a que los listeners se detengan completamente
            # keyboard_listener.join()
            # mouse_listener.join()
            return False  # Detiene el listener

    except AttributeError:
        pass

def play_actions():
    """ Ejecuta los clics grabados con los tiempos guardados. """
    for i, (x, y, timestamp, delay) in enumerate(clicks):
        if i == 0:
            pyautogui.click(x, y)  # Realiza el primer clic sin esperar
            print(f"Clic inicial en ({x}, {y})")
        else:
            time.sleep(delay)  # Espera el tiempo registrado
            pyautogui.click(x, y)  # Realiza el clic
            print(f"Clic en ({x}, {y}) después de {delay:.2f}s")

print("Iniciando el programa...")

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
