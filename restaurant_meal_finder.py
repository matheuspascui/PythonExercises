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


comidas_cafe_manha = ["Pão na chapa", "Café com leite", "Pão com requeijão", "Pão de queijo", "Frutas", "Iogurte natural", "Granola", "Sucrilhos"]
comidas_almoco = ["Carnes Bovinas", "Carnes Suínas", "Frango", "Peixe", "Refrigerante", "Café expresso", "Salada", "Macarrão", "Prato feito", "Strogonoff", "Pastel e Caldo de cana"]
comidas_jantar = ["Sanduíche", "Salada", "Prato feito", "Salgados", "Pão com frios", "Sopa", "Salgados fritos"]


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
2 - Quero uma sugestão de café """
    )
    if escolha_cafe == "1":
        escolha = input("Ok! Por favor, digite sua opção de café da mahã: ")
        return escolha
    elif escolha_cafe == "2":
        escolha = random.choice(comidas_cafe_manha)
        print(f"Ok! Nossa sugestão de refeição para seu café da manhã é: {escolha}")
        return escolha
    
def gravar_almoco():
    escolha_almoco = input(
        """\nVocê deseja escolher sua opção de almoço ou deseja uma sugestão de nosso assitente?
1 - Desejo escolher
2 - Quero uma sugestão de almoço """
    )
    if escolha_almoco == "1":
        escolha = input("Ok! Por favor, digite sua opção de almoço: ")
        return escolha
    elif escolha_almoco == "2":
        escolha = random.choice(comidas_almoco)
        print(f"Ok! Nossa sugestão de almoço para você hoje é: {escolha}")
        return escolha

def gravar_jantar():
    escolha_jantar = input(
        """\nVocê deseja escolher sua opção de almoço ou deseja uma sugestão de nosso assitente?
1 - Desejo escolher
2 - Quero uma sugestão de jantar """
    )
    if escolha_jantar == "1":
        escolha = input("Ok! Por favor, digite sua opção de jantar: ")
        return escolha
    elif escolha_jantar == "2":
        escolha = random.choice(comidas_almoco)
        print(f"Ok! Nossa sugestão de jantar para você hoje é: {escolha}")
        return escolha

def main():
    print("\nBem-vindo ao FoodFinder, seu ajudante para te dar sugestões de refeições para o seu dia!")
    hora_refeicao = input("Por favor, digite o período da refeição (manhã, tarde, noite): ")
    if hora_refeicao == "manhã" or hora_refeicao == "manha":
        opcoes_cafe_manha()
        cafe = gravar_cafe()
        print(f"\nFinalizamos seu atendimento.\nSua opção para o dia de hoje foi: {cafe}\n")
    elif hora_refeicao == "tarde":
        opcoes_almoco()
        almoco = gravar_almoco()
        print(f"\nFinalizamos seu atendimento.\nSua opção para o dia de hoje foi: {almoco}\n")
    elif hora_refeicao == "Noite" or hora_refeicao == "noite":
        opcoes_jantar()
        jantar = gravar_jantar()
        print(f"\nFinalizamos seu atendimento.\nSua opção para o dia de hoje foi: {jantar}\n")
    else:
        print("Opção Inválida")

main()