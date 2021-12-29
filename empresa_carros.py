from carros import Carros, lista_carros

while(True):
    escolha  = input("1 - Adicionar novo carro\n2 - Imprimir lista de Carros\n3 - Imprimir endereços\n9 - Para sair\n- ")

    if escolha == "1":
        Carros.adicionar_carro()

    elif escolha == "2":
        Carros.print_carros(lista_carros) 

    elif escolha == "3":
        Carros.print_enderecos()

    elif escolha == "9":
        break
    else:
        print("Tente denovo") 
        
