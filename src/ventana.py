import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("aviso","¡Boton presionado!")
ventana = tk.Tk()
ventana.title("ventana simple")
label = tk.Label(ventana,text="¡Hola mundo!")
label.pack()
boton = tk.Button(ventana, text="Haz click aqui")
boton.pack()


ventana.mainloop()