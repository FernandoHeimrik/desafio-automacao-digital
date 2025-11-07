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
        'cor': 'azul',
        'comprimento': 20
    },
    {
        'id': 3,
        'peso': 97,
        'cor': 'verde',
        'comprimento': 18
    },
    {
        'id': 4,
        'peso': 105,
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
        'peso': 99,
        'cor': 'azul',
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
        'comprimento': 20
    },
    {
        'id': 9,
        'peso': 95,
        'cor': 'azul',
        'comprimento': 19
    }
]

SEQUENCE_ID = len(PECAS)

PESO_MINIMO = 95
PESO_MAXIMO = 105
CORES_VALIDAS = ['azul', 'verde']
COMPRIMENTO_MINIMO = 10
COMPRIMENTO_MAXIMO = 20    


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
    resultado = validar_peso(peca) and \
                validar_cor(peca)  and \
                validar_comprimento(peca)
    return "Aprovada" if resultado else "Reprovada"

def listar_pecas_por_status(status):
    return [peca for peca in PECAS if status_peca(peca) == status]

def validar_peso(peca):
    return peca['peso'] >= PESO_MINIMO and peca['peso'] <= PESO_MAXIMO

def validar_cor(peca):
    return CORES_VALIDAS.count(peca['cor']) > 0

def validar_comprimento(peca):
    return peca['comprimento'] >= COMPRIMENTO_MINIMO and peca['comprimento'] <= COMPRIMENTO_MAXIMO

def identificar_motivo_reprovacao(peca):
    motivos = []
    if not validar_peso(peca):
        motivos.append(f"Peso {Fore.RED + str(peca['peso']) + Fore.RESET} fora do intervalo ({PESO_MINIMO}-{PESO_MAXIMO})")
    if not validar_cor(peca):
        motivos.append(f"Cor {Fore.RED + peca['cor'] + Fore.RESET} inválida (deve ser {', '.join(CORES_VALIDAS)})")
    if not validar_comprimento(peca):
        motivos.append(f"Comprimento {Fore.RED + str(peca['comprimento']) + Fore.RESET} fora do intervalo ({COMPRIMENTO_MINIMO}-{COMPRIMENTO_MAXIMO})")
    return motivos