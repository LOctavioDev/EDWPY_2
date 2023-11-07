class ArraySorter:
    def __init__(self, array):
        self.array = array
        
    def selection_sort(self):
        n = len(self.array)
        
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i],self.array[min_index] = self.array[min_index],self.array[i]

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                

arr = [9,8,7,6,5,4,3,2,1]
sorter = ArraySorter(arr)

print(f'ARREGLO ACTUAL {arr}')
sorter.selection_sort()
print(f'ARREGLO CON METODO DE SELECCION {arr}')

arr = [9,8,7,6,5,4,3,2,1]
bubble = ArraySorter(arr)

print(f'ARREGLO ACTUAL {arr}')
bubble.bubble_sort()
print(f'ARREGLO CON BUBBLE {arr}')