import random

# user = input("Insira seu nome: ")

# computer = "Computador"

# option = ['pedra','papel','tesoura']
# user_choice = input("Escolha uma opção abaixo: \n1- pedra \n2- papel \n3- tesoura\n\n\t ")

def sort_and_choice(user_choice):
    if (user_choice == '1' ):
        user_choice = 'pedra'
    elif(user_choice== '2' ):
        user_choice = 'papel'
    elif(user_choice == '3'):
        user_choice = 'tesoura'
    else:
        user_choice = 'sair'
    return user_choice


# computer_choice = random.choice(option)


def declareWinner(user, computer, user_choice,computer_choice):
    if(user_choice == "pedra" and computer_choice == "tesoura" ):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O grande vencedor é: {user} !")  
    elif(user_choice == "pedra" and computer_choice == "papel") :
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O grande vencedor é: {computer} !")  
    elif(user_choice == "pedra" and computer_choice == "pedra" ):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O Resultado é EMPATE !")  
    elif(user_choice == 'tesoura' and computer_choice == 'papel'):
        return print(f'Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O Grande vencedor é: {user}')
    elif(user_choice == "tesoura" and computer_choice == "pedra" ):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O grande vencedor é: {computer} !")
    elif(user_choice == "tesoura" and computer_choice == "tesoura" ):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O Resultado é EMPATE !")
    elif(user_choice == 'papel' and computer_choice == 'pedra'):
        return print(f'Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O Grande vencedor é: {user}')
    elif(user_choice == 'papel' and computer_choice == 'tesoura'):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O grande vencedor é: {computer} !")
    elif(user_choice == 'papel' and computer_choice == 'papel'):
        return print(f"Você escolheu {user_choice}\nO computador escolheu: {computer_choice} então \n O Resultado é EMPATE ! \n\n") 
    else:
        print("Você escolheu sair")
        print('_-------------------------------------_')
        print('Encerrando o programa.')
        exit()
    


def main():
    user = input("Insira seu nome: ")

    computer = "Computador"
    
    option = ['pedra','papel','tesoura']

    user_choice = input("Escolha uma opção abaixo: \n1- pedra \n2- papel \n3- tesoura \n 4 - Sair \n\n> ")


    choice = sort_and_choice(user_choice)
    computer_choice = random.choice(option)
    declareWinner(user, computer, choice, computer_choice)
    print("\n\n ----------------------------------------------------------------------\n\n")
    while(user_choice != "4"):
        main()




main()
