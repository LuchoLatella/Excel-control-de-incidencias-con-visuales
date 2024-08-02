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
                self.text_area.insert(tk.END, self.data.head().to_string() + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    
    def limpiar_archivo(self):
        if self.data is not None:
            try:
                # Eliminar columnas I, J, P, Q, R, S
                cols_to_drop = [8, 9, 15, 16, 17, 18]
                self.data.drop(self.data.columns[cols_to_drop], axis=1, inplace=True)

                # Reordenar columnas (mover E a la posición D)
                cols = list(self.data.columns)
                moved_col = cols.pop(4)
                cols.insert(3, moved_col)
                self.data = self.data[cols]

                # Renombrar columnas (si es necesario)
                self.data.columns = [f'Column{i}' for i in range(self.data.shape[1])]

                messagebox.showinfo("Información", "Archivo limpiado.")
                self.text_area.insert(tk.END, "Archivo limpiado.\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo limpiar el archivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def generar_tabla_dinamica(self):
        if self.data is not None:
            try:
                # Creación de una tabla dinámica similar a la definida en VBA
                self.pivot_table = self.data.pivot_table(
                    index=['Column1', 'Column2', 'Column3'],  # Filas (ajustar según sea necesario)
                    values='Column4',  # Valores a agregar (ajustar según sea necesario)
                    aggfunc={'Column4': ['sum', 'count']}  # Funciones de agregación
                )
                
                # Renombrar columnas en la tabla dinámica
                self.pivot_table.columns = ['Q unidades / $', 'Q casos']
                self.pivot_table.reset_index(inplace=True)
                
                self.text_area.insert(tk.END, "Tabla dinámica generada:\n")
                self.text_area.insert(tk.END, self.pivot_table.to_string() + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo generar la tabla dinámica: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def cruce_ministerio_salud(self):
        if self.data is not None:
            try:
                # Implementar la lógica específica para el cruce de datos
                filtrados = self.data[self.data['ColumnX'] == 'Salud']  # Ajustar según la columna y el valor correspondiente
                self.text_area.insert(tk.END, "Cruce Ministerio de Salud:\n")
                self.text_area.insert(tk.END, filtrados.to_string() + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo realizar el cruce de datos: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
    
    def cruce_adm_general(self):
        if self.data is not None:
            try:
                # Implementar la lógica específica para el cruce de datos
                filtrados = self.data[self.data['ColumnY'] == 'Administración']  # Ajustar según la columna y el valor correspondiente
                self.text_area.insert(tk.END, "Cruce Administración General:\n")
                self.text_area.insert(tk.END, filtrados.to_string() + "\n")
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