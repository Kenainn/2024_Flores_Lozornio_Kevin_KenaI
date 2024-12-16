import time
from tkinter import Tk, Label, Button, Listbox, END, messagebox
from ordenamiento import burbuja, seleccion_sort, insercion, merge, quick_sort

# Función para ejecutar el ordenamiento
def ejecutar_ordenamiento():
    metodo = metodo_lista.curselection()
    if not metodo:
        messagebox.showwarning("Advertencia", "Seleccione un método de ordenamiento.")
        return

    seleccion = metodo[0]
    lista_original = [12, 66, 14, 31, 50, 32, 22, 23, 1, 17, 55, 30, 33, 40, 18, 44, 67, 77, 90, 15, 60, 20, 21, 10, 13, 11, 88, 19, 16]
    lista_a_ordenar = lista_original.copy()

    inicio = time.time()
    if seleccion == 0:
        lista_ordenada = burbuja(lista_a_ordenar)
    elif seleccion == 1:
        lista_ordenada = seleccion_sort(lista_a_ordenar)
    elif seleccion == 2:
        lista_ordenada = insercion(lista_a_ordenar)
    elif seleccion == 3:
        lista_ordenada = merge(lista_a_ordenar)
    elif seleccion == 4:
        lista_ordenada = quick_sort(lista_a_ordenar)
    fin = time.time()

    tiempo_total = fin - inicio

    # Mostrar resultados
    resultado_label.config(text=f"Lista Original:\n{lista_original}\n\nLista Ordenada:\n{lista_ordenada}")
    tiempo_label.config(text=f"Tiempo de Ordenamiento: {tiempo_total:.6f} segundos")

# Configuración de la interfaz
root = Tk()
root.title("Métodos de Ordenamiento")
root.geometry("600x600")

Label(root, text="Métodos de Ordenamiento", font=("Arial", 16)).pack(pady=10)

metodo_lista = Listbox(root, height=5, font=("Arial", 14))
metodo_lista.insert(END, "Burbuja")
metodo_lista.insert(END, "Selección")
metodo_lista.insert(END, "Inserción")
metodo_lista.insert(END, "Merge Sort")
metodo_lista.insert(END, "Quick Sort")
metodo_lista.pack(pady=10)

Button(root, text="Ordenar", command=ejecutar_ordenamiento, font=("Arial", 14), bg="blue", fg="white").pack(pady=10)

resultado_label = Label(root, text="Resultados aparecerán aquí.", font=("Arial", 12), justify="left")
resultado_label.pack(pady=10)

tiempo_label = Label(root, text="", font=("Arial", 12))
tiempo_label.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()
