import os
import time
from datetime import date

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    limpar_terminal()
    print(titulo.center(100,'='))
    print("".center(100,'='))

def selecionar_opcao():
    print("".center(100,'='))
    return int(input("Escolha uma opção: "))

def gerar_relatorio():

    while True:

        exibir_cabecalho(" Relatório de Produção e Qualidade ")
        print("1.  Gerar relatório")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    # TODO: Adicionar geração de relatorio
                    break
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

def listar_caixas_fechadas():

    while True:

        exibir_cabecalho(" Consulta de Caixas de Armazenamento ")
        print("1.  Listar todas as caixas fechadas")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    # TODO: Adicionar listar caixas fechadas
                    break
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

def menu_remover_peca():

    while True:

        exibir_cabecalho(" Remover Peça do Sistema ")
        print("1.  Remover peça")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    # TODO: Adicionar remover peça
                    break
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

def menu_listar_pecas():

    while True:

        exibir_cabecalho(" Visualizar Peças Cadastradas ")
        print("1.  Listar peças aprovadas")
        print("2.  Listar peças reprovadas")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    # TODO: Adicionar Listar peças aprovadas
                    break
                case 2:
                    # TODO: Adicionar Listar peças reprovadas
                    break
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 2!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

def menu_cadastrar_peca():

    while True:

        exibir_cabecalho(" Registrar Nova Peça ")
        print("1.  Cadastrar peça")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    # TODO: Adicionar cadastro de peças
                    break
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

def menu_principal():

    while True:

        exibir_cabecalho(" Sistema de controle de produção e qualidade das peças fabricadas ")
        print("1.  Cadastrar nova peça")
        print("2.  Listar peças aprovadas/reprovadas")
        print("3.  Remover peça cadastrada")
        print("4.  Listar caixas fechadas ")
        print("5.  Gerar relatório final")
        print("0.  Sair")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    menu_cadastrar_peca()
                case 2:
                    menu_listar_pecas()
                case 3:
                    menu_remover_peca()
                case 4:
                    listar_caixas_fechadas()
                case 5:
                    gerar_relatorio()
                case 0:
                    print("Saindo do programa!")
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 5!')
                    time.sleep(2)
        except ValueError:
            print('Os valores devem ser números inteiros!')
            time.sleep(2)

# Inicio Programa

menu_principal()

    