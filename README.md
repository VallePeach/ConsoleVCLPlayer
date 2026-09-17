# Reproductor de Música CLI en Python

Un reproductor de música interactivo desarrollado en **Python** que funciona directamente desde la consola (Terminal). Utiliza la potencia del motor multimedia de **VLC** (`python-vlc`) para la reproducción de archivos de audio locales y cuenta con un sistema robusto de validación de entradas para evitar errores de ejecución.

## Características Principales

- **Escaneo automático:** Detecta y numera automáticamente todas las canciones disponibles en el directorio de música.
- **Controles interactivos:** Permite pausar, reanudar, repetir o detener la canción actual mediante comandos de texto en tiempo real.
- **Gestión de estados:** Detecta automáticamente cuándo una canción finaliza y ofrece opciones claras para continuar.
- **Validación de errores:** 
- Control de excepciones para evitar bloqueos si el usuario ingresa letras en lugar de números.
- Validación de rangos numéricos para evitar errores de índice (`IndexError`) si se selecciona un número fuera de la lista.

## Prerrequisitos y Requisitos Técnicos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente en tu sistema:

1. **Python 3.x** instalado en tu computadora.
2. **VLC Media Player** instalado oficialmente en tu sistema (necesario para que la librería interactúe con el motor de audio). Puedes descargarlo desde [videolan.org](https://www.videolan.org/).

## Instalación y Configuración

**Clona este repositorio o descarga los archivos:**
   git clone [https://github.com/VallePeach/ConsoleVCLPlayer](https://github.com/VallePeach/ConsoleVCLPlayer)

	- Instala la dependencia de Python para VLC
	pip install python-vlc

	Por defecto, el script busca los archivos en la ruta C:\Music.
	Asegúrate de crear una carpeta llamada Music en el disco C: y coloca allí tus archivos .mp3 (o ajusta la ruta en el código si prefieres otra ubicación).

Ejecuta el script principal desde tu terminal: python "ConsoleVCLPlayer.py"

Una vez abierto el menú principal:

1. Escribe play y presiona Enter.
2. Selecciona el número correspondiente a la canción que deseas escuchar.
3. Utiliza los controles disponibles mientras suena la música:
play -> Reanuda la reproducción.
pause -> Pausa o reanuda la canción.
repeat -> Reinicia la canción actual.
menu -> Detiene la pista actual y regresa al menú principal.
exit -> Cierra el programa por completo.
