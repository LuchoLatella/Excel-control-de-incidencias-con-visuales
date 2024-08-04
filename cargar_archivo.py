import pandas as pd
import tkinter as tk    
from tkinter import filedialog, messagebox
import os
import subprocess

class App:
    def __init__(self, root):
        self.data = None
        self.text_area = tk.Text(root)
        self.text_area.pack()
        self.cargar_archivo_btn = tk.Button(root, text="Cargar Archivo", command=self.cargar_archivo)
        self.cargar_archivo_btn.pack()
        self.abrir_en_excel_btn = tk.Button(root, text="Abrir en Excel", command=self.abrir_en_excel, state=tk.DISABLED)
        self.abrir_en_excel_btn.pack()

    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo",
            filetypes=[("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xls;*.xlsx;*.xlsm")]
        )
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
                    self.text_area.insert(tk.END, "Archivo CSV cargado exitosamente.\n")
                elif file_path.endswith(('.xls', '.xlsx', '.xlsm')):
                    self.data = pd.read_excel(file_path)
                    self.text_area.insert(tk.END, "Archivo Excel cargado exitosamente.\n")
                self.text_area.insert(tk.END, self.data.head().to_string() + "\n")
                self.abrir_en_excel_btn.config(state=tk.NORMAL)
                self.file_path = file_path
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

    def abrir_en_excel(self):
        if hasattr(self, 'file_path'):
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(self.file_path)
                elif os.name == 'posix':  # macOS, Linux
                    subprocess.call(['open', self.file_path])
                else:
                    messagebox.showerror("Error", "No se puede abrir el archivo en Excel en este sistema operativo.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo en Excel: {str(e)}")
