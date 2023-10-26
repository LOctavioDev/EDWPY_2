class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDobleLigada:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def esta_vacia(self):
        return self.primer_nodo is None

    def agregar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo.siguiente = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo

    def eliminar(self, valor):
        nodo_actual = self.primer_nodo
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.primer_nodo = nodo_actual.siguiente

                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.ultimo_nodo = nodo_actual.anterior

                return  # NODO ELIMINADO
            nodo_actual = nodo_actual.siguiente

    def imprimir_lista(self):
        nodo_actual = self.primer_nodo
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" <-> ")
            nodo_actual = nodo_actual.siguiente
        print("None")



mi_lista = ListaDobleLigada()

mi_lista.agregar_al_principio(1)
mi_lista.agregar_al_principio(2)
mi_lista.agregar_al_final(3)
mi_lista.agregar_al_final(4)
mi_lista.agregar_al_principio(5)

mi_lista.imprimir_lista() 

mi_lista.eliminar(2)

mi_lista.imprimir_lista()  