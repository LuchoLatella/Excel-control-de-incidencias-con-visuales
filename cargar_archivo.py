import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

class ArchivoHandler:
    def __init__(self):
        self.data = None
        self.file_path = None

    def cargar_archivo(self, app, tipo):
        filetypes = [("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xls;*.xlsx;*.xlsm")]
        file_path = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=filetypes)
        
        if file_path:
            try:
                if file_path.endswith('.csv') and tipo == 'csv':
                    self.data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
                    app.text_area.insert(tk.END, "Archivo CSV cargado exitosamente.\n")
                elif file_path.endswith(('.xls', '.xlsx', '.xlsm')) and tipo == 'excel':
                    self.data = pd.read_excel(file_path)
                    app.text_area.insert(tk.END, "Archivo Excel cargado exitosamente.\n")
                else:
                    messagebox.showerror("Error", "Tipo de archivo no compatible con la opción seleccionada.")
                    return

                app.data = self.data
                app.file_path = self.file_path = file_path
                app.text_area.insert(tk.END, self.data.head().to_string() + "\n")
                app.abrir_en_excel_btn.config(state=tk.NORMAL)
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
