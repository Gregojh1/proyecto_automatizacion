from calculadora import calculadora


class menu:
    def __init__(self):  # constructor
        pass

    def pedirNumeros(self):
        a = float(input("ingrese el primer numero"))
        b = float(input("ingrese el segundo numero"))

        return a, b

    def elegirOperacion(self):


        calculadora1 = calculadora()
        bandera = True

        while bandera:
            operacion = int(
            input("Elija operacion: 1. sumar 2.restar 3.multiplicar 4.dividir 5.salir"))
            match operacion:
                case 1:
                    a, b = self.pedirNumeros()
                    print (f"Resultados: {calculadora1.sumar(a, b)}")
                case 2:
                    a, b = self.pedirNumeros()
                    print(f"Resultado: {calculadora1.restar(a, b)}")
                case 3:
                    a, b = self.pedirNumeros()
                    print (f"Resultado: {calculadora1.multiplicar(a, b)}")
                case 4:
                    a, b = self.pedirNumeros()
                    print(f"Resultado: {calculadora1.dividir}")
                case 5:
                    calculadora1.apagar
                    bandera = False
                case _:
                    print("opncion incorrecta")
