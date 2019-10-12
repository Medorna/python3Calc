#Calculatronik v0.1b sin POO
#importo las librerias que voy a usar
from tkinter import *
import tkinter.messagebox


######################
#funcion que captura e imprime command en el Entry "pantalla"
######################

def numero(x):
        return lambda: pantalla.insert(END, x) #lo robe de internet!

#######################
#funcion para operacion matematica usando eval
#Si numero se puede evaluar lo hace, sino tira error.
#######################

def igual():
        try:
                numero = eval(pantalla.get())
        except:
                numero = "*ERROR*"
        pantalla.delete(0, END)
        pantalla.insert(0, numero)

def ayuda():
	tkinter.messagebox.showinfo ("Ayuda", "Hola soy una ayuda")

def borrar(event):
    pantalla.delete(0, END)

def logueo():
    root=Tk()
    Login(root)
    root.mainloop()

#############################
#creo la ventana TK en vez de usar de nombre "root" uso "ventana", mas facil
#de recordar :P
#############################

ventana = Tk()
ventana.title("Calculatronik v0.1b")
ventana.geometry("230x200")
ventana.config(bg="LightCyan2")
ventana.resizable(0,0)
ventana.bind('<Escape>', borrar)

#creo mi contenedor (frame)dentro de mi ventana
frame = Frame(ventana)

#formato del frame, columnas y filas(row), pad(margenes)
frame.grid(column=0, row=0, padx=(30,30), pady=(30,30))

#formato columas
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

#############################
#creo mi variable str para tomar el valor de la caja de texto
#la caja de texto "Entry" y  el grid
#############################

valor = ""
pantalla = Entry(frame, width=28, textvariable=valor)
pantalla.grid(column=1, row=1, columnspan=7)
pantalla.bind('<Escape>', borrar)

#############################
#1.Crear la barra de menu "bMenu"
#2.Crear menu
#3.Crear los comandos de los menus
#4.Agregar menu a la barra menu
#5.Indicar barra menu estara en la ventana
###############################

bMenu = Menu(ventana)

mArchivo = Menu(bMenu)
mEdicion = Menu(bMenu, tearoff=0)
mAyuda= Menu(bMenu)

mArchivo.add_command(label="Abrir")
mArchivo.add_command(label="Guardar")
mArchivo.add_command(label="Login", command=logueo)
mArchivo.add_command(label="Salir", command=ventana.quit)

mEdicion.add_command(label="copiar")
mEdicion.add_command(label="cortar")
mEdicion.add_command(label="pegar")

mAyuda.add_command(label="Ayuda", command=ayuda)

bMenu.add_cascade(label="Archivo",menu=mArchivo)
bMenu.add_cascade(label="Edicion",menu=mEdicion)
bMenu.add_cascade(label="Ayuda",menu=mAyuda)

ventana.config(menu=bMenu)

#Aca vienen todos los botones.

b7 = Button(frame, text="7", width=4, activebackground = "LightCyan3", command=numero(7))
b7.grid(column=1, row=2)

b8 = Button(frame, text="8", width=4, activebackground = "LightCyan3", command=numero(8))
b8.grid(column=2, row=2)

b9 = Button(frame, text="9", width=4, activebackground = "LightCyan3", command=numero(9))
b9.grid(column=3, row=2)

dividir = Button(frame, text="/", width=7, activebackground = "LightCyan3", command=numero("/"))
dividir.grid(column=4, row=2)

#tercera row
b4 = Button(frame, text="4", width=4, activebackground = "LightCyan3", command=numero(4))
b4.grid(column=1, row=3)

b5 = Button(frame, text="5", width=4, activebackground = "LightCyan3", command=numero(5))
b5.grid(column=2, row=3)

b6 = Button(frame, text="6", width=4, activebackground = "LightCyan3", command=numero(6))
b6.grid(column=3, row=3)

multiplicar = Button(frame, text="X", width=7, activebackground = "LightCyan3", command=numero("*"))
multiplicar.grid(column=4, row=3)

#cuarta row
b1 = Button(frame, text="1", width=4, activebackground = "LightCyan3", command=numero(1))
b1.grid(column=1, row=4)

b2 = Button(frame, text="2", width=4, activebackground = "LightCyan3", command=numero(2))
b2.grid(column=2, row=4)

b3 = Button(frame, text="3", width=4, activebackground = "LightCyan3", command=numero(3))
b3.grid(column=3, row=4)

resta = Button(frame, text="-", width=7, activebackground = "LightCyan3", command=numero("-"))
resta.grid(column=4, row=4)

#quinta row
b0 = Button(frame, text="0", width=4, activebackground = "LightCyan3", command=numero(0))
b0.grid(column=1, row=5)

decimal = Button(frame, text=".", width=4, activebackground = "LightCyan3", command=numero("."))
decimal.grid(column=2, row=5)

suma = Button(frame, text="+", width=4, activebackground = "LightCyan3", command=numero("+"))
suma.grid(column=3, row=5)

igual = Button(frame, text="=", width=7, activebackground = "LightCyan3", command=igual)
igual.grid(column=4, row=5)


ventana.mainloop()

