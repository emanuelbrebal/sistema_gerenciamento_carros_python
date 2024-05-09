import sqlite3
import gerenciador
import lista_busca

conexao = sqlite3.connect('carros.sqlite') #cria conexão com banco de dados
cursor = conexao.cursor() #cria o cursor (intermediario entre programa e banco de dados)

continua = True #variável de controle do While

while continua == True: #menu em loop
    menu = int(input("Bem vindo ao aplicativo de Gerenciamento de carros.\n\n Por favor, insira:\n 1 - para cadastrar um novo veículo\n 2 - para listar os carros\n 3- para realizar uma busca por ID\n 0 - encerrar.\n"))

    if menu == 1: #cadastrar novo carro
        print("-----Cadastrando novo veículo-----")
        new_model = input("\nDigite o modelo do carro que quer registrar: ")
        new_year = input("Qual ano do carro? ")
        new_doors_quantity = input("Quantas portas? ")
        new_horse_power = int(input("E quantos cavalos de potência? "))
        print("\n")
        gerenciador.insert_car(new_model, new_year, new_doors_quantity, new_horse_power) 
        
    elif menu == 2: #exibindo todos os carros registrados
        print("\n-----Exibindo todos os carros registrados-----")
        lista_busca.list_cars()

    elif menu == 3: #busca por ID
        print("\n-----Exibindo carros selecionados por ID-----")
        new_id = int(input("Digite o ID do carro desejado: "))
        lista_busca.list_cars_byId(new_id)
        print("\n")

    elif menu == 0 : #encerra a sessão
        print("-----Fim de sessão-----")
        continua = False
    else: 
        print("\n-----Entrada Inválida, por favor tente novamente.-----\n")
        continue
