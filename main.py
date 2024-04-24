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
    d = tk.Toplevel(root)
    d.minsize(800,800)# tamaño de root
    d.resizable(width=False,height=False)# no se hace mas pequña
    d.title("About Me")
    def Instrucciones():
        intrucciones = tk.Toplevel(d)
        intrucciones.minsize(1200,800)# tamaño de root
        intrucciones.resizable(width=False,height=False)# no se hace mas pequña
        intrucciones.title("Instrucciones")
        instrucciones_label = tk.Label(intrucciones, text= "Instrucciones del juego", font=("Helvetica", 18, "bold"), fg="navy")
        instrucciones_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        text = """-Este juego está inspirado en Bomberman\n
        -Tiene una jugabilidad muy semejante\n
        -Está constituido por 3 niveles, para pasar cada nivel usted deberá ir destruyendo con las bombas los muros,\n 
        en alguno de ellos estará escondida una llave que le permitirá pasar al siguiente nivel\n
        -Las teclas necesarias para el juego son:\n
            *Arriba/Abajo\n
            *Izquierda/Derecha\n
            *Espacio (Colocar bombas)\n
        -Con las bombas podrá ir destruyendo a sus enemigos y sumando más puntos"""
        instrucciones_label = tk.Label(intrucciones, text=text, font=("Helvetica", 14, "bold"), fg="navy")
        instrucciones_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    #Nombre
    name_label = tk.Label(d, text="Autor: Steven Pérez Aguilar", font=("Helvetica", 18, "bold"), fg="navy")
    name_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    #Imágen del Estudiante
    image_path = r".//fotoEstudiante.jpg"
    image = Image.open(image_path)
    image = image.resize((300,200))
    photo = ImageTk.PhotoImage(image)
    imagen = tk.Label(d, image= photo)
    imagen.place(relx=0.5, rely = 0.25, anchor=tk.CENTER) 
    carnet = tk.Label(d, text="Carnet: 2024118003", font=("Helvetica", 14, "bold"), fg="navy")
    carnet.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    institute = tk.Label(d, text="Instituto Tecnológico de Costa Rica", font=("Helvetica", 14, "bold"), fg="navy")
    institute.place(relx=0.5, rely=0.49, anchor=tk.CENTER)
    carrera = tk.Label(d, text="Carrera: Ingeniería en Computadores 2024", font=("Helvetica", 14, "bold"), fg="navy")
    carrera.place(relx=0.5, rely=0.53, anchor=tk.CENTER)
    profesor = tk.Label(d, text="Profesor: Jason Leitón Jiménez", font=("Helvetica", 14, "bold"), fg="navy")
    profesor.place(relx=0.5, rely=0.57, anchor=tk.CENTER)
    pais = tk.Label(d, text="Pais de Producción: Costa Rica", font=("Helvetica", 14, "bold"), fg="navy")
    pais.place(relx=0.5, rely=0.61, anchor=tk.CENTER)
    version = tk.Label(d, text="Versión del juego: Beta 0.0.1", font=("Helvetica", 14, "bold"), fg="navy")
    version.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    boton_instrucciones = tk.Button(d, text="Instrucciones", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Instrucciones)
    boton_instrucciones.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    d.mainloop()



def P_mejores_puntajes():
    # Función para abrir la ventana de mejores puntajes
    def MejoresPuntajesAux(level, root):
        mejores_puntajes_window_aux = tk.Toplevel(root)
        mejores_puntajes_window_aux.title(f"Mejores Puntajes nivel {level}")
        def LeerArchivo(level):
            ruta=f"{level}.txt"
            archivo=open(ruta) # coloca el contenido en memoria
            contenido=archivo.readlines()
            archivo.close()
            return contenido 
        def Mayor(Registros, res):
            if Registros == []:
                res = res.split("@")
                #return f"El registro con más edad es: {res[0]+" "+res[1]} con {res[2][:len(res[2])-1]} años"
                return res
            elif int(Registros[0].split("@")[1][:len(Registros[0])-1])>int(res.split("@")[1]):
                return Mayor(Registros[1:], Registros[0])
            else:
                return Mayor(Registros[1:], res)
        content = LeerArchivo(level)
        def mostrar(contenido,allregistrys, row):
            if contenido == []:
                return
            else:
                registro = contenido[0].split("@")
                #registro = Edad_Mayor(allregistrys, contenido[0])
                print(registro)
                registry= tk.Label(mejores_puntajes_window_aux,text=f"Nombre: {registro[0]} Puntaje: {registro[1]}", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
                registry.grid(row=row, column=0)
                mostrar(contenido[1:],allregistrys, row+1)

        mostrar(content,content,0)
    mejores_puntajes_window = tk.Toplevel(root)
    mejores_puntajes_window.title("Mejores Puntajes")
    PuntajesNivel1 = tk.Button(mejores_puntajes_window, text="Nivel 1", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:MejoresPuntajesAux(1,mejores_puntajes_window))
    PuntajesNivel1.grid(row=0, column=0)
    PuntajesNivel2 = tk.Button(mejores_puntajes_window, text="Nivel 2", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:MejoresPuntajesAux(2,mejores_puntajes_window))
    PuntajesNivel2.grid(row=1, column=0)
    PuntajesNivel3 = tk.Button(mejores_puntajes_window, text="Nivel 3", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=lambda:MejoresPuntajesAux(3,mejores_puntajes_window))
    PuntajesNivel3.grid(row=2, column=0)
    


    # Aquí puedes agregar los widgets y funcionalidades de la ventana de mejores puntajes

def P_juego():

    Personalizacion(root)
    #Nivel(root,1, 4, 10, 180)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("800x600")

#Usamos pillow para la imágen de fondo para poder manipularla mejor y no generar errores
background_image = Image.open(".//fondo.jpeg")
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
