# Por si acaso necesitamos estas funciones algún día:
# os.getcwd() Función para obtener la ruta del directorio actual
# os.listdir(r"C:\Music") Función para listar los nombres de los archivos en un directorio

# IMPORTANTE: Coloca tus canciones en la carpeta C:\Music
print("\n- - - - Reproductor de música con Python - - - -\n")

import os
import vlc
import time #Para poder hacer una pequeña pausa antes de repetir la cancion


# Creamos un diccionario Canciones, una lista con las direcciones de las canciones en la carpeta C:\Music, y la lista de reproducción actual
Canciones = {}
CancionesDir = []
Playlist = {}
player = vlc.MediaPlayer()

# Función scan: arma el diccionario de canciones desde cero - ALERTA: ESTA FUNCIÓN RESETEA EL DICCIONARIO DE CANCIONES Y EL DIRECTORIO DE CANCIONES
def scan():
    # Uso de os para escanear carpeta "Music", y añadir los nombres de los archivos que contiene a una lista
    ListaCanciones = []
    ListaCanciones = os.listdir(r"C:\Music") #La r nos permite omitir las secuencias de la diagonal en el string.

    #Limpiamos el diccionario de canciones y el directorio de canciones.
    Canciones.clear()
    CancionesDir.clear()

    #Llenamos el diccionario de canciones y el directorio de canciones.
    CC = 1
    for i in ListaCanciones:
        Canciones[CC] = i
        CancionesDir.append(os.path.join(r"C:\Music",i)) #De nuevo, recuerden incluír la r antes del string de dirección.
        CC+=1
    return


# Cada vez que se ejecuta el programa, siempre ejecutamos la función scan 1 vez:
scan()

# Función para que el usuario pueda apreciar la lista de canciones:
def listarcanciones():
    print("Canciones disponibles:\n")
    for i in Canciones:
        print(i," - ",Canciones[i])
    print()
    return

# Cada vez que se ejecuta el programa, listamos las canciones disponibles:
listarcanciones()

# Función para comprobar el directorio de canciones:
def comprobarDir():
    print("Directorio de canciones:\n")
    for i in CancionesDir:
        print(i)
    print()

# Comprobación del directorio. SOLO PARA PRUEBAS: BORRAR O CONVERTIR EN COMENTARIO AL MOMENTO DE ENTREGAR EL PROYECTO.
#comprobarDir()


# --------------------------- FIN DE CÓDIGO INICIAL ---------------------------


def iniciar_reproductor(ruta):
    #Crea una instancia de VLC y reproduce la cancion.
    player = vlc.MediaPlayer(ruta) #Ruta sera el parametro donde pondremos de donde agarra los archivos .mp3, pero aqui aun no agarra cualquier archivo .mp3 solo el especificado
    player.play()
    print("Reproduciendo cancion\n")
    return player

#Solo para que el usuario vea los comandos
def mostrar_comandos():
    """Muestra los controles disponibles para el usuario."""
    print("Controles de reproducción:")
    print("- play       →   Reanudar cancion")
    print("- pause      →   Pausar/reanudar cancion")
    print("- repeat     →   Reproducir cancion actual desde el inicio")
    print("- menu       →   Detiene la cancion y regresa al menu principal\n")

#Bucle para que no se cierre el programa
def manejar_comando(comando, player):
    #Condiciona para que el reproductor haga algo dependiendo del comando
    if comando == "play":
        player.play()
        print("Canción reanudada.\n")

    elif comando == "pause":
        player.pause()
        print("Canción pausada.\n")

    elif comando == "repeat":
        player.stop()
        time.sleep(0.3)
        player.play()
        print("Canción reiniciada.\n")

    elif comando == "menu":
        player.stop()
        print("Canción detenida. Regresando a menu principal.\n") 
        return False  #Señal para salir del bucle, osea que el usuario pueda cerrarlo

    else:
        print("Comando no reconocido. Usa 'play', 'pause', 'repeat' o 'menu'.\n")

    return True


def ejecutar_reproductor(ruta):
    """Función principal del reproductor de música."""
    player = iniciar_reproductor(ruta)
    mostrar_comandos()

    while True:
        estado = player.get_state()

        #Detecta si la cancion termino, pero no cierra el programa hasta que el usuario use el comando 'exit'
        if estado == vlc.State.Ended:
            print("La cancion ha terminado.")
            print("Que deseas hacer?")
            print("1. Reproducir otra cancion (regresar al menu)")
            print("2. Repetir esta cancion")
            print("3. Salir del programa\n")
            
            eleccion = input("Elige una opción (1, 2 o escribe 'menu'): ").strip().lower()
            if eleccion == "1" or eleccion == "menu":
                player.stop()
                break
            elif eleccion == "2" or eleccion == "repeat":
                player.stop()
                time.sleep(0.3)
                player.play()
                print("🔁  Reproduciendo de nuevo...\n")
                continue
            elif eleccion == "3" or eleccion == "exit":
                player.stop()
                print("👋  Reproductor cerrado.")
                exit()
        comando = input("> ").strip().lower()
        if not manejar_comando(comando, player):
            break

        

def Menu():

    print("- - - - Menú principal - - - -\n")
    menu = True
    while menu == True:
        opcion = None
        print("Ingresa un comando: \n\n 'play' = Reproduce una cancion de tu elección.\n 'exit' = Salir.\n")
        opcion = input()
        print()

        # Modo de reproducción de 1 cancion
        if opcion == "play":
            print("- - - - Reproduciendo una cancion - - - -\n")
            listarcanciones()

            # Blucle para selección de cancion. Rechaza cosas que no sean números enteros. (CRASHEA CON NÚMEROS FUERA DEL RANGO DE CANCIONES. <= CORREGIDO 15/11/25)
            a = True
            while a:
                print("Escribe el número de la cancion a reproducir:")
                cancion = input()
                print()

                # Valida que sea entero
                try:
                    cancion = int(cancion)
                except:
                    print("Error: Por favor ingresa un número entero.\n")
                    continue
    
                # Valida que esté dentro del rango
                if cancion < 1 or cancion > len(CancionesDir):
                    print(f"Error: Ingresa un número entre 1 y {len(CancionesDir)}.\n")
                    continue

                # Si pasa ambas sale del bucle
                a = False

            c = int(cancion) - 1
            ejecutar_reproductor(CancionesDir[c])

        # Si el usuario desea cerrar el menu.
        elif opcion == "exit":
            print("Reproductor cerrado.\n")
            menu = False
        
        # Si el usuario no ingresa un comando reconocido por el menu.
        else:
            print("Comando no valido.\n")
    
    # Al cerrar el menu, cerramos el programa.
    exit()



# --------------------------- PROGRAMA PRINCIPAL ---------------------------

if __name__ == "__main__":    
        Menu()