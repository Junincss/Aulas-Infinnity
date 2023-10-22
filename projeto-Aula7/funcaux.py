
def rodar(choice):
    if choice == 1:
        a,b = solicitarnumeros()
        somar(a,b)
    if choice == 2:
        a,b = solicitarnumeros()
        subtrair(a,b)
    if choice == 3:
        a,b = solicitarnumeros()
        dividir(a,b)
    if choice == 4:
        a,b = solicitarnumeros()
        multiplicar(a,b)

def solicitarnumeros():
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite o outro número:"))
    return n1,n2

def somar(a,b):
    soma = a + b
    return print(f"A soma de {a} + {b} é igual a  {soma}")

def subtrair (a,b):
    sub = a - b
    return print(f"A subtração de {a} - {b} é igual a  {sub}")


def multiplicar(a,b):
    mul = a * b 
    return print(f"A multiplicação de {a} * {b} é igual a  {mul}")


def dividir (a,b):
    div = a / b
    return print(f"A divisão de {a} / {b} é igual a  {div}")
