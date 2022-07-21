# se importa la librería tkinter con todas sus funciones
from tkinter import *
from turtle import width

# ------------------
# ventana_principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk() ventana_principal = Tk()
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("BANDERA DE BELGICA")

# establece tamaño a la ventana 
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la pantalla principal
ventana_principal.config (bg="burlywood3")

#-----------------
#frame color3
#-----------------
frame_color3 = Frame(ventana_principal)
frame_color3.config(bg="red", width=780, height=780)
frame_color3.place(x=5, y=10)

#-----------------
#frame color2
#-----------------
frame_color2 = Frame(ventana_principal)
frame_color2.config(bg="yellow", width=520, height=780)
frame_color2.place(x=6, y=10)

#-----------------
#frame color1
#-----------------
frame_color1 = Frame(ventana_principal)
frame_color1.config(bg="black", width=260, height=780)
frame_color1.place(x=6, y=10)

# se ejecuta el metodo mainloop de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()