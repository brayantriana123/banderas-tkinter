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
ventana_principal.geometry("300x200")

# icono de la ventana principal


# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana principal
ventana_principal.config(bg="burlywood3")

# agregamos un widget a la ventana principal
letrero= Label(text="\nsistemas el mejor!!\n\n" , bg="burlywood3")
letrero.pack()

# agregamos un widget a la ventana principal
letrero2= Label(text="\n\nBRAYAN\n\n" , bg="burlywood3")
letrero2.pack()


# agregamos un widget a la ventana principal
letrero3= Label(text="\n\ncolegio san jose de guanenta\n\n" , bg="burlywood3")
letrero3.pack()

# se ejecuta el metodo mainloop() dela clase TK() a travez de la instancia ventana_principal. este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton escribir, etc). cada accion del usuario se conoce como un evento. el metodo mainloop() es un bucle infinito
ventana_principal.mainloop()