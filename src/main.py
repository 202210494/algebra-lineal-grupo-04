import tkinter as tk
from controller import ProyeccionController

if __name__ == "__main__":
    root = tk.Tk()
    app = ProyeccionController(root)
    root.mainloop()


def main():
   
    puntos = {}
    vectores = {}

    # get punto a proyectar P (x, y, z)
    P_P = np.array([-1, 2, 0])
    puntos["P"] = P_P
    print("Punto a proyectar:\n", P_P)
    
    # get plano donde se proyectará el punto PL_M (ax + by + cz + d = 0)
    PL_M = np.array([2, -3, 1, 2])
    print("Plano donde se proyectará el punto:\n", PL_M)

    # calcular proyeccion ortogonal
       # calcular punto de origen del plano P0 (interseccion con el eje z)
         # cz + d = 0 -> z = -d/c -> P0 = (0, 0, -d/c)
 
    P_P0 = np.array([0, 0, -1 * PL_M[3]/PL_M[2]])  # TODO: MATEMATIZAR  
    print("Punto de origen del plano:\n", P_P0)
    puntos["P_0"] = P_P0
    
       # calcular vector P-P0 (u)
    vec_u = P_P0 - P_P
    vectores["u"] = np.concatenate([P_P, vec_u])

    print("Vector u:\n", vec_u)
       # calular vector normal del plano N (n) 
    vec_n = PL_M[:3]
    vectores["n"] = np.concatenate([P_P0, vec_n / np.linalg.norm(vec_n)])
    vectores["-n"] = np.concatenate([P_P0, -vec_n/ np.linalg.norm(vec_n)])

    print("Vector n:\n", vec_n)
        # vector P-P'(proy_n_u)
    proy_n_u = np.dot(vec_u, -vec_n)/ np.linalg.norm(-vec_n)**2 * -vec_n
    vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])

    print("Vector proyeccion ortogonal:\n", proy_n_u)
       # calcular punto proyectado P'
       # P' = P + proy_n_u
    P_P_ = P_P + proy_n_u
    puntos["P_"] = P_P_

    # mostrar resultado
    print("Punto proyectado:\n", P_P_) 

    graficar(plano=PL_M, vectores=vectores, puntos=puntos)

def calcular_proyeccion(puntos, vectores, root):
    try:
        P_P = np.array([float(entry_px.get()), float(entry_py.get()), float(entry_pz.get())])
        puntos["P"] = P_P
        PL_M = np.array([float(entry_a.get()), float(entry_b.get()), float(entry_c.get()), float(entry_d.get())])

        P_P0 = np.array([0, 0, -1 * PL_M[3] / PL_M[2]])
        puntos["P_0"] = P_P0
        vec_u = P_P0 - P_P
        vectores["u"] = np.concatenate([P_P, vec_u])
        vec_n = PL_M[:3]
        vectores["n"] = np.concatenate([P_P0, vec_n / np.linalg.norm(vec_n)])
        vectores["-n"] = np.concatenate([P_P0, -vec_n / np.linalg.norm(vec_n)])
        proy_n_u = np.dot(vec_u, -vec_n) / np.linalg.norm(-vec_n) ** 2 * -vec_n
        vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])
        P_P_ = P_P + proy_n_u
        puntos["P_"] = P_P_

        graficar(plano=PL_M, vectores=vectores, puntos=puntos)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def main2():
    root = tk.Tk()
    root.title("Proyección Ortogonal de un Punto sobre un Plano")

    puntos = {}
    vectores = {}

    frame_punto = tk.Frame(root)
    frame_punto.pack(pady=10)
    tk.Label(frame_punto, text="Punto a proyectar (x, y, z):").grid(row=0, columnspan=6)

    tk.Label(frame_punto, text="x:").grid(row=1, column=0)
    entry_px = tk.Entry(frame_punto)
    entry_px.grid(row=1, column=1)

    tk.Label(frame_punto, text="y:").grid(row=1, column=2)
    entry_py = tk.Entry(frame_punto)
    entry_py.grid(row=1, column=3)

    tk.Label(frame_punto, text="z:").grid(row=1, column=4)
    entry_pz = tk.Entry(frame_punto)
    entry_pz.grid(row=1, column=5)

    frame_plano = tk.Frame(root)
    frame_plano.pack(pady=10)
    tk.Label(frame_plano, text="Plano (ax + by + cz + d = 0):").grid(row=0, columnspan=8)

    tk.Label(frame_plano, text="a:").grid(row=1, column=0)
    entry_a = tk.Entry(frame_plano)
    entry_a.grid(row=1, column=1)

    tk.Label(frame_plano, text="b:").grid(row=1, column=2)
    entry_b = tk.Entry(frame_plano)
    entry_b.grid(row=1, column=3)

    tk.Label(frame_plano, text="c:").grid(row=1, column=4)
    entry_c = tk.Entry(frame_plano)
    entry_c.grid(row=1, column=5)

    tk.Label(frame_plano, text="d:").grid(row=1, column=6)
    entry_d = tk.Entry(frame_plano)
    entry_d.grid(row=1, column=7)

    tk.Button(root, text="Calcular y Graficar", command=calcular_proyeccion).pack(pady=10)

    root.mainloop()


# Si no se coloca el __name__ = "__main__", te ejecutas todos los .py importados      
if __name__ == "__main__":
    main2()


