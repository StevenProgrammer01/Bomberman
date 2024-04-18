import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import random
laberinto = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', 'X', 'Y', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', 'Y', 'Y', 'X'],
        ['X', 'Y', 'X', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'X', 'X'],
        ['X', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'P', ' ', 'Y', ' ', 'Y', 'Y', 'Y', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', 'Y', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

def Nivel1(root):
     # Crear la ventana del juego
    ventana = tk.Toplevel(root)
    ventana.title("Laberinto")
    ventana.config(bg="Green")
    
    global personaje_imagen
    global imagen_actual
    global personaje_posicion
    global personaje
    global bomba_posicion
    global fire
    global enemigo
    global posiciones_destructibles
    global posicion_llave
    global llave_encontrada 
    global posicion_puerta
    
    #Inicializar variables globales del juego
    posicion_puerta = []
    llave_encontrada = False
    imagen_actual = "1"
    personaje_imagen = Image.open(f"Bomberman Images//2-{imagen_actual}.png")
    personaje_imagen = personaje_imagen.resize((40, 40))
    personaje_imagen = ImageTk.PhotoImage(personaje_imagen)
    bomba_posicion=[]
    personaje_posicion = [2,1]
    posiciones_destructibles = []
    #Funciones de jugador
    

    ################################################
    def cargarImagen(name, row, column):
        imagen = Image.open(f"Bomberman Images//{name}.png")  
        imagen = imagen.resize((44, 44))
        imagen = ImageTk.PhotoImage(imagen)
        label = tk.Label(ventana, image=imagen,borderwidth=0, highlightthickness=0)
        label.image = imagen
        label.grid(row=row, column=column)
    def desplegar_personaje():
        global personaje
        personaje = tk.Label(ventana, image=personaje_imagen, fg = "#408404", bg="#408404")
        personaje.grid(row=personaje_posicion[0], column=personaje_posicion[1])
    def cambiarImagenPersonaje(categoría, imagen):
        global personaje_imagen
        personaje_imagen = Image.open(f"Bomberman Images//{categoría}-{imagen}.png")
        personaje_imagen = personaje_imagen.resize((40, 40))
        personaje_imagen = ImageTk.PhotoImage(personaje_imagen)
        personaje.config(image=personaje_imagen)
        ventana.update()

    def animacion_moveAux(cat_move):
        global imagen_actual
        if imagen_actual == "1":
            imagen_actual = "0"
        elif imagen_actual == "0":
            imagen_actual = "2"
        elif imagen_actual == "2":
            imagen_actual = "1"
        cambiarImagenPersonaje(cat_move,imagen_actual)
        

    def Movimiento(move):
        if move == "Up":
            return animacion_moveAux("2")
        elif move == "Right":
            return animacion_moveAux("0")
        elif move == "Left":
            return animacion_moveAux("1")
        elif move == "Down":
            return animacion_moveAux("2")
        
        if move == "space":
            return colocarBomba()
        
    def colocarBomba():
        global personaje_posicion
        global bomba_posicion
        global bomba
        bomba_imagen= Image.open(r"Bomberman Images\bomba0.png")
        bomba_imagen = bomba_imagen.resize((40, 40))
        bomba_imagen = ImageTk.PhotoImage(bomba_imagen)
        bomba = tk.Label(ventana, image=bomba_imagen, fg = "Green", bg="Green")
        bomba.image = bomba_imagen
        bomba_posicion = [personaje_posicion[0],personaje_posicion[1]]
        bomba.grid(row=bomba_posicion[0], column=bomba_posicion[1])
        ventana.update()
        hilo_bomba_animación = threading.Thread(target=Bomba, args=(bomba_posicion[0],bomba_posicion[1] ))
        hilo_bomba_animación.start()

    def mover_personaje(event):
        global personaje_posicion
        tecla = event.keysym
        nueva_fila, nueva_columna = personaje_posicion
        
        if tecla == "Up":
            nueva_fila -= 1
        elif tecla == "Down":
            nueva_fila += 1
        elif tecla == "Left":
            nueva_columna -= 1
        elif tecla == "Right":
            nueva_columna += 1
        Movimiento(tecla)
        if es_accesible_personaje(nueva_fila, nueva_columna):
            #Crear nueva posición, cambiando el valor de la variable global posición
            personaje_posicion = [nueva_fila, nueva_columna]
            #Actualizando la los valores de la posición del personaje
            personaje.grid(row=nueva_fila, column=nueva_columna)
#Funciones de explosión y esparcimiento de la bomba
    def Bomba(row, column):
        global bomba
        time.sleep(3)
        rigth = threading.Thread(target=esparcimiento_fuego, args=(row, column, 0, "right"))
        rigth.start()
        left = threading.Thread(target=esparcimiento_fuego, args=(row, column, 0, "left"))
        left.start()
        up = threading.Thread(target=esparcimiento_fuego, args=(row, column, 0, "up"))
        up.start()
        down = threading.Thread(target=esparcimiento_fuego, args=(row, column, 0, "down"))
        down.start()
        time.sleep(2)
        mostrar_laberinto(0,0)   
        #desplegar_personaje() 
    def esparcimiento_fuego(x, y, iterator, direction):

        if iterator < 5 and es_accesible_bomba(x, y):
            fireImage= Image.open(fr"Bomberman Images\Fuego{iterator}.png")
            fireImage = fireImage.resize((40, 40))
            fireImage = ImageTk.PhotoImage(fireImage)
            fire = tk.Label(ventana, image=fireImage, fg = "Green", bg="Green")
            fire.image = fireImage
            fire.grid(row=x, column=y)
            laberinto[x][y] = " "
            
            if direction == "right":
                #time.sleep(0.05)
                ventana.update()
                esparcimiento_fuego(x,y+1, iterator+1, "right")
            elif direction == "left":
                #time.sleep(0.05)
                #fire.destroy()
                
                ventana.update()
                esparcimiento_fuego(x,y-1, iterator+1, "left")
            elif direction == "up":
                #time.sleep(0.05)
                #fire.destroy()
                
                ventana.update()
                esparcimiento_fuego(x-1,y, iterator+1, "up")
            elif direction == "down":
                #time.sleep(0.05)
                #fire.destroy()
                ventana.update()
                esparcimiento_fuego(x+1,y, iterator+1, "down")
    ################################################
    def Enemigos():
        global enemigo
        enemigo_imagen = Image.open(f"Bomberman Images//2-{imagen_actual}.png")
        enemigo_imagen = personaje_imagen.resize((40, 40))
        enemigo_imagen = ImageTk.PhotoImage(personaje_imagen)
        enemigo = tk.Label(ventana, image=personaje_imagen, fg = "#408404", bg="#408404")
        enemigo.grid(row=14, column=2)

    #Funciones para la llave oculta

    def posicion_random_con_espacios():
        # Encontrar las posiciones con valor " " utilizando la función recursiva
        global posiciones_destructibles

        # Elegir una posición aleatoria de las posiciones con valor " "
        posicion_elegida = random.choice(posiciones_destructibles)
        print (posicion_elegida)
        return posicion_elegida




    ################################################
        
    def mostrar_laberinto(x=0, y=0):
        global posiciones_destructibles
        global posicion_puerta
        if x >= len(laberinto) or y >= len(laberinto[0]):
            pass
        if laberinto[x][y] != ' ' or laberinto[x][y] == "Z":
            if laberinto[x][y]=="Y":
                posiciones_destructibles +=[[x,y]]
            if laberinto[x][y] == "Z":
                cargarImagen("Y", x, y)
            elif laberinto[x][y] == "E":
                cargarImagen("llave", x, y)
            elif laberinto[x][y] == "P":
                posicion_puerta = [x,y]
                cargarImagen("puerta", x, y)
            else:
                cargarImagen(laberinto[x][y], x, y)
            ventana.update()
        else:
            cargarImagen("pasto", x, y)
            desplegar_personaje()
            ventana.update()
        if y < len(laberinto[0]) - 1: #Eval+ua si la posición de la matriz [x][y] en y no ha llegado al límite
            mostrar_laberinto(x, y + 1)
        elif x < len(laberinto) - 1:#Eval+ua si la posición de la matriz [x][y] en x no ha llegado al límite
            mostrar_laberinto(x + 1, 0)
        
        
    
   
    #Código basado en ChatGPT
    def es_accesible_personaje(fila, columna):
        global posicion_puerta
        global llave_encontrada
        if fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]):
            return False
        elif fila == posicion_puerta[0] and columna == posicion_puerta[1] and llave_encontrada:
            print("Pasaste Nivel 1")
        return laberinto[fila][columna] == ' ' # Retorna True solo si el valor accedido en la matriz sea == " "
    #Código basado en ChatGPT
    def es_accesible_bomba(fila, columna):
        global posicion_llave
        global llave_encontrada
        if fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]):
            return False
        elif fila == posicion_llave[0] and columna == posicion_llave[1]:
            laberinto[fila][columna] = "E"
            llave_encontrada = True
        return laberinto[fila][columna] == ' ' or laberinto[fila][columna] == "Y" or laberinto[fila][columna] == "Z"# Retorna True solo si el valor accedido en la matriz sea == " "
    #Crear posición random de la llave
    mostrar_laberinto(0,0)
    posicion_llave = posicion_random_con_espacios()
    laberinto[posicion_llave[0]][posicion_llave[1]] = "Z"

    # Mostrar el laberinto
    print(laberinto)
    ventana.bind("<KeyPress>", mover_personaje)
    boton_configuracion = tk.Button(ventana, text="Configuración", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
    boton_configuracion.place(relx=0.0, rely=0.0, anchor=tk.CENTER)
    ventana.mainloop()


