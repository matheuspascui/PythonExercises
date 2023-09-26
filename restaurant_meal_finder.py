'''Os principais objetivos deste programa são:
- possuir por padrão lista com algumas refeições
- permitir que o usuário adicione opções nessas listas
- sugerir "aleatoriamente" uma opção para o usuário

Implementação:
--> listas de comidas e locais

manha - café da manhã
tarde - almoço
noite - jantar

'''
import random
# Função MAIN para conter o programa principal
# Funções como Mostrar_refeicoes_cafe, Mostrar_refeicoes_almoco, chamadas baseadas em IF hora_refeicao da match
# Carregar as listas built-in antes do programa começar (antes de chamar a MAIN)

comidas_cafe_manha = ["Pão na chapa", "Café com leite", "Pão com requeijão", "Pão de queijo", "Frutas", "Iogurte natural", "Granola", "Sucrilhos"]
comidas_almoco = ["Carnes Bovinas", "Carnes Suínas", "Frango", "Peixe", "Refrigerante", "Café expresso", "Salada", "Macarrão", "Prato feito"]
comidas_jantar = ["Sanduíche", "Salada", "Prato feito", "Salgados", "Pão com frios", "Sopa"]


print("\nBem-vindo ao FoodFinder, seu ajudante para te dar sugestões de refeições para o seu dia!")
hora_refeicao = input("Por favor, digite o período da refeição (manhã, tarde, noite): ")

def opcoes_cafe_manha():
    print("Opções de café da manhã:\n")
    indice_de_comidas = 1
    for comida in comidas_cafe_manha:
        print(indice_de_comidas, comida)
        indice_de_comidas +=1

def opcoes_almoco():
    print("Opções de almoço:\n")
    indice_de_comidas = 1
    for comida in comidas_almoco:
        print(indice_de_comidas, comida)
        indice_de_comidas +=1

def opcoes_jantar():
    print("Opções de jantar:\n")
    indice_de_comidas = 1
    for comida in comidas_jantar:
        print(indice_de_comidas, comida)
        indice_de_comidas +=1

def gravar_cafe():
    escolha_cafe = input(
        """\nVocê deseja escolher sua opção de café da manhã ou prefere que nosso assistente lhe dê uma sugestão?
1 - Desejo escolher
2 - Quero uma sugestão de café\t"""
    )
    if escolha_cafe == "1":
        logs_escolhas_cafe = []
        escolha = input("Ok! Por favor, digite sua opção de café da mahã:\t")
        logs_escolhas_cafe.append(escolha)
        return logs_escolhas_cafe
    elif escolha_cafe == "2":
        logs_escolhas_cafe = []
        escolha = random.choice(comidas_cafe_manha)
        print(f"Ok! Nossa sugestão de refeição para seu café da manhã é: {escolha}")
        logs_escolhas_cafe.append(escolha)
        return logs_escolhas_cafe
    
def gravar_almoco():
    escolha_almoco = input(
        """\nVocê deseja escolher sua opção de almoço ou deseja uma sugestão de nosso assitente?
1 - Desejo escolher
2 - Quero uma sugestão de almoço\t"""
    )
    if escolha_almoco == "1":
        logs_escolhas_almoco = []
        escolha = input("Ok! Por favor, digite sua opção de almoço:\t")
        logs_escolhas_almoco.append(escolha)
        return logs_escolhas_almoco
    elif logs_escolhas_almoco == "2":
        logs_escolhas_almoco = []
        escolha = random.choice(comidas_almoco)
        print(f"Ok! Nossa sugestão de almoço para você hoje é: {escolha}")
        logs_escolhas_almoco.append(escolha)
        return logs_escolhas_almoco


if hora_refeicao == "manhã" or hora_refeicao == "manha":
    opcoes_cafe_manha()
    cafe = gravar_cafe()
    print(f"\nExcelente! Sua opção de hoje para o café da manhã foi: {cafe}")
elif hora_refeicao == "tarde":
    opcoes_almoco()
    almoco = gravar_almoco()
    print(f"\nExcelente! Sua opção de almoço apra hoje foi: {almoco}")
elif hora_refeicao == "Noite" or hora_refeicao == "noite":
    opcoes_jantar()
else:
    print("Opção Inválida")

