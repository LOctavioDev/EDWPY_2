"""" 
    EJERCICIOS DE LISTA SIMPLEMENTE LIGADA 

    a) Crear una funcion que permita insertar un elemento al final de la lista ya creada.
    b) Crear una funcion que prmita insertar un elemento inmediatamente despues de un numero que se enceuntra en la lista.
    c) Crear una funcion que permita calcular el promedio de los elementos de una lista ya creada.
    d) Implemente una funcion que, para una lista dada, elimine el nodo que tenga el mayor.
    e) Implemente una funcion que sumprima de la lista todos los elementos mayores qe un numero dad como limite. Por ejemplo si la lista inicial es:
    f) Escribe una funcion que dada una lista L devuelva otra lista R conteniendo los elementos repetidos de L. Por ejemplo, si L almacena los valores 5,2,7,2,5,5,1 debe construir una lista R con los valores 5,2. SI no hay elementos repetidos, R sera la lista vacia.
    g) Escribe una funcion que dada una lista L devuelva una lista R, inversa de L
     
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # FUNCION PARA INSERTAR UN ELEMNTO AL FINAL DE LA LISTA
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # FUNCION PARA INSERTAR UN ELEMENTO DESPUES DE UN NUMERO EN LA LISTA
    def insertar_despues_de(self, numero, dato):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        while actual:
            if actual.dato == numero:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                break
            actual = actual.siguiente

    # FUNCION PARA CALCULAR EL PROMEDIO DE LOS ELEMNTOS DE UNA LISTA
    def calcular_promedio(self):
        actual = self.cabeza
        suma = 0
        contador = 0
        while actual:
            suma += actual.dato
            contador += 1
            actual = actual.siguiente
        if contador == 0:
            return 0
        return suma / contador

    #  ELIMINAR EL NODO QUE CONTIENE EL VALOR MAXICO
    def eliminar_maximo(self):
        if not self.cabeza:
            return
        max_valor = self.cabeza.dato
        actual = self.cabeza
        nodo_anterior = None
        while actual.siguiente:
            if actual.siguiente.dato > max_valor:
                max_valor = actual.siguiente.dato
                nodo_anterior = actual
            actual = actual.siguiente
        if nodo_anterior:
            nodo_anterior.siguiente = nodo_anterior.siguiente.siguiente
        else:
            self.cabeza = self.cabeza.siguiente

    # FUNCION PARA OBTENER LISTA CON ELEMENTOS REPETIDOS
    def obtener_repetidos(self):
        elementos = {}
        repetidos = ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.dato in elementos:
                repetidos.insertar_al_final(actual.dato)
            elementos[actual.dato] = True
            actual = actual.siguiente
        return repetidos

    # FUNCION PARA LA LISTA INVESRSA
    def obtener_inversa(self):
        inversa = ListaEnlazada()
        actual = self.cabeza
        while actual:
            nuevo_nodo = Nodo(actual.dato)
            nuevo_nodo.siguiente = inversa.cabeza
            inversa.cabeza = nuevo_nodo
            actual = actual.siguiente
        return inversa

    # METODO PARA MOSTRAR LA LISTA
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


lista = ListaEnlazada()
lista.insertar_al_final(3)
lista.insertar_al_final(7)
lista.insertar_al_final(1)
lista.insertar_al_final(1)
lista.insertar_al_final(1)
lista.mostrar_lista()  

# INSERTAR UN NUMERO DESPUES DE OTRO
lista.insertar_despues_de(7, 10)
lista.mostrar_lista()  

# PROMEDIO 
promedio = lista.calcular_promedio()
print("Promedio:", promedio)  

# ELIMINAR EL DE VALOR MAXIMO
lista.eliminar_maximo()
lista.mostrar_lista() 

# LISTA CON ELEMENTOS REPETIDOS
repetidos = lista.obtener_repetidos()
repetidos.mostrar_lista() 

# LISTA INVERSA
inversa = lista.obtener_inversa()
inversa.mostrar_lista()  
