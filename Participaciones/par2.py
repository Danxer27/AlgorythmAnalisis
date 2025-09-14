import math as m
import random as rm
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#Alumno: Daniel Joel Corona Espinoza

root = tk.Tk()
root.title("Par mas cercano")
root.geometry("850x350")

pts = []
dist_puntos = []
#NUM_NODOS = int(input("Numero de nodos: "))
NUM_NODOS = 0

def generar_pares(N):
    for i in range(N):
        par = (rm.randint(1,30), rm.randint(1,30))
        pts.append(list(par))

def dist(p1, p2):
    dis_res = m.sqrt(((p2[0]-p1[0])**2) + ((p2[1] - p1[1])**2))
    return dis_res


def calcular_distancias(pts):
    min = 1000
    for j in range(len(pts)):
        for i in range(len(pts)):
            if pts[j] != pts[i]:
                dist_puntos.append(dist(pts[j], pts[i]))
                temp_dist = dist(pts[j], pts[i])
                if temp_dist < min:
                    min = temp_dist
                    pmi = i
                    pmj = j
                    
                

        pts[j].append(list(dist_puntos))
        dist_puntos.clear()
    label_respuesta.config(text=f"La distancia mas corta es {min} entre el punto P{pmi} ({pts[pmi][0], pts[pmi][1]}) y  P{pmj} ({pts[pmj][0], pts[pmj][1]})")
    
def procesar():
    temp_num = entrada_num_nodos.get()
    try:
        temp_num = int(temp_num)
    except:
        raise ValueError("numero no valido")
    
    if temp_num < 0:
        raise ValueError("Numero no valido")
    
    generar_pares(temp_num)
    calcular_distancias(pts)

    print("Puntos:")
    for i in range(len(pts)):
        print(f"PNT: {pts[i], pts[i]}")
        Puntos.insert('1.0', str(f"PNT: {pts[i][0], pts[i][1]} \n"))
        
    grafica()
    
def procesar_manual():
    calcular_distancias(pts)
    
    print("Puntos:")
    for i in range(len(pts)):
        print(f"PNT: {pts[i], pts[i]}")
        Puntos.insert('1.0', str(f"PNT: {pts[i][0], pts[i][1]} \n"))
        
    grafica()
        
def grafica():
    x = [p[0] for p in pts]
    y = [p[1] for p in pts]

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(x, y, color="blue", marker="o")
    ax.set_title("Gráfica de Puntos")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)      

entradas_x = []
entradas_y = []

def capturar_datos():
    global pts
    pts.clear() 

    for ex, ey in zip(entradas_x, entradas_y):
        val_x = ex.get().strip()
        val_y = ey.get().strip()

        if val_x != "" and val_y != "":
            try:
                x = float(val_x)
                y = float(val_y)
                pts.append([x, y])
            except ValueError:
                print(f"Entrada inválida: {val_x}, {val_y}")

    if len(pts) > 1:
        calcular_distancias(pts)
        grafica()

    print("Puntos capturados:", pts)


#GUI
# framde de captura de ndos
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

for i in range(5):
    lbl_x = tk.Label(frame_inputs, text=f"X{i+1}:")
    lbl_x.grid(row=i, column=0, padx=5, pady=2)
    entry_x = tk.Entry(frame_inputs, width=5)
    entry_x.grid(row=i, column=1, padx=5, pady=2)
    entradas_x.append(entry_x)
    lbl_y = tk.Label(frame_inputs, text=f"Y{i+1}:")
    lbl_y.grid(row=i, column=2, padx=5, pady=2)
    entry_y = tk.Entry(frame_inputs, width=5)
    entry_y.grid(row=i, column=3, padx=5, pady=2)
    entradas_y.append(entry_y)

    
tk.Button(root, text="Guardar Nodos", command=capturar_datos).pack(padx=5)

label_num_nodos = tk.Label(root, text="Numero de Nodos: ")
label_num_nodos.pack(pady=3)

entrada_num_nodos = tk.Entry(root)
entrada_num_nodos.pack(pady=2)

tk.Button(root, text="Generar Aleatoriamente", command=procesar).pack(padx=5)

label_respuesta = tk.Label(root, text="")
label_respuesta.pack(pady=3)

Puntos = tk.Text(root, width=80, height=15, wrap=tk.WORD)
Puntos.pack(padx=15)



root.mainloop()