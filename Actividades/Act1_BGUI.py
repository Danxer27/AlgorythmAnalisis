import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time
#Daniel Joel Corona Espinoza

class Busquedas:
    cantidad = 0
    datos = []
    generated = False
    elemento = 0
    
    tamano_lineal = []
    tiempos_lineal = []
    tamano_binaria = []
    tiempos_binaria = []
    
    
    def set_cantidad(self):
        valor = entrada_datos.get()
            
        try:
            self.cantidad = int(valor)
            self.generar_datos()
            
        except ValueError:
            print("Entrada invalida")
            status_datos.config(text="Error detectando la entrada.", bg="red")
            return
            
    def set_elemento(self, tipo):
        valor = entrada_busqueda.get()
        if not self.generated:
            status_busqueda.config(text="Datos aun no generados.", bg="red")
        else:
            try:
                self.elemento = int(valor)
                if tipo == 1:
                    self.busqueda_lineal()
                else:
                    self.busqueda_binaria()
            except ValueError:
                print("Entrada invalida")
                status_busqueda.config(text="Error detectando la entrada.", bg="red")
                return

    def generar_datos(self):
        self.datos = np.random.default_rng().integers(low=0, high=self.cantidad, size=self.cantidad)
        self.datos.sort()
        print(self.datos)
        if len(self.datos) == 0:
            status_datos.config(text="Error generando datos.", bg="red")
        else:
            status_datos.config(text="DATOS GENERADOS CORRECTAMENTE.",  bg="LawnGreen")
            self.generated = True
            #recuadro de numeros generados
            tnums.config(state='normal', bg="white")
            tnums.delete('1.0', tk.END)  
            tnums.insert('1.0', str(self.datos))
            tnums.config(state='disabled') 
            
    def busqueda_lineal(self):
        inicio = time.perf_counter()
        encontrado = False
        for pos, ele in enumerate(self.datos):
            if self.elemento == ele and encontrado == False:
                index = pos
                encontrado = True
          
        final = time.perf_counter()  
        tiempo = final-inicio
        self.tamano_lineal.append(len(self.datos))
        self.tiempos_lineal.append(tiempo)
        
        self.show_encontrado(index, encontrado, tiempo)
            
    
    def busqueda_binaria(self):
        inicio = time.perf_counter()
        encontrado = False
        index = -1

        bq = self.elemento
        size = len(self.datos)
        min = 0
        max = size - 1

        while max >= min:
            mid = (min + max) // 2  
            if self.datos[mid] == bq:
                encontrado = True
                index = mid
                break
            elif bq > self.datos[mid]:
                min = mid + 1
            else:
                max = mid - 1

        final = time.perf_counter()
        tiempo = final - inicio
        self.tamano_binaria.append(len(self.datos))
        self.tiempos_binaria.append(tiempo)

        self.show_encontrado(index, encontrado, tiempo)
        
    def show_encontrado(self, index, found, time):
        if found:
            status_busqueda.config(text=f"Encontrado en indice {index} en un tiempo de: {time} segundos", background="LawnGreen")
        else:
            status_busqueda.config(text="Elemento no encontrado", background="red")    
        
    def mostrar_grafica_lineal(self):
        ventana = tk.Toplevel(root)
        ventana.title("Gráfica Búsqueda Lineal")

        fig, ax = plt.subplots()
        ax.plot(self.tamano_lineal, self.tiempos_lineal, marker="o", color="blue", label="Tiempo vs Nº de datos")
        ax.set_title("Tiempo y tamanio (Lineal)")
        ax.set_xlabel("Numero de datos")
        ax.set_ylabel("Tiempo (segundos)")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        
    def mostrar_grafica_binaria(self):
        ventana = tk.Toplevel(root)
        ventana.title("Gráfica Búsqueda Binaria")

        fig, ax = plt.subplots()
        ax.plot(self.tamano_binaria, self.tiempos_binaria, marker="o", color="green", label="Tiempo vs Nº de datos")
        ax.set_title("Tiempo y tamanio (Binaria)")
        ax.set_xlabel("Numero de datos")
        ax.set_ylabel("Tiempo (segundos)")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()


search = Busquedas()




#gui
root = tk.Tk()
root.title("Busquedas")
root.geometry("520x520")
root.configure(bg="DarkSlateGrey")

#generacion de datos
label_datos = tk.Label(root, text="Ingresa la cantidad de datos:", bg="DarkSlateGray3")
label_datos.pack(pady=5)

entrada_datos = tk.Entry(root)
entrada_datos.pack(pady=5)

btn_generar_datos = tk.Button(root, text="Generar Datos", command=search.set_cantidad)
btn_generar_datos.pack(pady=5)

tnums = tk.Text(root, state='disabled', width=40, height=10, wrap=tk.WORD, bg="DarkSlateGrey")
tnums.pack(padx=15)


status_datos = tk.Label(root, text="", background="DarkSlateGrey")
status_datos.pack(pady=5)


#busqueda
label_buscar = tk.Label(root, text="Ingresa el valor a buscar:", bg="DarkSlateGray3")
label_buscar.pack(pady=5)

entrada_busqueda = tk.Entry(root)
entrada_busqueda.pack(pady=5)

btn_buscar_elemento_lineal = tk.Button(root, text="Buscar Elemento con Lineal", command=lambda: search.set_elemento(1))
btn_buscar_elemento_lineal.pack(pady=5)

btn_buscar_elemento_binaria = tk.Button(root, text="Buscar Elemento con Binaria", command=lambda: search.set_elemento(2))
btn_buscar_elemento_binaria.pack(pady=5, padx=10)

status_busqueda = tk.Label(root, text="", background="DarkSlateGrey")
status_busqueda.pack(pady=5)

#mostrar la grafica
btn_grafica = tk.Button(root, text="Mostrar gráfica de blineal", command=search.mostrar_grafica_lineal)
btn_grafica.pack(pady=5)
btn_grafica = tk.Button(root, text="Mostrar gráfica de Binaria", command=search.mostrar_grafica_binaria)
btn_grafica.pack(pady=5)

root.mainloop()