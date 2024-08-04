import tkinter as tk
from tkinter import filedialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Manipulación de Datos")

        # Importar las funciones necesarias de otros módulos
        from cargar_archivo import cargar_archivo_csv, cargar_archivo_excel
        from limpieza_datos import limpiar_archivo, generar_tabla_dinamica
        from cruce_datos import cruce_ministerio_salud, cruce_adm_general
        from descargar_archivo import descargar_archivo

        # Botones para cargar archivos CSV y Excel
        tk.Button(root, text="Cargar Archivo CSV", command=lambda: cargar_archivo_csv(self)).pack()
        tk.Button(root, text="Cargar Archivo Excel", command=lambda: cargar_archivo_excel(self)).pack()

        # Otros botones para funcionalidades
        tk.Button(root, text="Limpiar Archivo", command=lambda: limpiar_archivo(self)).pack()
        tk.Button(root, text="Generar Tabla Dinámica", command=lambda: generar_tabla_dinamica(self)).pack()
        tk.Button(root, text="Cruce x Casos Ministerio de Salud", command=lambda: cruce_ministerio_salud(self)).pack()
        tk.Button(root, text="Cruce x Adm General", command=lambda: cruce_adm_general(self)).pack()
        tk.Button(root, text="Descargar Archivo Terminado", command=lambda: descargar_archivo(self)).pack()

        # Área para mostrar datos
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(fill='both', expand=True)

        self.data = None  # Para almacenar los datos cargados
