from tkinter import filedialog, messagebox

def descargar_archivo(app):
    if app.data is not None:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV (Delimitado por comas)", "*.csv"),
                ("Excel Workbook", "*.xlsx"),
                ("Excel 97-2003 Workbook", "*.xls"),
                ("Excel con macros habilitados", "*.xlsm"),
            ]
        )
        if file_path:
            try:
                if file_path.endswith(".csv"):
                    app.data.to_csv(file_path, index=False, encoding='ISO-8859-1', sep=';')
                elif file_path.endswith(".xlsx"):
                    app.data.to_excel(file_path, index=False, engine='openpyxl')
                elif file_path.endswith(".xls"):
                    app.data.to_excel(file_path, index=False)
                elif file_path.endswith(".xlsm"):
                    app.data.to_excel(file_path, index=False, engine='openpyxl')

                messagebox.showinfo("Información", f"Archivo guardado exitosamente en: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Cargue y procese un archivo primero.")
