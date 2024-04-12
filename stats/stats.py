'''
1. Calcul Desviacio estandar
2.1 Calcular la mitjana
2.2. Aplicar la formula per calcular la desviacio estandar
'''

class Statistics:
    def __init__(self) -> None:
        self.numeros = [1,2,3,4,5,6,6,7,8]
        self.mitjana: int = 0
        self.suma_desviacio: int = 0
        self.desviacio_e: int = 0

    def calcul_mitjana(self):
        for numero in self.numeros:
            suma_num = numero + suma_num
        self.mitjana = suma_num / len(self.numeros)
    
    def calcul_suma_desviacio(self):
        Statistics.calcul_mitjana(self)
        if self.mitjana != 0:
            for numero in self.numeros:
                self.suma_desviacio = self.suma_desviacio + ((numero - self.mitjana)**2)
    
    def calcul_desviacioe(self):
        Statistics.calcul_suma_desviacio(self)
        if self.mitjana != 0:
            self.desviacio_e = (self.suma_desviacio/len(self.numeros))**0.5
        else:
            self.desviacio_e = 0

    def mostrar_resultat(self):
        Statistics.calcul_desviacioe(self)
        print(f"La desviació estàndar es {self.desviacio_e}")

class Main:
    desviacio = Statistics()
    desviacio.mostrar_resultat()

app = Main()

