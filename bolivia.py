# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#--------------------
# ventana principal
#--------------------

# se  declara una variable llamada ventana_principal y adquiere las caracteristicas de un objeto TK()
ventana_principal=Tk()

# titulo de la ventana
ventana_principal.title("BOLIVIA")

# establecer tamaño ala ventana
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="burlywood3")

#-----------------
#frame color1
#-----------------

frame_color1 =Frame(ventana_principal)
frame_color1.config(bg="red", width=780, height=180)
frame_color1.place(x=10,y=10)

#-----------------
#frame color3
#-----------------
frame_color3=Frame(ventana_principal)
frame_color3.config(bg="green", width=780, height=160)
frame_color3.place(x=10,y=330)

#-----------------
#frame color2
#-----------------
frame_color2=Frame(ventana_principal)
frame_color2.config(bg="yellow", width=780, height=160)
frame_color2.place(x=10,y=170)

# se ejecuta el metodo mainloop() dela clase TK() a travez de la instancia ventana_principal. este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton escribir, etc). cada accion del usuario se conoce como un evento. el metodo mainloop() es un bucle infinito
ventana_principal.mainloop()