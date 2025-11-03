from colorama import init, Fore

PECAS = [
    {
        'id': 1,
        'peso': 100,
        'cor': 'azul',
        'comprimento': 15
    },
    {
        'id': 2,
        'peso': 90,
        'cor': 'vermelho',
        'comprimento': 25
    },
    {
        'id': 3,
        'peso': 97,
        'cor': 'verde',
        'comprimento': 18
    },
    {
        'id': 4,
        'peso': 110,
        'cor': 'azul',
        'comprimento': 12
    },
    {
        'id': 5,
        'peso': 102,
        'cor': 'verde',
        'comprimento': 20
    },
    {
        'id': 6,
        'peso': 85,
        'cor': 'amarelo',
        'comprimento': 15
    },
    {
        'id': 7,
        'peso': 99,
        'cor': 'azul',
        'comprimento': 11
    },
    {
        'id': 8,
        'peso': 105,
        'cor': 'verde',
        'comprimento': 22
    },
    {
        'id': 9,
        'peso': 95,
        'cor': 'azul',
        'comprimento': 19
    }
]

SEQUENCE_ID = len(PECAS)

def exibir_peca(peca):
    status_formatado = Fore.GREEN + "APROVADA" if status_peca(peca) == "Aprovada" else Fore.RED + "REPROVADA"
    print(f"ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm | Status: {status_formatado}")

def salvar_peca(peso, cor, comprimento):
    global SEQUENCE_ID
    SEQUENCE_ID += 1
    peca = {
        'id': SEQUENCE_ID,
        'peso': peso,
        'cor': cor.strip().lower(),
        'comprimento': comprimento
    }
    PECAS.append(peca)
    return peca

def buscar_peca_por_id(id):
    for peca in PECAS:
        if peca['id'] == id:
            return peca

def remover_peca_por_id(id):
    for i, obj in enumerate(PECAS):
        if obj['id'] == id:
            PECAS.pop(i)
            return True
    return False

def listar_todas_pecas():
    for peca in PECAS:
        exibir_peca(peca)

def status_peca(peca):
    resultado = (peca['peso'] >= 95 and peca['peso'] <= 105) and \
                (peca['cor'] == "azul" or peca['cor'] == "verde")  and \
                peca['comprimento'] >= 10 and peca['comprimento'] <= 20
    return "Aprovada" if resultado else "Reprovada"

def listar_pecas_por_status(status):
    return [peca for peca in PECAS if status_peca(peca) == status]
