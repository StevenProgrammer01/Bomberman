import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import random
import datetime
import time
laberinto = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'],
        ['X', 'Y', ' ', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', 'Y', 'Y', 'X'],
        ['X', 'Y', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', ' ', 'Y', 'X'],
        ['X', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', 'X', ' ', 'Y', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'Y', 'X', 'Y', ' ', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'X', 'X'],
        ['X', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'P', ' ', 'Y', ' ', 'Y', 'Y', 'Y', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

def Nivel(root, skin_code,lifes, bombs, duración):
     # Crear la ventana del juego
    ventana = tk.Toplevel(root)
    ventana.title("Laberinto")
    ventana.config(bg="Green")
    
    
    global vidas, llave_encontrada,bombas,puntuacion, enemy1, enemy2, tiempo
    global fire, enemigo1, enemigo2,personaje
    global enemigoImagen1, enemigoImagen2,personaje_imagen,imagen_actual
    global posicionEnemigo1, posicionEnemigo2,posicion_puerta,posiciones_destructibles, posicion_llave, personaje_posicion,bomba_posicion
    global lista_explosiones
    global skin
    #Inicializar variables globales del juego
    posicionEnemigo1 = [8,17]
    posicionEnemigo2 = [14,12]
    posicion_puerta = []
    llave_encontrada = False
    imagen_actual = "1"
    bomba_posicion=[]
    personaje_posicion = [2,1]
    posiciones_destructibles = []
    vidas = lifes
    bombas = bombs
    lista_explosiones = [] 
    enemy1 = True
    enemy2 = True
    puntuacion = 0
    tiempo = duración
    skin = skin_code
    #Funciones de jugador
    

    ################################################
    #Código basado en ChatGPT
    def countdown(duration):
        remaining_time = datetime.timedelta(seconds=duration)
        while remaining_time.total_seconds() > 0:
            Time= tk.Label(ventana,text=remaining_time, bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
            Time.place(relx=0.0, rely=0.0)
            time.sleep(1)
            remaining_time -= datetime.timedelta(seconds=1)
        

    def funcionvidas(vidas):
        if vidas <= 0:
            ventana.destroy()
        else:
            Vida= tk.Label(ventana,text=str(vidas)+"X", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
            Vida.grid(row=1, column=0)
            cargarImagen("life",1,1)
            ventana.update()
    
    def incrementa_puntos(puntos):
        score= tk.Label(ventana,text="Puntuación"+str(puntos), relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
        score.place(relx=0.5, rely=0)
    
    def cargarImagen(name, row, column):
        imagen = Image.open(f"Bomberman Images//{name}.png")  
        imagen = imagen.resize((44, 44))
        imagen = ImageTk.PhotoImage(imagen)
        label = tk.Label(ventana, image=imagen,borderwidth=0, highlightthickness=0)
        label.image = imagen
        label.grid(row=row, column=column)

    def find_key(row, column):
        global llave_encontrada, posicion_llave
        if row == posicion_llave[0] and column == posicion_llave[1]:
            laberinto[row][column] = "E"
            llave_encontrada = True
            
   ##################################################
   #Colisiones
    def colisiones_personaje(row, column, row2, column2):
        global vidas
        if row == row2 and column == column2:
                vidas -= 1
                #funcionvidas(vidas)
                mostrar_laberinto(0,0)
    def colisiones_bomba():
        global lista_explosiones, personaje_posicion, vidas, posicionEnemigo1, posicionEnemigo2,enemy1, enemy2,puntuacion
        if personaje_posicion in lista_explosiones:
            vidas -= 1
            #funcionvidas(vidas)
            mostrar_laberinto(0,0)
        if posicionEnemigo1 in lista_explosiones:
            enemy1 = False
            puntuacion += 10
            enemigo1.destroy()
        if posicionEnemigo2 in lista_explosiones:
            enemy2 = False
            puntuacion += 25
            enemigo2.destroy()

            
################################################################################
#Personaje principal
    def desplegar_personaje():
        global personaje, personaje_imagen, skin
        personaje_imagen = Image.open(f"Bomberman Images//{skin}-2-{imagen_actual}.png")
        personaje_imagen = personaje_imagen.resize((40, 40))
        personaje_imagen = ImageTk.PhotoImage(personaje_imagen)
        personaje = tk.Label(ventana, image=personaje_imagen, fg = "#408404", bg="#408404")
        personaje.grid(row=personaje_posicion[0], column=personaje_posicion[1])

    def cambiarImagenPersonaje(categoría, imagen):
        global personaje_imagen, skin
        personaje_imagen = Image.open(f"Bomberman Images//{skin}-{categoría}-{imagen}.png")
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
        
    
    def mover_personaje(event):
        global personaje_posicion
        global vidas
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
    """def Bomba(row, column):
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
        time.sleep(3)
        mostrar_laberinto(0,0)""" 

        #desplegar_personaje() 
    
    """def esparcimiento_fuego(x, y, iterator, direction):
        global lista_explosiones
        if iterator < 3 and es_accesible_bomba(x, y):
            fireImage= Image.open(fr"Bomberman Images\Fuego{iterator}.png")
            fireImage = fireImage.resize((40, 40))
            fireImage = ImageTk.PhotoImage(fireImage)
            fire = tk.Label(ventana, image=fireImage, fg = "Green", bg="Green")
            fire.image = fireImage
            fire.grid(row=x, column=y)
            lista_explosiones +=[[x,y]]
            laberinto[x][y] = " "
            print(lista_explosiones)
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
                esparcimiento_fuego(x+1,y, iterator+1, "down")"""
    def colocarBomba():
        global personaje_posicion
        global bomba_posicion
        global bomba
        cargarImagen("bomba0",personaje_posicion[0],personaje_posicion[1])
        bomba_posicion = [personaje_posicion[0],personaje_posicion[1]]
        
        hilo_bomba_animación = threading.Thread(target=esparcimiento_fuego, args=(bomba_posicion[0],bomba_posicion[1] ))
        hilo_bomba_animación.start()
        bomba_posicion =[]

    def esparcimiento_fuego(row, column):
        global lista_explosiones
        time.sleep(2)
        cargarImagen("Fuego0", row, column)
        lista_explosiones+=[[row, column]]
        accesible_bomba(row+1,column)
        accesible_bomba(row-1, column)
        accesible_bomba(row, column+1)
        accesible_bomba(row, column-1)
        colisiones_bomba()
        time.sleep(2)
        mostrar_laberinto(0,0) 
    def accesible_bomba(row, column):
        global lista_explosiones, llave_encontrada, posicion_llave 
        if laberinto[row][column] != "X":
            cargarImagen("Fuego0", row, column)
            lista_explosiones+=[[row, column]]
            laberinto[row][column] = " "
            find_key(row,column)     
    ################################################
    #Enemigos
    def desplegar_enemigos(Imagen,row, column,enemytype):
        global enemigo1, enemigo2,enemigoImagen1,enemigoImagen2, enemy1, enemy2
        
        if enemytype == 1 and enemy1:
            enemigoImagen1 = Image.open(f"Bomberman Images//{Imagen}.png")
            enemigoImagen1 = enemigoImagen1.resize((40, 40))
            enemigoImagen1 = ImageTk.PhotoImage(enemigoImagen1)
            enemigo1 = tk.Label(ventana, image=enemigoImagen1, fg = "#408404", bg="#408404")
            enemigo1.grid(row=row, column=column)
        elif enemytype == 2:
            enemigoImagen2 = Image.open(f"Bomberman Images//{Imagen}.png")
            enemigoImagen2 = enemigoImagen2.resize((40, 40))
            enemigoImagen2 = ImageTk.PhotoImage(enemigoImagen2)
            enemigo2 = tk.Label(ventana, image=enemigoImagen2, fg = "#408404", bg="#408404")
            enemigo2.grid(row=row, column=column)
    def Enemigos():
        global enemigo
        global posicionEnemigo1, posicionEnemigo2
        hilo1 = threading.Thread(target=desplegar_enemigos, args=("Enemigo1", posicionEnemigo1[0],posicionEnemigo1[1],1))
        hilo2 = threading.Thread(target=desplegar_enemigos, args=("Enemigo2", posicionEnemigo2[0],posicionEnemigo2[1],2))
        hilo1.start()
        hilo2.start()
    
    def MovimientoLaberinto(row, column,enemytype, direction):
        global posicionEnemigo1, posicionEnemigo2, enemigo1, enemigo2
        global personaje_posicion

        colisiones_personaje(personaje_posicion[0],personaje_posicion[1], row,column)

        if direction == "Up"and enemytype==1:
            if es_accesible_personaje(row+1, column):
                posicionEnemigo1 = [row+1, column]
                enemigo1.grid(row = row+1, column=column)
                ventana.update()
                time.sleep(0.5)
                MovimientoLaberinto(row+1,column, enemytype, "Up")
                print(posicionEnemigo1)
            else:
                MovimientoLaberinto(posicionEnemigo1[0], posicionEnemigo1[1], 1,"Down")
        elif direction == "Down":
            if es_accesible_personaje(row-1, column):
                posicionEnemigo1 = [row-1, column]
                enemigo1.grid(row = row-1, column=column)
                ventana.update()
                time.sleep(0.5)
                MovimientoLaberinto(row-1,column, enemytype, "Down")
                print(posicionEnemigo1)
            else:
                MovimientoLaberinto(posicionEnemigo1[0], posicionEnemigo1[1], 1,"Up")
        if direction == "Right" and enemytype==2:
            if es_accesible_personaje(row, column+1):
                posicionEnemigo2 = [row, column+1]
                enemigo2.grid(row = row, column=column+1)
                ventana.update()
                time.sleep(0.5)
                MovimientoLaberinto(row,column+1, enemytype,"Right")
                print(posicionEnemigo2)
            else:
                MovimientoLaberinto(posicionEnemigo2[0], posicionEnemigo2[1], 2,"Left")
        elif direction == "Left":
            if es_accesible_personaje(row, column-1):
                posicionEnemigo2 = [row, column-1]
                enemigo2.grid(row = row, column=column-1)
                ventana.update()
                time.sleep(0.5)
                MovimientoLaberinto(row,column-1, enemytype,"Left")
                print(posicionEnemigo2)
            else:
                MovimientoLaberinto(posicionEnemigo2[0], posicionEnemigo2[1], 2,"Right")
        
    def AnimacionEnemigos():
        global posicionEnemigo1,posicionEnemigo2

        enemy1 = threading.Thread(target=MovimientoLaberinto, args=(posicionEnemigo1[0], posicionEnemigo1[1], 1, "Up"))
        enemy2 = threading.Thread(target=MovimientoLaberinto, args=(posicionEnemigo2[0], posicionEnemigo2[1], 2, "Right"))
        enemy1.start()
        enemy2.start()

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
        global posiciones_destructibles, vidas, laberinto_cargado, puntuacion
        global posicion_puerta
        if x == len(laberinto)-1 and y == len(laberinto[0])-1:
            print(laberinto)
            desplegar_personaje()
            Enemigos()
            funcionvidas(vidas)
            incrementa_puntos(puntuacion)

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
            #ventana.update()
        elif laberinto[x][y] == " " or [x,y] in lista_explosiones:
            cargarImagen("pasto", x, y)
        ventana.update()    
        if y < len(laberinto[0]) - 1: #Eval+ua si la posición de la matriz [x][y] en y no ha llegado al límite
            mostrar_laberinto(x, y + 1)
        elif x < len(laberinto) - 1:#Eval+ua si la posición de la matriz [x][y] en x no ha llegado al límite
            mostrar_laberinto(x + 1, 0)
        
        
        
    
   
    #Código basado en ChatGPT
    def es_accesible_personaje(fila, columna):
        global posicion_puerta, bomba_posicion
        global llave_encontrada
        if fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]) or [fila, columna]==bomba_posicion:
            return False
        elif fila == posicion_puerta[0] and columna == posicion_puerta[1] and llave_encontrada:
            print("Pasaste Nivel 1")
        return laberinto[fila][columna] in [" ", "E", "Z"]  # Retorna True solo si el valor accedido en la matriz sea == " "
    #Código basado en ChatGPT
    """def es_accesible_bomba(fila, columna):
        global posicion_llave
        global llave_encontrada
        if fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]):
            return False
        elif fila == posicion_llave[0] and columna == posicion_llave[1]:
            laberinto[fila][columna] = "E"
            llave_encontrada = True
        return laberinto[fila][columna] in [" ", "Z", "Y", "E"]"""# Retorna True solo si el valor accedido en la matriz sea == " "
    #Crear posición random de la llave
    mostrar_laberinto(0,0)
    posicion_llave = posicion_random_con_espacios()
    laberinto[posicion_llave[0]][posicion_llave[1]] = "Z"
    
   
        
    AnimacionEnemigos() 
     # Definir la duración de la cuenta regresiva en segundos
    #ventana.update()
    # Llamar a la función countdown con la duración especificada
    cuenta_regresiva = threading.Thread(target=countdown, args=(tiempo,))
    cuenta_regresiva.start()
    
    ventana.bind("<KeyPress>", mover_personaje)
    ventana.mainloop()


