import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Manipulación de Datos")
        
        # Botones para cada funcionalidad
        tk.Button(root, text="Cargar Archivo", command=self.cargar_archivo).pack()
        tk.Button(root, text="Limpiar Archivo", command=self.limpiar_archivo).pack()
        tk.Button(root, text="Generar Tabla Dinámica", command=self.generar_tabla_dinamica).pack()
        tk.Button(root, text="Cruce x Casos Ministerio de Salud", command=self.cruce_ministerio_salud).pack()
        tk.Button(root, text="Cruce x Adm General", command=self.cruce_adm_general).pack()
        tk.Button(root, text="Descargar Archivo Terminado", command=self.descargar_archivo).pack()
        
        # Área para mostrar datos
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(fill='both', expand=True)
        
        self.data = None  # Para almacenar los datos cargados
    
    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
                self.text_area.insert(tk.END, "Archivo cargado exitosamente.\n")
                self.text_area.insert(tk.END, self.data.head().to_string())
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    
    def limpiar_archivo(self):
        if self.data is not None:
            # Ejemplo de limpieza: eliminar duplicados y filas con valores nulos
            self.data.drop_duplicates(inplace=True)
            self.data.dropna(inplace=True)
            messagebox.showinfo("Información", "Archivo limpiado.")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def generar_tabla_dinamica(self):
        if self.data is not None:
            try:
                # Ejemplo: crear una tabla dinámica simple
                pivot_table = self.data.pivot_table(index='Columna1', columns='Columna2', values='Columna3', aggfunc='sum')
                self.text_area.insert(tk.END, pivot_table.to_string())
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo generar la tabla dinámica: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def cruce_ministerio_salud(self):
        if self.data is not None:
            try:
                # Implementar la lógica específica para el cruce de datos
                # Ejemplo ficticio: Filtrar datos según ciertos criterios
                filtrados = self.data[self.data['Categoría'] == 'Salud']
                self.text_area.insert(tk.END, filtrados.to_string())
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo realizar el cruce de datos: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def cruce_adm_general(self):
        if self.data is not None:
            try:
                # Implementar la lógica específica para el cruce de datos
                # Ejemplo ficticio: Filtrar datos según otros criterios
                filtrados = self.data[self.data['Departamento'] == 'Administración']
                self.text_area.insert(tk.END, filtrados.to_string())
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo realizar el cruce de datos: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def descargar_archivo(self):
        if self.data is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
            if file_path:
                try:
                    self.data.to_csv(file_path, index=False, encoding='ISO-8859-1', sep=';')
                    messagebox.showinfo("Información", f"Archivo guardado exitosamente en: {file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue y procese un archivo primero.")

# Crear la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()