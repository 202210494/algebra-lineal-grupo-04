import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageSequence
import numpy as np

class ProyeccionView:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Proyección Ortogonal y Rotaciones")
        self.root.geometry("1200x600")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Configuración de modo oscuro
        self.style.configure(".", background="#2E2E2E", foreground="#FFFFFF", fieldbackground="#2E2E2E")
        self.style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
        self.style.configure("TButton", background="green", foreground="#FFFFFF", relief=tk.FLAT, font=("Arial", 12),
                             width=20, padding=5, borderwidth=0)
        self.style.map("TButton", background=[('active', "#1A4B27"), ('pressed', "#1A2A4B")])  # Cambiar color al pasar el mouse
                             
        
        self.style.configure("TEntry", fieldbackground="#4D4D4D", foreground="#FFFFFF", insertbackground="cyan", selectbackground="blue", selectforeground="white") 

        self.root.configure(bg="#2E2E2E")

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        ############################## Punto a proyectar ##############################
        size_box = 5

        self.frame_punto = ttk.Frame(self.left_frame)
        self.frame_punto.pack(pady=10)
        ttk.Label(self.frame_punto, text="Punto a proyectar (x, y, z):").grid(row=0, columnspan=6)

        ttk.Label(self.frame_punto, text="x:").grid(row=1, column=0)
        self.entry_px = ttk.Entry(self.frame_punto, width=size_box)
        self.entry_px.grid(row=1, column=1, padx=5)

        ttk.Label(self.frame_punto, text="y:").grid(row=1, column=2)
        self.entry_py = ttk.Entry(self.frame_punto, width=size_box)
        self.entry_py.grid(row=1, column=3)

        ttk.Label(self.frame_punto, text="z:").grid(row=1, column=4)
        self.entry_pz = ttk.Entry(self.frame_punto, width=size_box)
        self.entry_pz.grid(row=1, column=5)

        ############################## Ecuacion del plano ##############################
        self.frame_plano = ttk.Frame(self.left_frame)
        self.frame_plano.pack(pady=10)
        ttk.Label(self.frame_plano, text="Plano (ax + by + cz + d = 0):").grid(row=0, columnspan=8)

        self.entry_a = ttk.Entry(self.frame_plano, width=size_box)
        self.entry_a.grid(row=1, column=0) 
        ttk.Label(self.frame_plano, text="x + ").grid(row=1, column=1)

        self.entry_b = ttk.Entry(self.frame_plano, width=size_box)
        self.entry_b.grid(row=1, column=2)
        ttk.Label(self.frame_plano, text="y + ").grid(row=1, column=3)

        self.entry_c = ttk.Entry(self.frame_plano, width=size_box)
        self.entry_c.grid(row=1, column=4)
        ttk.Label(self.frame_plano, text="z + ").grid(row=1, column=5)

        self.entry_d = ttk.Entry(self.frame_plano, width=size_box)
        self.entry_d.grid(row=1, column=6)      
        ttk.Label(self.frame_plano, text="= 0").grid(row=1, column=7)

        self.calc_button = ttk.Button(self.left_frame, text="Calcular y Graficar")
        self.calc_button.pack(pady=10)

        ############################## Rotaciones ##############################
        self.frame_rotaciones = ttk.Frame(self.left_frame)
        self.frame_rotaciones.pack(pady=10)
        ttk.Label(self.frame_rotaciones, text="Rotaciones (grados):").grid(row=0, columnspan=8) 
        
        ttk.Label(self.frame_rotaciones, text="Rotación en X:").grid(row=1, column=0)
        self.entry_rot_x = ttk.Entry(self.frame_rotaciones, width=size_box)
        self.entry_rot_x.grid(row=1, column=1)

        ttk.Label(self.frame_rotaciones, text="Rotación en Y:").grid(row=1, column=2)
        self.entry_rot_y = ttk.Entry(self.frame_rotaciones, width=size_box)
        self.entry_rot_y.grid(row=1, column=3)

        ttk.Label(self.frame_rotaciones, text="Rotación en Z:").grid(row=1, column=4)
        self.entry_rot_z = ttk.Entry(self.frame_rotaciones, width=size_box)
        self.entry_rot_z.grid(row=1, column=5)

        self.calc_button_rot = ttk.Button(self.left_frame, text="Calcular Proyección con Rotaciones")
        self.calc_button_rot.pack(pady=10)

        ############################## GIF ##############################
        self.frame_gif = ttk.Frame(self.right_frame)
        self.frame_gif.pack(fill=tk.BOTH, expand=True)
        ttk.Label(self.frame_gif, text="Visualización del GIF:").pack()

        self.gif_label = ttk.Label(self.frame_gif)
        self.gif_label.pack(expand=True)
        self.load_gif("proyeccion.gif")

    def load_gif(self, path):
        self.gif = Image.open(path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        self.update_gif()

    def update_gif(self):
        frame = self.frames[self.frame_index]
        self.gif_label.configure(image=frame)
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(100, self.update_gif)

    def get_punto(self):
        try:
            P_P = np.array([1,0,0]) #dev
            #P_P = np.array([float(self.entry_px.get()), float(self.entry_py.get()), float(self.entry_pz.get())])
            return P_P
        except ValueError:
            messagebox.showerror("Input Error", "Por favor, ingrese números válidos para el punto.")
            return None

    def get_plano(self):
        try:
            PL_M = np.array([1,2,3,4])
            #PL_M = np.array([float(self.entry_a.get()), float(self.entry_b.get()), float(self.entry_c.get()), float(self.entry_d.get())])
            return PL_M
        except ValueError:
            messagebox.showerror("Input Error", "Por favor, ingrese números válidos para el plano.")
            return None

    def get_rotaciones(self):
        try:
            # si no se detalla se considerara 0
            rot_x = float(self.entry_rot_x.get()) if self.entry_rot_x.get() else 0
            rot_y = float(self.entry_rot_y.get()) if self.entry_rot_y.get() else 0
            rot_z = float(self.entry_rot_z.get()) if self.entry_rot_z.get() else 0
            rot_z = 180
            return np.radians([rot_x, rot_y, rot_z]) # convertir a radianes
        except ValueError:
            messagebox.showerror("Input Error", "Por favor, ingrese números válidos para las rotaciones.")
            return None