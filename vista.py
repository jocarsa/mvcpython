import tkinter as tk
from controlador import *


def muestraVentana(algo):
    ventana = tk.Tk()
    etiqueta = tk.Label(ventana,text=algo)
    etiqueta.pack(padx=50,pady=50)
    ventana.mainloop()

muestraVentana(dameDato())
