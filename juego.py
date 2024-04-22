import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time
import threading
import random
import datetime
import time

def Personalizacion(root):
    def boton_presionado(numero, nombre):
        root2.destroy()
        Nivel(root,numero,3,10,180,nombre, 1)

    # Crear la ventana
    root2 = tk.Toplevel(root)
    root2.title("Personalización0")
    root2.config(bg="black")
    root2.resizable(False, False)  # Hacer que la ventana no sea redimensionable
    root2.attributes('-topmost', True)  # Hacer que la ventana esté siempre arriba
    # Cargar las imágenes
    imagen1 = PhotoImage(file=r".\Bomberman Images\0-2-1.png")
    imagen2 = PhotoImage(file=r".\Bomberman Images\1-2-1.png")
    imagen3 = PhotoImage(file=r".\Bomberman Images\2-2-1.png")
    imagen = Image.open(f"Bomberman Images//0-2-1.png")  
    imagen = imagen.resize((44, 44))
    imagen = ImageTk.PhotoImage(imagen)

    #Colocar entrada de texto
    label_nombre = tk.Label(root2, text="Ingresa el nombre del jugador:")
    label_nombre.grid(row=1, column=1)
    entrada_nombre = tk.Entry(root2,font=("Fixedsys", 20, "normal"))
    entrada_nombre.grid(row=2, column=1)

    # Crear los botones con las imágenes
    boton1 = tk.Button(root2, image=imagen1,command=lambda: boton_presionado(0, entrada_nombre.get()))
    boton2 = tk.Button(root2, image=imagen2,command=lambda: boton_presionado(1, entrada_nombre.get()))
    boton3 = tk.Button(root2, image=imagen3,command=lambda: boton_presionado(2, entrada_nombre.get() ))
    #Colocar Imágenes en los botones
    boton1.image = imagen1
    boton1.image = imagen2
    boton1.image = imagen3

    # Colocar los botones en la ventana
    boton1.grid(row=0, column=0, padx=10, pady=10)
    boton2.grid(row=0, column=1, padx=10, pady=10)
    boton3.grid(row=0, column=2, padx=10, pady=10)

    
    # Ejecutar el bucle principal de la aplicación
    root2.mainloop()




def Nivel(root, skin_code,lifes, bombs, duración, nombre, level):
    
     # Crear la ventana del juego
    ventana = tk.Toplevel(root)
    ventana.title("Laberinto")
    ventana.config(bg="Green")
    print(nombre)
    
    global vidas, llave_encontrada,bombas,puntuacion, enemy1, enemy2, tiempo, laberinto
    global fire, enemigo1, enemigo2,personaje
    global enemigoImagen1, enemigoImagen2,personaje_imagen,imagen_actual
    global posicionEnemigo1, posicionEnemigo2,posicion_puerta,posiciones_destructibles, posicion_llave, personaje_posicion,bomba_posicion
    global lista_explosiones
    global skin, finish, name
    #Inicializar variables globales del juego
    laberinto = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'C', 'X', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
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
    finish = False
    name = nombre
    #Funciones de jugador
    

    ################################################

    def EscribirArchivo(name, puntuacion, level):
        ruta=f"{level}.txt"
        archivo=open(ruta,"a")#a->append OJO
        archivo.write(f"{name}@{puntuacion}\n") # escribe el dato en el archivo
        archivo.close()

    #Código basado en ChatGPT    
    def countdown(duration):
        global finish, tiempo
        remaining_time = datetime.timedelta(seconds=duration)
        while remaining_time.total_seconds() > 0:
            if finish:
                break
            Time= tk.Label(ventana,text=remaining_time, bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"))
            Time.place(relx=0.0, rely=0.0)
            time.sleep(1)
            remaining_time -= datetime.timedelta(seconds=1)
            tiempo -=1
        if not finish:
            GameOver(root)
        

    def funcionvidas(vidas):
        if vidas <= 0:
            GameOver(root)
        else:
            Vida= tk.Label(ventana,text=str(vidas)+"X", relief="raised", bd=4, font=("Fixedsys", 17, "normal"))
            Vida.grid(row=1, column=0)
            ventana.update()
    
    def funcionbombas(bombas):
        if bombas <= 0:
            GameOver(root)
        else:
            Bomba= tk.Label(ventana,text=str(bombas)+"X", relief="raised", bd=4, font=("Fixedsys", 17, "normal"))
            Bomba.grid(row=1, column=2)
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

    #GameOver
    def YouWin(root):
        global puntuacion,vidas,bombas,tiempo, finish
        puntuacion+=tiempo+100*vidas+25*bombas
        ventana.destroy()
        def Continuar():
            gameOver.destroy()
            if level == 1:
                Nivel(root=root, skin_code=skin,lifes=2,bombs=10,duración=120, nombre=nombre, level=2)
            elif level == 2:
                Nivel(root=root, skin_code=skin,lifes=1,bombs=5,duración=90, nombre=nombre, level=3)
            else:
                pass
        gameOver = tk.Toplevel(root)
        gameOver.resizable(False, False)
        gameOver.title("Game Over")
        gameOver.config(bg="black")
        Title= tk.Label(gameOver,text=f"Congrats {nombre} you Win the level {level}", relief="raised", bd=4,borderwidth=0, highlightthickness=0,font=("Fixedsys", 32, "normal"),fg="green", bg="black")
        Title.grid(row=0, column=0)
        Score =tk.Label(gameOver,text=f"Your Score is {puntuacion}", borderwidth=0, highlightthickness=0,relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="green", bg="black")
        Score.grid(row=1, column=0) 
        EscribirArchivo(name, puntuacion, level)

        Continuar = tk.Button(gameOver, text="Continue", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Continuar)
        Continuar.grid(row=2, column=0)
    
    def GameOver(root):
        global finish
        finish = True
        ventana.destroy()
        def Retry():
            gameOver.destroy()
            if level == 1:
                Nivel(root=root, skin_code=skin,lifes=3,bombs=10,duración=180, nombre=nombre, level=1)
            elif level == 2:
                Nivel(root=root, skin_code=skin,lifes=2,bombs=7,duración=120, nombre=nombre, level=2)
            else:
                Nivel(root=root, skin_code=skin,lifes=1,bombs=5,duración=90, nombre=nombre, level=3)
        gameOver = tk.Toplevel(root)
        gameOver.resizable(False, False)
        gameOver.title("Game Over")
        gameOver.config(bg="black")
        Title= tk.Label(gameOver,text=f"You Lose", relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="green", bg="black")
        Title.grid(row=0, column=0)
        Title2= tk.Label(gameOver,text=f"Press the button to retry", relief="raised", bd=4, font=("Fixedsys", 32, "normal"),fg="green", bg="black")
        Title2.grid(row=1, column=0)
        Reiniciar = tk.Button(gameOver, text="Retry", bg="#110F34", fg="white", relief="raised", bd=4, font=("Fixedsys", 20, "normal"), command=Retry)
        Reiniciar.grid(row=2, column=0)

       
   ##################################################
   #Colisiones
    def colisiones_personaje(row, column, row2, column2):
        global vidas
        if row == row2 and column == column2:
                vidas -= 1
                funcionvidas(vidas)
                mostrar_laberinto(0,0)
    def colisiones_bomba():
        global lista_explosiones, personaje_posicion, vidas, posicionEnemigo1, posicionEnemigo2,enemy1, enemy2,puntuacion
        if personaje_posicion in lista_explosiones:
            vidas -= 1
            funcionvidas(vidas)
           # mostrar_laberinto(0,0)
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
        global bomba, bombas
        cargarImagen("bomba0",personaje_posicion[0],personaje_posicion[1])
        bomba_posicion = [personaje_posicion[0],personaje_posicion[1]]
        bombas -=1
        funcionbombas(bombas)
        hilo_bomba_animación = threading.Thread(target=esparcimiento_fuego, args=(bomba_posicion[0],bomba_posicion[1] ))
        hilo_bomba_animación.start()
        bomba_posicion = []

    def esparcimiento_fuego(row, column):
        global lista_explosiones
        time.sleep(2)
        cargarImagen("Fuego0", row, column)
        lista_explosiones+=[[row, column]]
        accesible_bomba(row+1,column)
        accesible_bomba(row-1, column)
        accesible_bomba(row, column+1)
        accesible_bomba(row, column-1)
        time.sleep(0.5)
        colisiones_bomba()
        lista_explosiones=[]
        mostrar_laberinto(0,0) 
    def accesible_bomba(row, column):
        global lista_explosiones, llave_encontrada, posicion_llave, personaje_posicion
        if laberinto[row][column] not in ["X","C", "B"]:
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
        global posiciones_destructibles, vidas, laberinto_cargado, puntuacion,bombas
        global posicion_puerta
        if x == len(laberinto)-1 and y == len(laberinto[0])-1:
            print(laberinto)
            desplegar_personaje()
            Enemigos()
            funcionvidas(vidas)
            funcionbombas(bombas)
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
            elif laberinto[x][y] == "B":
                posicion_puerta = [x,y]
                cargarImagen("bomba", x, y)
            elif laberinto[x][y] == "C":
                posicion_puerta = [x,y]
                cargarImagen("life", x, y)
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
            YouWin(root)
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


