"""
    
    EXAMEN: Elabora un programa que gestione una lista simplemente ligada que almacena los datos de una competencia de turismo.
    
    La estructura es como sigue:
    
    - Nombre del piloto
    - Modelo del vehiculo
    - Puntos obtenidos
    - Direccion del siguiente nodo
    
    El modulo debera definir las siguientes operaciones sobre los elementos de la lista:
    
    - Inicilizar: inicia la lista tomando en cuenta que siempre comienza vacia.
    - Aniadir despues de 6 elementos al principio de la lista.
    - Aniadir despues de: aniade elementos despues de un elemento en particular.
    - Buscar Ganador: realiza un recorrido por la lista buscando al piloto con mas puntos, imprime el nombre y el modelo del vehiculo.
    - Elimina al primer piloto: elimina a un elemento en particular de la lista.
    -  Mostrar datos: muestra los datos de todos los pilotos.
    - Buscar piloto: dado el nombre de un piloto y determinar si existe o no existe.
    - Eliminar al piloto puntero: recorre la lista buscando al piloto con mas puntos. Un a vez que lo encuentra, modifica la puntuacion del piloto de la derecha sumandole un punto y al piloto puntero restandole un punto.
    

"""
from colorama import Fore, Back, Style, init


class Nodo:
    def __init__(self, nombre, modelo, puntos):
        self.nombre = nombre
        self.modelo = modelo
        self.puntos = puntos
        self.siguiente = None

class ListaCompetencia:
    def __init__(self):
        self.primer_nodo = None

    def inicializar(self):
        self.primer_nodo = None

    def aniadir_inicio(self, nombre, modelo, puntos):
        nuevo_nodo = Nodo(nombre, modelo, puntos)
        nuevo_nodo.siguiente = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def aniadir_despues_de(self, nombre_anterior, nombre, modelo, puntos):
        nuevo_nodo = Nodo(nombre, modelo, puntos)
        actual = self.primer_nodo
        while actual:
            if actual.nombre == nombre_anterior:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                break
            actual = actual.siguiente

    def buscar_ganador(self):
        max_puntos = -1
        ganador_nombre = ""
        ganador_modelo = ""
        actual = self.primer_nodo
        while actual:
            if actual.puntos > max_puntos:
                max_puntos = actual.puntos
                ganador_nombre = actual.nombre
                ganador_modelo = actual.modelo
            actual = actual.siguiente
        if max_puntos != -1:
            print("\n----------Ganador:\n-----Nombre =", ganador_nombre, "\n-----Modelo =", ganador_modelo, "\n")

    def eliminar_primero(self, nombre):
        actual = self.primer_nodo
        anterior = None
        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.primer_nodo = actual.siguiente
                break
            anterior = actual
            actual = actual.siguiente

    def mostrar_datos(self):
        actual = self.primer_nodo
        while actual:
            print("\n-----Nombre:", actual.nombre, "\nModelo:", actual.modelo, "\nPuntos:", actual.puntos)
            actual = actual.siguiente

    def buscar_piloto(self, nombre):
        actual = self.primer_nodo
        while actual:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
        return False

    def eliminar_piloto_puntero(self):
        max_puntos = -1
        piloto_puntero = None
        actual = self.primer_nodo
        anterior = None
        while actual:
            if actual.puntos > max_puntos:
                max_puntos = actual.puntos
                piloto_puntero = actual
                piloto_anterior = anterior
            anterior = actual
            actual = actual.siguiente

        if piloto_puntero:
            piloto_puntero.puntos -= 1
            if piloto_anterior:
                piloto_anterior.puntos += 1
            else:
                self.primer_nodo = piloto_puntero.siguiente


lista = ListaCompetencia()
lista.inicializar()

lista.aniadir_inicio("Briones", "M-1", 1)
lista.aniadir_inicio("Haziel", "M-2", 2)
lista.aniadir_inicio("Jesus", "M-3", 3)
lista.aniadir_inicio("Raul", "M-4", 4)
lista.aniadir_inicio("Brayan", "M-5", 5)
lista.aniadir_inicio("Sech", "M-6", 6)

lista.aniadir_despues_de("Briones", "Abdiel", "M-7", 7)

lista.buscar_ganador()

lista.eliminar_primero("Briones")

print("BUSQUEDA DEL PILOTO:", lista.buscar_piloto("Raul"))

lista.eliminar_piloto_puntero()
lista.mostrar_datos()
