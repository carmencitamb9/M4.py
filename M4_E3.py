"""
******************************************************************************************************
Autor       : Bristela Muñoz Burgos
Carrera     : Ingeniería en Informática
Ramo        : Programación Básica
Modulo      : M4-E3
Ejercicio 3 : 
Crear una clase llamada “cuenta”. Al instanciar la clase se debe proveer el número de cuenta,
el nombre el titular, saldo inicial, tipo cuenta (ahorro, corriente, inversiones). Crear tres métodos depositar,
retirar, obtener balance. Si en la cuenta1 hay un saldo inicial de 10 y se hace un depósito de 20 y un retiro de 5,
entonces al obtener el balance debe mostrar un saldo de 25. Imprimir la información con todos los
datos de usuarios y balances.

******************************************************************************************************
"""

class cuenta:
    def __init__(ObjetoCliente):
        ObjetoCliente.nro_cuenta = "123456"
        ObjetoCliente.nom_titular = "Josefina La Gallina"
        ObjetoCliente.saldo_Inicial = 10
        ObjetoCliente.tipo_cuenta = "corriente"
    def depositar(ObjetoCliente, cantidad):
        ObjetoCliente.saldo_Inicial += cantidad
    def retiro(ObjetoCliente, cantidad):
        ObjetoCliente.saldo_Inicial -= cantidad

if __name__ == "__main__":
    Cliente1 = cuenta()
    print("**********  CLIENTE ***************************************")
    print("Nombre:",Cliente1.nom_titular)
    print("Tipo Cuenta:", Cliente1.tipo_cuenta)
    print("N° Cuenta:", Cliente1.nro_cuenta)
    print("Saldo Inicial:",Cliente1.saldo_Inicial)

    Cliente1.depositar(20)
    Cliente1.retiro(5)
    print("**********  CLIENTE DESPUES DEL LOS DEPOSITO Y RETIRO *****")
    print("Nombre:",Cliente1.nom_titular)
    print("Tipo Cuenta:", Cliente1.tipo_cuenta)
    print("N° Cuenta:", Cliente1.nro_cuenta)
    print("Saldo Final:",Cliente1.saldo_Inicial)
