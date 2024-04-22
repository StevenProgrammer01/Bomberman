import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from juego import Nivel,Personalizacion
import winsound
import threading
def play_song():
    winsound.PlaySound(".//Sounds//mainSong.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_song():
    winsound.PlaySound(None, winsound.SND_PURGE)
def ReproducirSonido(name):
    winsound.PlaySound(name,winsound.SND_FILENAME)
def P_personalizacion():
    # Función para abrir la ventana de personalización
    configuracion_window = tk.Toplevel(root)
    configuracion_window.title("Pantalla de Configuración")
    configuracion_window.geometry("300x200")
    #Botón para reproducir canción
    play_button = tk.Button(configuracion_window, text="Play Song", command=play_song)
    play_button.grid(row=0, column=0)
    #Botón para pausar canción
    stop_button = tk.Button(configuracion_window, text="Stop Song", command=stop_song)
    stop_button.grid(row=0, column=1)
    # Aquí puedes agregar los widgets y funcionalidades de la ventana de personalización

def P_informacion():
    # Función para abrir la ventana de información
    configuracion_window = tk.Toplevel(root)
    configuracion_window.title("Pantalla de Información")
    configuracion_window.geometry("300x200")
    # Aquí puedes agregar los widgets y funcionalidades de la ventana de configuración

def P_mejores_puntajes():
    # Función para abrir la ventana de mejores puntajes
    mejores_puntajes_window = tk.Toplevel(root)
    mejores_puntajes_window.title("Mejores Puntajes")
    mejores_puntajes_window.geometry("300x200")
    # Aquí puedes agregar los widgets y funcionalidades de la ventana de mejores puntajes

def P_juego():

    Personalizacion(root)
    #Nivel(root,1, 4, 10, 180)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("800x600")

#Usamos pillow para la imágen de fondo para poder manipularla mejor y no generar errores
background_image = Image.open("fondo.jpeg")
background_image = background_image.resize((800, 600))
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Crear el menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

sound = threading.Thread(target=play_song)
sound.start()
# Menú desplegable "Opciones"


boton_configuracion = tk.Button(root, text="Configuración", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=P_personalizacion)
boton_configuracion.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
boton_mejores_puntajes = tk.Button(root, text="Mejores Puntajes", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=P_mejores_puntajes)
boton_mejores_puntajes.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
boton_info = tk.Button(root, text="Información", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=P_informacion)
boton_info.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
boton_inicio = tk.Button(root, text="Iniciar Juego",bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=P_juego)
boton_inicio.place(relx=0.85, rely=0.94, anchor=tk.CENTER)

root.mainloop()
