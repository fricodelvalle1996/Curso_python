from random import *
from os import system

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, numero_cuenta, balance):
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente {self.nombre} {self.apellido}, con número de cuenta {self.numero_cuenta} tiene un balance de {self.balance}€\n"

    def deposito(self):
        deposito1 = int(input("Introduce el importe que quieres depositar en tu cuenta: "))
        return deposito1

    def retirada(self):
        retirada1 = int(input("Introduce el importe que quieres retirar de tu cuenta: "))
        return retirada1

def crear_cliente():
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    num_cuenta = randint(111111111, 999999999)
    cliente = Cliente(num_cuenta, 0)
    cliente.nombre = nombre
    cliente.apellido = apellido
    return cliente


def inicio():
    system("cls")
    print("Buenos días, bienvenid@ al banco FRDV\n")

    #crear cuenta
    cliente = crear_cliente()
    cliente.balance = 0
    print(cliente)
    print('\n')
    accion = "x"

    while accion != "Salir":
        # que quieres hacer?
        accion = input("¿Que acción desea realizar ([Depositar]/[Retirar]/[Salir])?: ")

        if accion == 'Depositar':
            deposito = cliente.deposito()
            cliente.balance += deposito
            print(f"Has depositado {deposito}€ con éxito\n")

        elif accion == 'Retirar':
            deseo_retirar = cliente.retirada()
            if cliente.balance - deseo_retirar > 0:
                cliente.balance -= deseo_retirar
                print(f"Has retirado {deseo_retirar}€ con éxito\n")
            else:
                print("No tiene fondos para retirar el importe seleccionado")

        # mostrar balance
        print(cliente)

    print("Gracias por confiar en FRDV. Vuelva pronto")


inicio()
