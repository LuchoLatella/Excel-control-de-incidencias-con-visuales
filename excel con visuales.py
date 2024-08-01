import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

# Función para cargar y mostrar datos en el Treeview
def cargar_datos():
    file_path = filedialog.askopenfilename(title="Selecciona un archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        for i, row in df.iterrows():
            tree.insert("", "end", values=list(row))

# Crear la ventana principal
root = tk.Tk()
root.title("Visualizador de Excel")

# Crear un Treeview para mostrar los datos
tree = ttk.Treeview(root, columns=("A", "B", "C", "D"), show="headings")
tree.heading("A", text="Columna A")
tree.heading("B", text="Columna B")
tree.heading("C", text="Columna C")
tree.heading("D", text="Columna D")
tree.pack(fill="both", expand=True)

# Botón para cargar los datos
boton_cargar = tk.Button(root, text="Cargar Datos", command=cargar_datos)
boton_cargar.pack()

# Ejecutar la aplicación
root.mainloop()