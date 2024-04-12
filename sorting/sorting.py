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
        error = False
        for numero in range(len(self.numeros)):
            if self.numeros[numero] > self.numeros[numero +1] and error == False:
                self.numeros[numero], self.numeros[numero +1] = self.numeros[numero +1], self.numeros[numero]
                print(numero)