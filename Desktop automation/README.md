# Desktop Automation Tool

## Módulos utilizados (y documentación)

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/) - Para simular los clics del mouse
- [pynput](https://pynput.readthedocs.io/en/latest/) - Para capturar eventos del mouse y teclado

## Requisitos

1. Python 3.7 o superior
2. Sistema operativo compatible (Windows, Linux o MacOS)

## Creación del entorno virtual e instalación de módulos

```bash
python -m venv env
.\env\Scripts\activate # (Windows)
# source env/bin/activate (Linux)

python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Uso

### Uso del script [main.py](main.py)

1. Ejecutar el script:
    ```bash
    python main.py
    ```

2. Comandos disponibles:
   - Presiona `s` para iniciar/detener la grabación de clics
   - Presiona `p` para reproducir la secuencia de clics grabada
   - Presiona `q` para salir del programa

3. Funcionamiento:
   - Al iniciar la grabación (`s`), el programa registrará la posición y el tiempo entre cada clic
   - Al reproducir (`p`), el programa ejecutará la secuencia de clics con los mismos intervalos de tiempo
   - La secuencia se mantiene en memoria hasta que:
     - Se inicia una nueva grabación
     - Se cierra el programa

### Notas importantes

- La herramienta registra las coordenadas absolutas de la pantalla
- Asegúrate de que las ventanas y elementos estén en la misma posición durante la reproducción
- La secuencia se perderá al cerrar el programa
- Es recomendable tener un punto de referencia claro antes de iniciar la grabación

## Características

- Grabación de secuencias de clics
- Registro de intervalos de tiempo entre clics
- Reproducción precisa de las secuencias
- Interfaz simple mediante teclas de control
- Ejecución en segundo plano

## Limitaciones actuales

- No guarda las secuencias de forma permanente
- No registra acciones del teclado
- No captura clics del botón derecho
- Las coordenadas son absolutas (no relativas a ventanas)

## Próximas mejoras planeadas

- Guardar/cargar secuencias en archivo
- Añadir soporte para teclas y botón derecho
- Implementar coordenadas relativas
- Añadir interfaz gráfica básica

## Créditos

Desarrollado como herramienta de automatización de escritorio utilizando las librerías pyautogui y pynput.