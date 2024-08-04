import pandas as pd
import tkinter as tk    
from tkinter import filedialog, messagebox

def cargar_archivo_csv(app):
    file_path = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    if file_path:
        try:
            app.data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
            app.text_area.insert(tk.END, "Archivo CSV cargado exitosamente.\n")
            app.text_area.insert(tk.END, app.data.head().to_string() + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo CSV: {str(e)}")

def cargar_archivo_excel(app):
    file_path = filedialog.askopenfilename(title="Selecciona un archivo Excel", filetypes=[("Archivos Excel", "*.xls *.xlsx")])
    if file_path:
        try:
            app.data = pd.read_excel(file_path)
            app.text_area.insert(tk.END, "Archivo Excel cargado exitosamente.\n")
            app.text_area.insert(tk.END, app.data.head().to_string() + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo Excel: {str(e)}")
