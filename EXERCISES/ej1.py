# SUPONGAMOS QUE ESTAS DESARROLLANMDO UN SISTEMA DE REGISTRO DE ALUMNOS PARA UNA ESCELA. CADA ALUMNO SE REPRESENTA COMO UNA ESTRUCTURA QUE CONTIENE SU NOMBRE Y SU CALIFICACION. DEBES IMPLEMETAR UNA LISTA ENLAZADA PARA ALMACENAR ESTOS REGISTROS Y RESLIZAR LAS SIGUIENTES OPERACIONES:


"""

    1.- Agregar un alumno al final de la lista
    2.- Eliminar un alumno por su nombre 
    3.- Mostrar la lista de alumnos

"""


class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        self.siguiente = None


class listaEnlazada:
    def __init__(self):
        self.cabeza = None
    def agergar_al_final(self, nombre, calificacion):
        new_alumno = Alumno(nombre,calificacion)
        if not self.cabeza:
            self.cabeza = new_alumno
        else:
            actual = self.cabeza

            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = new_alumno
            
    def eliminar_por_nombre(self, nombre):
      actual = self.cabeza
      if actual and actual.nombre == nombre:
          self.cabeza = actual.siguiente
          return
      while actual:
          if actual.nombre == nombre:
              break
          anterior = actual
          actual = actual.siguiente
      if actual is None:
          print(f"El alumno con el nombre '{nombre}' no se encontró en la lista.")
          return
      anterior.siguiente = actual.siguiente
    
            
    def mostrar(self):
        actual = self.cabeza
        
        while actual:
            print(f'Nombre: {actual.nombre}, Calificacion {actual.calificacion}')
            actual = actual.siguiente
    

def printel():
    print("------------------------------\n")


una_lista = listaEnlazada()
printel()
una_lista.agergar_al_final('Briones', 10)
una_lista.mostrar()
printel()
una_lista.agergar_al_final('Haziel', 9.7)
una_lista.agergar_al_final('Jaime', 8.8)
una_lista.mostrar()
una_lista.eliminar_por_nombre('Briones')
printel()
una_lista.mostrar()