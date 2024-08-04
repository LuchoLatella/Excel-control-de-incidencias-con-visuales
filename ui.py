import tkinter as tk
from cargar_archivo import ArchivoHandler
from limpieza_datos import limpiar_archivo, generar_tabla_dinamica
from cruce_datos import cruce_ministerio_salud, cruce_adm_general
from descargar_archivo import descargar_archivo

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de incidencias - Excel / .csv")
        self.data = None  # Para almacenar los datos cargados
        self.file_path = None  # Para almacenar la ruta del archivo cargado
        self.archivo_handler = ArchivoHandler()

        # Botones para cargar archivos CSV y Excel
        tk.Button(root, text="Cargar Archivo CSV", command=lambda: self.archivo_handler.cargar_archivo(self, 'csv')).pack()
        tk.Button(root, text="Cargar Archivo Excel", command=lambda: self.archivo_handler.cargar_archivo(self, 'excel')).pack()

        # Otros botones para funcionalidades
        tk.Button(root, text="Limpiar Archivo", command=lambda: limpiar_archivo(self)).pack()
        tk.Button(root, text="Generar Tabla Dinámica", command=lambda: generar_tabla_dinamica(self)).pack()
        tk.Button(root, text="Cruce x Casos Ministerio de Salud", command=lambda: cruce_ministerio_salud(self)).pack()
        tk.Button(root, text="Cruce x Adm General", command=lambda: cruce_adm_general(self)).pack()
        tk.Button(root, text="Descargar Archivo Terminado", command=lambda: descargar_archivo(self)).pack()

        # Botón para abrir en Excel
        self.abrir_en_excel_btn = tk.Button(root, text="Abrir en Excel", command=self.archivo_handler.abrir_en_excel, state=tk.DISABLED)
        self.abrir_en_excel_btn.pack()

        # Área para mostrar datos
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(fill='both', expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

