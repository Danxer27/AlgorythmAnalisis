import tkinter as tk
from tkinter import ttk


def generar_datos():
    pass

#gui
root = tk.Tk()
root.title("Busquedas")
root.geometry("520x220")
root.configure(bg="DarkSlateGrey")

btn_datos1 = tk.Button(root, text="100", command=generar_datos)
btn_datos1.pack(pady=10)
btn_datos2 = tk.Button(root, text="1,000", command=generar_datos)
btn_datos2.pack(pady=10)
btn_datos3 = tk.Button(root, text="10,000", command=generar_datos)
btn_datos3.pack(pady=10)
btn_datos4 = tk.Button(root, text="100,000", command=generar_datos)
btn_datos4.pack(pady=10)




root.mainloop()