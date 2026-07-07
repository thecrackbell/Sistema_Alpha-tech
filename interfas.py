import tkinter as tk
from tkinter import messagebox, ttk
import ttkbootstrap as tb  # <-- Cambiamos tkinter.ttk por esto
from ttkbootstrap.constants import *
from lista_reparaciones import ListaReparaciones

class AlphaTechApp:
    def __init__(self, root):
       self.root = root
       self.root.title("Alpha Tech v5.0 - Professional")
       self.root.geometry("600x600") # Un poco más grande para que quepa todo
        
        # 1. Crear el contenedor principal (Frame)
        # Esto agrupa todo y evita que los elementos queden flotando
       self.main_frame = tb.Frame(self.root, padding=20)
       self.main_frame.pack(fill=BOTH, expand=YES)

        # 2. Título dentro del Frame
       tb.Label(self.main_frame, text="Panel de Gestión", font=("Helvetica", 18, "bold")).pack(pady=10)

        # 3. Botones (ahora los ponemos dentro del main_frame, no de root)
       self.crear_boton("Registrar Orden", self.abrir_registro)
       self.crear_boton("Ver Todas las Órdenes", self.ver_ordenes)
       self.crear_boton("Cerrar y Guardar", self.cerrar_sistema)

        # 4. Tabla (también dentro del main_frame)
       self.configurar_tabla()
        
        # 5. Carga de datos
       self.sistema = ListaReparaciones()
       self.sistema.cargar_desde_json()
       self.refrescar_tabla()

    def crear_boton(self, texto, comando):
        # Nota: aquí también usamos 'self.main_frame' en lugar de 'self.root'
        tb.Button(self.main_frame, text=texto, command=comando, width=30, bootstyle="info").pack(pady=5)

    def configurar_tabla(self):
        # Definimos las columnas correctamente
        # Nota que ahora usamos self.main_frame como contenedor
        self.tree = tb.Treeview(self.main_frame, columns=("ID", "Cliente", "Dispositivo", "Estado"), show="headings", bootstyle="info")
        # ... el resto de tu configuración igual ...
        self.tree.pack(fill="both", expand=True) # Esto hace que se estire
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Dispositivo", text="Dispositivo")
        self.tree.heading("Estado", text="Estado")
        self.tree.column("ID", width=50)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

    def refrescar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        actual = self.sistema.cabeza
        while actual:
            self.tree.insert("", "end", values=(actual.obtener_id(), actual.obtener_cliente(), actual.obtener_dispositivo(), actual.estado))
            actual = actual.siguiente

    def abrir_registro(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Nueva Orden")
        campos = {}
        etiquetas = ["Cliente", "Dispositivo", "Falla", "Costo"]
        for i, campo in enumerate(etiquetas):
            tk.Label(top, text=f"{campo}:").grid(row=i, column=0, padx=10, pady=5)
            campos[campo] = tk.Entry(top)
            campos[campo].grid(row=i, column=1, padx=10, pady=5)
        
        def guardar_datos():
            try:
                p = float(campos["Costo"].get())
                self.sistema.registrar_equipo(campos["Cliente"].get(), campos["Dispositivo"].get(), campos["Falla"].get(), p)
                self.refrescar_tabla()
                messagebox.showinfo("Éxito", "Orden registrada")
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "El costo debe ser un número")
        
        tk.Button(top, text="Guardar Registro", command=guardar_datos).grid(row=4, columnspan=2, pady=10)

    def ver_ordenes(self):
        # Esta función ya no es necesaria si tienes la tabla en la ventana principal,
        # pero puedes dejarla o eliminarla.
        pass

    def cerrar_sistema(self):
        self.sistema.guardar_en_json()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlphaTechApp(root)
    root.mainloop()