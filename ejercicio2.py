# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#--------------------
# ventana principal
#--------------------

# se  declara una variable llamada ventana_principal y adquiere las caracteristicas de un objeto TK()
ventana_principal=Tk()

# titulo de la ventana
ventana_principal.title("BRAYAN")

# establecer tamaño ala ventana
ventana_principal.geometry("800x500")

# icono de la ventana principal


# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="burlywood3")

#-----------------
#frame entrada
#-----------------

frame_entrada =Frame(ventana_principal)
frame_entrada.config(bg="yellow", width=780, height=240)
frame_entrada.place(x=10,y=10)

#-----------------
#frame operaciones
#-----------------
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="red", width=780, height=120)
frame_operaciones.place(x=10,y=370)

#-----------------
#frame resultados
#-----------------
frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="blue", width=780, height=120)
frame_resultados.place(x=10,y=250)

# se ejecuta el metodo mainloop() dela clase TK() a travez de la instancia ventana_principal. este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton escribir, etc). cada accion del usuario se conoce como un evento. el metodo mainloop() es un bucle infinito
ventana_principal.mainloop()