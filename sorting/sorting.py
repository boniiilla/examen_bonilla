'''
1. Ordenar una lista de numeros
2.1. pedir numeros y guardarlos en una lista
2.3. ordernarlos
'''

class Sorting:
    def __init__(self):
        self.numeros = []
    
    def pedir_numeros(self):
        self.numero = 0
        print("Introduce 10 numeros: ")
        for i in range(10):
            self.numero = int(input())
            self.numeros.append(self.numero)

    def ordenar_numeros(self):
        Sorting.pedir_numeros(self)
        for numero1 in range(len(self.numeros)):
            for numero2 in range(numero1,len(self.numeros)):
                if self.numeros[numero1] > self.numeros[numero2]:
                    self.numeros[numero1], self.numeros[numero2] = self.numeros[numero2], self.numeros[numero1]
    
    def mostrar_lista(self):
        Sorting.pedir_numeros(self)
        print("Lista ordenada:")
        for numero in self.numeros:
            print(f"\t{numero}")