from tkinter import messagebox

def limpiar_archivo(app):
    if app.data is not None:
        try:
            cols_to_drop = [8, 9, 15, 16, 17, 18]
            app.data.drop(app.data.columns[cols_to_drop], axis=1, inplace=True)

            cols = list(app.data.columns)
            moved_col = cols.pop(4)
            cols.insert(3, moved_col)
            app.data = app.data[cols]

            app.data.columns = [f'Column{i}' for i in range(app.data.shape[1])]

            messagebox.showinfo("Información", "Archivo limpiado.")
            app.text_area.insert(tk.END, "Archivo limpiado.\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo limpiar el archivo: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Cargue un archivo primero.")

def generar_tabla_dinamica(app):
    if app.data is not None:
        try:
            app.pivot_table = app.data.pivot_table(
                index=['Column1', 'Column2', 'Column3'],
                values='Column4',
                aggfunc={'Column4': ['sum', 'count']}
            )
            app.pivot_table.columns = ['Q unidades / $', 'Q casos']
            app.pivot_table.reset_index(inplace=True)

            app.text_area.insert(tk.END, "Tabla dinámica generada:\n")
            app.text_area.insert(tk.END, app.pivot_table.to_string() + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar la tabla dinámica: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Cargue un archivo primero.")