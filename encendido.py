from menu import menu
class encender:
    def __init__(self):  #constructor 
        pass

    @staticmethod
    def iniciar ():
        print("bienvenido a la calculadora python")
        miMenu = menu()
        miMenu.elegirOperacion()