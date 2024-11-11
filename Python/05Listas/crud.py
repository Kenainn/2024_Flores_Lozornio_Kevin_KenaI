import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de alumnos
alumnos = []

# 
def registrar_alumno():
    '''
    Función para registrar un nuevo alumno
    
    '''
    boleta = simpledialog.askstring("Registro", "Ingrese la boleta del alumno:")
    nombre = simpledialog.askstring("Registro", "Ingrese el nombre del alumno:")
    app = simpledialog.askstring("Registro", "Ingrese el apellido paterno del alumno:")
    apm = simpledialog.askstring("Registro", "Ingrese el apellido materno del alumno:")
    fecnac = simpledialog.askstring("Registro", "Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA):")
    
    # Solicitamos calificaciones para 3 parciales
    calificaciones = []
    for i in range(3):
        calificacion = simpledialog.askfloat("Registro", f"Ingrese la calificación del parcial {i + 1}:")
        calificaciones.append(calificacion)

    # Crear el diccionario del alumno
    alumno = {
        "boleta": boleta,
        "nombre": nombre,
        "apellido_paterno": app,
        "apellido_materno": apm,
        "fecha_nacimiento": fecnac,
        "calificaciones": calificaciones
    }
    alumnos.append(alumno)
    messagebox.showinfo("Éxito", "El alumno se registró exitosamente")

# Función para consultar los datos del arreglo de alumnos
def consultar_alumnos():
    if not alumnos:
        messagebox.showinfo("Sin registros", "No hay registros de alumnos.")
    else:
        lista_alumnos = "\n".join([f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']}, "
                                  f"Apellido Paterno: {alumno['apellido_paterno']}, "
                                  f"Apellido Materno: {alumno['apellido_materno']}, "
                                  f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}, "
                                  f"Calificaciones: {alumno['calificaciones']}"
                                  for alumno in alumnos])
        messagebox.showinfo("Lista de Alumnos", lista_alumnos)

# Función para buscar y editar la boleta
def editar_alumno():
    boleta = simpledialog.askstring("Entrada", "Ingrese la boleta del alumno que desea editar: ")
    for alumno in alumnos:
        if alumno['boleta'] == boleta:
            nuevo_nombre = simpledialog.askstring("Entrada", "Ingresa el nuevo nombre o presiona Enter para mantener el actual: ")
            if nuevo_nombre:
                alumno['nombre'] = nuevo_nombre

            nuevo_app = simpledialog.askstring("Entrada", "Ingresa el nuevo apellido paterno o presiona Enter para mantener el actual: ")
            if nuevo_app:
                alumno['apellido_paterno'] = nuevo_app

            nuevo_apm = simpledialog.askstring("Entrada", "Ingresa el nuevo apellido materno o presiona Enter para mantener el actual: ")
            if nuevo_apm:
                alumno['apellido_materno'] = nuevo_apm

            nueva_fecnac = simpledialog.askstring("Entrada", "Ingresa la nueva fecha de nacimiento o presiona Enter para mantener la actual: ")
            if nueva_fecnac:
                alumno['fecha_nacimiento'] = nueva_fecnac

            # Editamos las calificaciones
            for i in range(3):
                nueva_calificacion = simpledialog.askfloat("Entrada", f"Ingrese la nueva calificación del parcial {i + 1} o presiona Enter para mantener la actual: ")
                if nueva_calificacion is not None:
                    alumno['calificaciones'][i] = nueva_calificacion

            messagebox.showinfo("Actualización", "Los datos del alumno se han actualizado.")
            return

    messagebox.showinfo("No encontrado", "No se encontró un alumno con esa boleta.")

# Función para eliminar un alumno
def eliminar_alumno():
    boleta = simpledialog.askstring("Entrada", "Ingrese la boleta del alumno que desea eliminar: ")
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno['boleta'] != boleta]
    messagebox.showinfo("Eliminación", "El alumno ha sido eliminado.")

# Función principal con el menú
def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal, ya que solo usamos diálogos

    while True:
        # Menú de opciones
        opcion = simpledialog.askstring("Menú de Gestión",
            "1. Registrar alumno\n"
            "2. Consultar alumnos\n"
            "3. Editar alumno\n"
            "4. Eliminar alumno\n"
            "5. Salir\n"
            "Selecciona una opción:")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            consultar_alumnos()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            messagebox.showinfo("Salida", "¡Hasta pronto!")
            break
        else:
            messagebox.showinfo("Error", "Opción no válida")

    root.quit()

# Ejecutar el programa
if __name__ == "__main__":
    main()
