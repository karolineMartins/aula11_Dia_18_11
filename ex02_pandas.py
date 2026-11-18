#solicida ao usuario a quantidade de cadastro para o datafreme

import pandas as pd 

#Lista vazias para o armazenar os dados 
cargos = []
salarios = []

#Quantos registros o usuario vai informar 
qtd = int(input("Quantos cargos deseja cadastrar? "))

#Coleta de dados 
for i in range(qtd):
    print(f"Cadastro {i+1}:")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salario: "))

    cargos.append(cargo)
    salarios.append(salario)

#Criação do DataFrame   
dados = {"Cargos": cargos, "Salarios": salarios}
dados_bi = pd.DataFrame(dados)

# Exibição do DataFrame
print("------------ Tabela de Cargos e Salarios: ------------")
print(dados_bi)