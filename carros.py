from os import system

class Carros:
    def __init__(self, marca, cor, velocidade_max):
        self.marca = marca 
        self.cor = cor
        self.velocidade = velocidade_max
    
    def print_carros(lista):
        system("cls")
        print("Carros Atuais:")
        print("------------")
        for carro in lista:
            print(carro.marca)
            print(carro.cor)
            print(carro.velocidade)
            print("------------")   
            
    def adicionar_carro():
        system("cls")
        marca = input("Coloque a marca do carro:")
        cor = input("Coloque a cor do carro:")
        velocidade_max = input("Coloque a velocidade MAX do carro: ")

        carro = Carros(marca, cor, velocidade_max)
        return lista_carros.append(carro)    

    def print_enderecos():
        system("cls")
        numb = 0
        for carro in lista_carros:
            numb += 1
            print("\n"+ str(numb) +"- "+str(carro) +"\n")


carro1 = Carros("Lamborguini", "Amarela", "280km")
carro2 = Carros("Camaro", "Amarelo", "250km")

lista_carros = [carro1, carro2]