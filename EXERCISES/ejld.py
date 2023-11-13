# Implementa una lista doblemente enlazada para crear una lista de tareas (to-do list). Cada tarea tiene un nombre y un estado (pendiente o completada). Debes realizar las siguientes operaciones:

"""

    1.- Agregar una tarea al final de la lista.
    2.- Marcar una tarea como completada.
    3.- Mover una tarea hacia arriba en la lista.
    4.- Mover una tarea hacia abajo en la lista.
    5.- Eliminar una tarea de la lista.
    
"""

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False
        self.before = None  
        self.after = None

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def empty(self):
        return self.first is None

    def add_task(self, name):
        new_task = Task(name)
        if self.empty():
            self.first = self.last = new_task
        else:
            new_task.before = self.last
            self.last.after = new_task
            self.last = new_task
        self.size += 1
    
    def mark_completed(self, task_name):
        current_task = self.first
        while current_task:
            if current_task.name == task_name:
                current_task.completed = True
                return
            current_task = current_task.after

    def move_up(self, task_name):
        current_task = self.first
        while current_task:
            if current_task.name == task_name:
                if current_task.before:

                    if current_task.after:
                        current_task.before.after = current_task.after
                        current_task.after.before = current_task.before
                    else:
                        current_task.before.after = None
                        self.last = current_task.before

                    current_task.after, current_task.before = current_task.before, current_task.after
                    if not current_task.before:
                        self.first = current_task
                    return
                else:
                    print("La tarea ya esta en la parte superior")
                    return
            current_task = current_task.after

    def move_down(self, task_name):
        current_task = self.first
        while current_task:
            if current_task.name == task_name:
                if current_task.after:
                    if current_task.before:
                        current_task.after.before = current_task.before
                        current_task.before.after = current_task.after
                    else:
                        current_task.after.before = None
                        self.first = current_task.after
    
                    current_task.before, current_task.after = current_task.after, current_task.before
                    if not current_task.after:
                        self.last = current_task
                    return
                else:
                    print("La tarea ya est en la parte inferior")
                    return
            current_task = current_task.after


    def remove_task(self, task_name):
        current_task = self.first
        while current_task:
            if current_task.name == task_name:
                if current_task.before:
                    current_task.before.after = current_task.after
                else:
                    self.first = current_task.after

                if current_task.after:
                    current_task.after.before = current_task.before
                else:
                    self.last = current_task.before

                self.size -= 1
                return
            current_task = current_task.after



to_do_list = DoublyLinkedList()

to_do_list.add_task("Hacer la compra")
to_do_list.add_task("Estudiar para el examen")
to_do_list.add_task("Hacer ejercicio")

# MARCAR UNA TAREA COMO COMPLETADA
to_do_list.mark_completed("Estudiar para el examen")

# MOVERUNA HACIA ARRIBA
to_do_list.move_up("Hacer ejercicio")

# MOVERUNA HACIA ABAJO
to_do_list.move_down("Hacer la compra")

# ELIMINAR UNA TAREA
to_do_list.remove_task("Estudiar para el examen")

# MOSTRAR LA LISTA DE TAREAS
current_task = to_do_list.first
while current_task:
    print(f"{current_task.name} - {'Completada' if current_task.completed else 'Pendiente'}")
    current_task = current_task.after
