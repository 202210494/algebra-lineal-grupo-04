import Controlador as c
import Modelo as m

def main():
    modelo = m.Modelo()
    #vista = v.Vista()
    controlador = c.Controlador(modelo)    
    controlador.iniciar_aplicacion()

# Si no se coloca el __name__ = "__main__", te ejecutas todos los .py importados      
if __name__ == "__main__":
    main()

# Se ha validado que los resultados de la proyeccion ortogonal 
# fueran los mismos que el anteior programa
