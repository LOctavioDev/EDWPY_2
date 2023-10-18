# UNA LISTA ENLAZADA ES UNA ESTRUCTURA DE DATOS LINEAL QUE CONSTA DE NODOS, DONDE CADA NODO CONTIENE UN VALOR Y UNA REFERENCIA O PUNTERO AL SIGUIENTE NODO EN LA LISTA

class Nodo: 
    def __init__(self, valor): # ACA TENEMOS EL CONSTRUCTOR DE LA CLASE NODO.
        self.valor = valor     # LOS ARGUMENTOS EN ESTE CASO EL VALOR QUE EL NODO ALMACENARA.
        self.siguiente = None

class listaEnlazada:
    def __init__(self):
        self.cabeza  = None    #EL CONSTRUCTOr DE LA CLASE listaEnlazada EN ESTE CASO INICIALIZA UNA LISTA VACIA.
        
    def agregar_al_principio(self, valor):      # ACA AGREGAMOS UN NODO AL PRINCIPIO DE LA LISTA
        nuevo_nodo = Nodo(valor)                # LOS ARGUMENTOS EN ESTE CASO EL VALOR A ALMACENAR EN EL NUEVO NODO
        nuevo_nodo.siguiente = self.cabeza      # EL NUEVO NODO APUNTA AL NODO ACTUAL DE LA CABEZA
        self.cabeza = nuevo_nodo        # LA CABEZA AHORA ES EL NUEVO NODO JSJSJS
    
    def eliminar(self, valor):          # ELIMINA EL PRIMER NODO QUE CONTIENE EL VALOR ESPECIFICADO
        actual = self.cabeza            # EN LOS ARGUMENTOS EL VALOR EN ESTE CASO ES EL DEL NODO A ELIMINAR
        if actual is not None and actual.valor == valor:    #SI EL VALOR ESTA EN LA CABEZA, ACTUALIZAMOS LA CABEZA
            self.cabeza = actual.siguiente
            return
            
        while actual is not None:
            if actual.valor == valor:
                break
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return
        anterior.siguiente = actual.siguiente
    
    def mostrar(self):
        actual = self.cabeza        # MUESTRA LOS VALORES DE LOS NODOS EN LA LISTA
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
        
# CREAMOS LA LISTA ENLAZADA 
mi_lista = listaEnlazada()

# AGREGAR ELEMENTOS AL PRINCIPIO DE LA LISTA
mi_lista.agregar_al_principio(3)
mi_lista.agregar_al_principio(2)
mi_lista.agregar_al_principio(1)

#  MOSTRAR LA LISTA
mi_lista.mostrar()

# ELIMINAR UN ELEMENTO DE LA LISTA
mi_lista.eliminar(2)

# MOSTRAR LA LISTA PARA VER EL ELEMENTO ELIMINADO
mi_lista.mostrar()