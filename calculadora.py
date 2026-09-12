class Calculadora:
    def __init__(self):  # constructor
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a- b

    def multiplicar (self, a, b): 
        return a * b

    def dividir (self, a, b):
        if b == 0:
            raise ValueError ("error no se puede dividir entre cero")
        else:
            return a/b
            

    def apagar(self):
        print("apagando")
        exit()