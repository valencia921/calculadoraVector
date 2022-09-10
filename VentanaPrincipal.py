'''
Autores : Karen Manuela Lara Grandas - Diego Mauricio Valencia Hernandez
'''

import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

import numpy as np
from tkinter import *

root = Tk()
root.title("Calculadora Vectores")
root.geometry("500x300")

#--------------------Metodos---------------------------
'''
Metodo que permite visulizar el proceso que se realiza en el producto punto
'''
def mostrarProcedimiento(a,b):
    resultado = ""
    for i in range(0,len(a)):
        if(i<len(a)-1):
            resultado += str(a[i]) + "*" + str(b[i]) + " + "
        else:
            resultado += str(a[i]) + "*" + str(b[i])
    return resultado
'''
Metodo que permite hallar el area de un triangulo de coordenasdas x,y,z
utilizando laformula
'''
def hallarArea(cruz):
    resultado =0
    for i in range(0,len(cruz)):
        resultado += cruz[i]**2
    resultado = math.sqrt(resultado) / 2

    return resultado

'''
Metodo encargado de sumar dos vectores (dichos vectores deben ser del mismo tamaño)
'''
def sumarVectores():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            print (f' Resultado suma :{v1 + v2}')
            suma = f'Vector1:{v1} Vector2:{v2}'
            suma += f' \nResultado suma :{v1 + v2}'
            mb.showinfo("Resultado Suma",suma)
        else:
            mb.showerror("Tamaño ","Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo encargado de restar dos vectores (dichos vectores deben ser del mismo tamaño)
'''
def restarVectores():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            resta= f'Vector1:{v1} Vector2:{v2} \nResta:{v1 - v2} '
            mb.showinfo("Resultado Resta", resta)
        else:
             mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo encargado de realizar el producto punto de dos vectores con la misma longitud 
'''
def productoPunto():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            salida = np.dot(v1, v2)
            print("Un poco de la forma en como realizar el producto punto :")
            procedimiento = "Procedimiento:  " + mostrarProcedimiento(v1, v2) + "\n"
            producto= f'Vector 1: {v1} Vector 2: {v2} \nProducto Punto : {salida}'
            mb.showinfo("Resultado Producto Punto", procedimiento + producto)
        else:
            mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo que permite ilustrar el producto cruz con coordenadas x,y,z
'''
def productoCruz():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            if len(v1) == 3 and len(v2) == 3:
                cruz = np.cross(v1, v2)
                resultado = f'Vector 1: {v1} Vector 2: {v2} \nProducto Cruz : {cruz}'
                mb.showinfo("Resultado Producto Cruz", resultado)
            else:
                mb.showerror("Tamaño ", "Lo sentimos los vectores deben tener coordenadas x , y , z ")
        else:
            mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo que permite hallar el area de un triangulo sabiendo las coordenadas de sus vectores
'''
def areaTriangulo ():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            if len(v1) ==3 and len(v2)== 3 :
                cruz = np.cross(v1, v2)
                resultado = f'Area del triangulo segun el producto cruz: {round(hallarArea(cruz),2)}'
                mb.showinfo("Resultado Área del triangulo de los vectores", resultado)
            else:
                mb.showerror("Tamaño ", "Lo sentimos los vectores deben tener coordenadas x , y , z ")
        else:
            mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo que permite hallar e angulo que hay entre dos puntos (vectores).
Ademas, de conocer el coseno del angulo por medio de la formula de pitágoras. 
'''
def anguloEntrePuntos ():
    try:
        try:
            x = np.array(list(map(int, entrada1.get().split(","))))
            y = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(x) == len(y):
            Lx = np.sqrt(x.dot(x))
            Ly = np.sqrt(y.dot(y))
            #Equivalente al teorema de Pitágoras, encuentre la longitud de la barra
            cos_angle = x.dot(y) / (Lx * Ly)
            # Busque el valor de cos_sita y calcule a la inversa. Multiplique la longitud absoluta por el ángulo cos como la longitud del vector. Conocimiento de la escuela secundaria. .
            print(f'Coseno del angulo : {cos_angle}')
            angle = np.arccos(cos_angle)
            angle2 = round(angle * 360 / 2 / np.pi, 2)
            # Conviértete en un ángulo
            resultado= f'Sabias que:\nEl ángulo entre dos vectores es la capacidad del arco de la circunferencia que forman los segmentos de los vectores unidos por un punto.\n \n' \
                       f'Tus vectores son :\n' \
                       f'\nVector 1: {x}     Vector 2: {y} \n \n El arco de la circunferencia es : {angle2}°'
            mb.showinfo("Resultado Angulo", resultado)
        else:
            mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

'''
Metodo que permite conocer la distacia que se tiene entre dos puntos (vectores)
'''
def distanciaEntrevectores ():
    try:
        try:
            v1 = np.array(list(map(int, entrada1.get().split(","))))
            v2 = np.array(list(map(int, entrada2.get().split(","))))
        except UnboundLocalError:
            mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    except ValueError:
        mb.showerror("Upp! ", "Lo sentimos para ejecutar las funciones debe de poner los vectores. ")
    else:
        if len(v1) == len(v2):
            dist = round(np.linalg.norm(v1 - v2),2)
            resultado = f'Sabias que:\nLa distancia entre dos puntos en el espacio es el módulo del vector formado por dichos puntos.\n\n' \
                        f'Tus vectores son :\n'\
                        f'\nVector 1: {v1}   Vector 2: {v2} \n\nDistancia entre los vectores es : {dist}'
            mb.showinfo("Resultado distancia", resultado)
        else:
            mb.showerror("Tamaño ", "Lo sentimos el tamaño de los vectores deben ser iguales ")

def limpiarCampos ():
    entrada1.delete(0,tk.END)
    entrada2.delete(0,tk.END)


#Campos de texto de entrada
titulo = Label(root, text= "CALCULADORA DE VECTORES")
titulo.pack()

instrucciones = Label(root, text= "Los vectores deben ser ingresados de la siguiente manera:   n,m...,z   Ej: 1,2,3")
instrucciones.place(x=40,y=25)

label1 = Label(root , text= "Vector 1:")
label1.place( x=15, y=50,width=200 , height=25)
entrada1 = Entry (root, highlightbackground = "gray", highlightcolor= "#FF3A00", highlightthickness=1.4)
entrada1.place( x=40, y=80,width=200 , height=25)

label2 = Label(root , text= "Vector 2:")
label2.place( x=250, y=50,width=200 , height=25)
entrada2 = Entry (root, highlightbackground = "gray", highlightcolor= "#FF3A00", highlightthickness=1.4)
entrada2.place( x=250, y=80,width=200 , height=25)

#Botones de acciones
labelOperaciones= Label(root, text= "OPERACIONES").place(x=200, y=120)

botonSuma = Button (root, text = "SUMAR", command= sumarVectores).place(x=40, y=160, width=200)
botonResta = Button (root, text = "RESTAR", command= restarVectores).place(x=250, y=160, width=200)
botonPunto = Button (root, text = "PRODUCTO PUNTO", command= productoPunto).place(x=40, y=190, width=200)
botonCruz = Button (root, text = "PRODUCTO CRUZ", command= productoCruz).place(x=250, y=190, width=200)
botonAngulo = Button (root, text = "ANGULO", command=anguloEntrePuntos).place(x=40, y=220, width=200)
botonDistancia = Button (root, text = "DISTANCIA", command= distanciaEntrevectores).place(x=250, y=220, width=200)
botonArea = Button (root, text = "AREA DE UN TRIANGULO", command=areaTriangulo).place(x=40, y=250, width=200)
botonlimpiar = Button (root, text = "LIMPIAR CAMPOS", bg= "#84C9FF", command= limpiarCampos).place(x=250, y=250, width=200)

root.mainloop()

