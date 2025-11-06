from peca import *

CAIXAS = [
    {
        'id': 1,
        'status': 'aberta',
        'pecas': PECAS.copy()
    }
]

SEQUENCE_ID = len(CAIXAS)
CAPACIDADE_MAXIMA = 10 # Máximo de peças por caixa

def salvar_caixa():
    global SEQUENCE_ID
    SEQUENCE_ID += 1
    caixa = {
        'id': SEQUENCE_ID,
        'status': 'aberta',
        'pecas': []
    }
    CAIXAS.append(caixa)
    return caixa

def criar_nova_caixa(peca):
    caixa = salvar_caixa()
    adicionar_peca_na_caixa(caixa, peca)
    return caixa

def finalizar_caixa(caixa):
    caixa['status'] = 'fechada'

def abrir_caixa(caixa):
    caixa['status'] = 'aberta'

def buscar_caixa_aberta():
    for caixa in CAIXAS:
        if caixa['status'] == 'aberta':
            return caixa    
        
def adicionar_peca_na_caixa(caixa, peca):
    if len(caixa['pecas']) < CAPACIDADE_MAXIMA:
        caixa['pecas'].append(peca)
        if len(caixa['pecas']) == CAPACIDADE_MAXIMA:
            finalizar_caixa(caixa)
        return True
    return False

def exibir_caixa(caixa):
    print(f"Caixa ID: {caixa['id']} | Status: {caixa['status']} | Número de Peças: {len(caixa['pecas'])}")

def listar_caixas_fechadas():
    return [caixa for caixa in CAIXAS if caixa['status'] == 'fechada']
    
def remover_peca_da_caixa(id_peca):
    for caixa in CAIXAS:
        for i, peca in enumerate(caixa['pecas']):
            if peca['id'] == id_peca:
                caixa['pecas'].pop(i)
                abrir_caixa(caixa)
                return True
    return False