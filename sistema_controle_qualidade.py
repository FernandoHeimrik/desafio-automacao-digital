import os
import time

from datetime import date
from colorama import init, Fore
from peca import *
from caixa import *

## Funções auxiliares
def mensagem_sucesso(texto):
    print(Fore.GREEN + texto)
    time.sleep(2)

def mensagem_erro(texto):
    print(Fore.RED + texto)
    time.sleep(2)

def mensagem_aviso(texto):
    print(Fore.YELLOW + texto)
    time.sleep(2)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    limpar_terminal()
    print(titulo.center(100,'='))
    print("".center(100,'='))

def selecionar_opcao():
    print("".center(100,'='))
    return int(input("Escolha uma opção: "))

def pausar():
    input("Pressione Enter para continuar...")

# Funções do sistema de controle de qualidade

def listar_pecas(status):
    pecas = listar_pecas_por_status(status)
    if not pecas:
        mensagem_aviso(f"Nenhuma peça {status.lower()} encontrada!")
    for peca in pecas:
        exibir_peca(peca)

def cadastrar_peca():
    peso = int(input("Informe o peso da peça (g): "))
    cor = input("Informe a cor da peça: ")
    comprimento = int(input("Informe o comprimento da peça em cm: "))
    peca = salvar_peca(peso, cor, comprimento)
    if peca:
        mensagem_sucesso("Peça cadastrada com sucesso!")
        exibir_peca(peca)
        return peca
    else:
        mensagem_erro("Erro ao cadastrar peça!")
    return None

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

def menu_listar_caixas_fechadas():

    while True:

        exibir_cabecalho(" Consulta de Caixas de Armazenamento ")
        print("1.  Listar todas as caixas fechadas")
        print("0.  Voltar")

        try:
            opcao = selecionar_opcao()
            match (opcao):
                case 1:
                    caixas = listar_caixas_fechadas()
                    if not caixas:
                        mensagem_erro("Nenhuma caixa fechada encontrada!")
                    for caixa in caixas:
                        exibir_caixa(caixa)


                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
            pausar()
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
                    listar_todas_pecas()
                    id_peca = int(input("Informe o ID da peça que deseja remover: "))
                    remover = remover_peca_por_id(id_peca)
                    if remover:
                        excluida_caixa = remover_peca_da_caixa(id_peca)
                        if excluida_caixa:
                            mensagem_aviso("Peça removida de uma caixa fechada. Caixa reaberta para novas peças.")
                        mensagem_sucesso("Peça removida com sucesso!")
                    else:
                        mensagem_erro("Peça não encontrada!")
                    
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 1!')
                    time.sleep(2)
            pausar()
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
                    listar_pecas("Aprovada")
                case 2:
                    listar_pecas("Reprovada")
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    print('Digite valores numéricos entre 0 e 2!')
                    time.sleep(2)
            pausar()
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
                    peca = cadastrar_peca()
                    if peca:
                        status = status_peca(peca)
                        if status == "Aprovada":
                            mensagem_aviso("Peça aprovada no controle de qualidade!")
                            caixa = buscar_caixa_aberta()
                            if caixa:
                                adicionou = adicionar_peca_na_caixa(caixa, peca)
                                if adicionou:
                                    mensagem_sucesso(f"Peça adicionada na caixa ID: {caixa['id']}")
                                else:
                                    nova_caixa = criar_nova_caixa(peca)
                                    mensagem_sucesso(f"Caixa ID: {caixa['id']} estava cheia. Nova caixa ID: {nova_caixa['id']} criada e peça adicionada.")
                            else:
                                nova_caixa = criar_nova_caixa(peca)
                                mensagem_sucesso(f"Nenhuma caixa aberta. Nova caixa ID: {nova_caixa['id']} criada e peça adicionada.")
                        else:
                            mensagem_aviso("Peça reprovada no controle de qualidade!")
                    pausar()

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
                    menu_listar_caixas_fechadas()
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

init(autoreset=True)

menu_principal()

    