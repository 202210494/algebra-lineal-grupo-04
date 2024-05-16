import tkinter as tk
from tkinter import messagebox
import numpy as np

class ProyeccionView:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Proyección Ortogonal y Rotaciones")

        self.frame_punto = tk.Frame(root)
        self.frame_punto.pack(pady=10)
        tk.Label(self.frame_punto, text="Punto a proyectar (x, y, z):").grid(row=0, columnspan=6)

        tk.Label(self.frame_punto, text="x:").grid(row=1, column=0)
        self.entry_px = tk.Entry(self.frame_punto)
        self.entry_px.grid(row=1, column=1)

        tk.Label(self.frame_punto, text="y:").grid(row=1, column=2)
        self.entry_py = tk.Entry(self.frame_punto)
        self.entry_py.grid(row=1, column=3)

        tk.Label(self.frame_punto, text="z:").grid(row=1, column=4)
        self.entry_pz = tk.Entry(self.frame_punto)
        self.entry_pz.grid(row=1, column=5)

        ############################## Ecucacion del plano ##############################
        # Todo: disminuir el tamaño de los entrys (padx=5, pady=3) (ir probando con valores)
        # sino mover el columnspan=3

        self.frame_plano = tk.Frame(root)
        self.frame_plano.pack(pady=10)
        tk.Label(self.frame_plano, text="Plano (ax + by + cz + d = 0):").grid(row=0, columnspan=5)

        self.entry_a = tk.Entry(self.frame_plano)
        self.entry_a.grid(row=1, column=0, padx=5) 
        tk.Label(self.frame_plano, text="x + ").grid(row=1, column=1)
        

        
        self.entry_b = tk.Entry(self.frame_plano)
        self.entry_b.grid(row=1, column=2, padx=2)
        tk.Label(self.frame_plano, text="y + ").grid(row=1, column=3)

        self.entry_c = tk.Entry(self.frame_plano)
        self.entry_c.grid(row=1, column=4)
        tk.Label(self.frame_plano, text="z + ").grid(row=1, column=5)
        
        self.entry_d = tk.Entry(self.frame_plano)
        self.entry_d.grid(row=1, column=6, padx=7)      

        tk.Label(self.frame_plano, text="= 0").grid(row=1, column=7)

        # TODO: leer ecucacion del plano en un solo entry

        self.frame_plano2 = tk.Frame(root)
        self.frame_plano2.pack(pady=10)
        tk.Label(self.frame_plano2, text="Ecuacion del Plano:").grid(row=0, columnspan=8)
        tk.Label(self.frame_plano2, text="(ax + by + cz + d = 0):").grid(row=1, column=0)
        self.entry_plano = tk.Entry(self.frame_plano2)
        self.entry_plano.grid(row=1, column=1)
    
        self.calc_button = tk.Button(root, text="Calcular y Graficar")
        self.calc_button.pack(pady=10)

        self.frame_rotaciones = tk.Frame(root)
        self.frame_rotaciones.pack(pady=10)
        tk.Label(self.frame_rotaciones, text="Rotaciones sexadecimal o radian?:").grid(row=0, columnspan=8) # columnspan=8 para que ocupe todo el ancho
        
        tk.Label(self.frame_rotaciones, text="Rotacion en X:").grid(row=1, column=0)
        self.entry_rot_x = tk.Entry(self.frame_rotaciones)
        self.entry_rot_x.grid(row=1, column=1)

        tk.Label(self.frame_rotaciones, text="Rotacion en Y:").grid(row=1, column=2)
        self.entry_rot_y = tk.Entry(self.frame_rotaciones)
        self.entry_rot_y.grid(row=1, column=3)

        tk.Label(self.frame_rotaciones, text="Rotacion en Z:").grid(row=1, column=4)
        self.entry_rot_z = tk.Entry(self.frame_rotaciones)
        self.entry_rot_z.grid(row=1, column=5)
        
        self.calc_button_rot = tk.Button(root, text="Calcular Proyeccion con Rotaciones")
        self.calc_button_rot.pack(pady=10)



    def get_punto(self):
        try:
            P_P = np.array([float(self.entry_px.get()), float(self.entry_py.get()), float(self.entry_pz.get())])
            return P_P
        except ValueError:
            messagebox.showerror("Input Error", "Por favor, ingrese números válidos para el punto.")
            return None

    def get_plano(self):
        try:
            PL_M = np.array([float(self.entry_a.get()), float(self.entry_b.get()), float(self.entry_c.get()), float(self.entry_d.get())])
            return PL_M
        except ValueError:
            messagebox.showerror("Input Error", "Por favor, ingrese números válidos para el plano.")
            return None
