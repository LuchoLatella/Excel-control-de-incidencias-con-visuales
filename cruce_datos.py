from tkinter import messagebox

def cruce_ministerio_salud(app):
    if app.data is not None:
        try:
            filtrados = app.data[app.data['ColumnX'] == 'Salud']
            app.text_area.insert(tk.END, "Cruce Ministerio de Salud:\n")
            app.text_area.insert(tk.END, filtrados.to_string() + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo realizar el cruce de datos: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Cargue un archivo primero.")

def cruce_adm_general(app):
    if app.data is not None:
        try:
            filtrados = app.data[app.data['ColumnY'] == 'Administración']
            app.text_area.insert(tk.END, "Cruce Administración General:\n")
            app.text_area.insert(tk.END, filtrados.to_string() + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo realizar el cruce de datos: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Cargue un archivo primero.")
