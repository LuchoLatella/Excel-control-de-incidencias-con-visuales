import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de incidencias - Excel / .csv")
        self.data = None  # Para almacenar los datos cargados
        self.file_path = None  # Para almacenar la ruta del archivo cargado

        # Importar las funciones necesarias de otros módulos
        from cargar_archivo import cargar_archivo_csv, cargar_archivo_excel
        from limpieza_datos import limpiar_archivo, generar_tabla_dinamica
        from cruce_datos import cruce_ministerio_salud, cruce_adm_general
        from descargar_archivo import descargar_archivo

        # Botones para cargar archivos CSV y Excel
        tk.Button(root, text="Cargar Archivo CSV", command=lambda: self.cargar_archivo('csv')).pack()
        tk.Button(root, text="Cargar Archivo Excel", command=lambda: self.cargar_archivo('excel')).pack()

        # Otros botones para funcionalidades
        tk.Button(root, text="Limpiar Archivo", command=lambda: limpiar_archivo(self)).pack()
        tk.Button(root, text="Generar Tabla Dinámica", command=lambda: generar_tabla_dinamica(self)).pack()
        tk.Button(root, text="Cruce x Casos Ministerio de Salud", command=lambda: cruce_ministerio_salud(self)).pack()
        tk.Button(root, text="Cruce x Adm General", command=lambda: cruce_adm_general(self)).pack()
        tk.Button(root, text="Descargar Archivo Terminado", command=lambda: descargar_archivo(self)).pack()

        # Botón para abrir en Excel
        self.abrir_en_excel_btn = tk.Button(root, text="Abrir en Excel", command=self.abrir_en_excel, state=tk.DISABLED)
        self.abrir_en_excel_btn.pack()

        # Área para mostrar datos
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(fill='both', expand=True)

    def cargar_archivo(self, tipo):
        filetypes = [("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xls;*.xlsx;*.xlsm")]
        file_path = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=filetypes)
        
        if file_path:
            try:
                if file_path.endswith('.csv') and tipo == 'csv':
                    self.data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
                    self.text_area.insert(tk.END, "Archivo CSV cargado exitosamente.\n")
                elif file_path.endswith(('.xls', '.xlsx', '.xlsm')) and tipo == 'excel':
                    self.data = pd.read_excel(file_path)
                    self.text_area.insert(tk.END, "Archivo Excel cargado exitosamente.\n")
                else:
                    messagebox.showerror("Error", "Tipo de archivo no compatible con la opción seleccionada.")
                    return

                self.text_area.insert(tk.END, self.data.head().to_string() + "\n")
                self.abrir_en_excel_btn.config(state=tk.NORMAL)
                self.file_path = file_path
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

    def abrir_en_excel(self):
        if self.file_path:
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(self.file_path)
                elif os.name == 'posix':  # macOS, Linux
                    subprocess.call(['open', self.file_path])
                else:
                    messagebox.showerror("Error", "No se puede abrir el archivo en Excel en este sistema operativo.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo en Excel: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
