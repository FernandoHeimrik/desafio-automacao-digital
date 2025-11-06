# desafio-automacao-digital

Sistema de automação digital para controle de qualidade industrial. Realiza inspeção automatizada de peças (peso, cor, comprimento), armazenamento inteligente em caixas e geração de relatórios consolidados. Projeto acadêmico desenvolvido em Python.

## Funcionalidades

- **Cadastro de Peças**: Registro de novas peças com peso, cor e comprimento
- **Validação Automática**: Sistema de controle de qualidade que aprova/reprova peças baseado em critérios específicos
- **Gestão de Caixas**: Armazenamento automático de peças aprovadas em caixas com capacidade máxima de 10 unidades
- **Consulta de Peças**: Listagem de peças aprovadas e reprovadas
- **Remoção de Peças**: Exclusão de peças do sistema com atualização automática das caixas
- **Relatórios**: Geração de relatórios consolidados com estatísticas de produção e qualidade

## Critérios de Validação

Uma peça é **aprovada** quando atende TODOS os seguintes requisitos:

| Parâmetro | Critério |
|-----------|----------|
| **Peso** | Entre 95g e 105g |
| **Cor** | Azul ou Verde |
| **Comprimento** | Entre 10cm e 20cm |

Peças que não atendem qualquer um dos critérios são automaticamente **reprovadas**.

## Pré-requisitos

- Python 3.11.9 ou superior
- Biblioteca `colorama` para formatação colorida do terminal

## Como Instalar e Executar

### Passo 1: Instalar o Python

Certifique-se de ter o Python instalado em seu sistema. Verifique com:

```bash
python --version
```

ou

```bash
python3 --version
```

### Passo 2: Instalar Dependências

Instale a biblioteca `colorama`:

```bash
pip install colorama
```

ou

```bash
pip3 install colorama
```

### Passo 3: Organizar os Arquivos

Certifique-se de que todos os arquivos estejam no mesmo diretório:

```
projeto/
│
├── sistema_controle_qualidade.py          # Arquivo principal
├── peca.py                                # Módulo de gerenciamento de peças
├── caixa.py                               # Módulo de gerenciamento de caixas
```

### Passo 4: Executar o Programa

No terminal, navegue até o diretório do projeto e execute:

```bash
python sistema_controle_qualidade.py
```

ou

```bash
python3 sistema_controle_qualidade.py
```

## Estrutura do Menu Principal

```
================= Sistema de controle de produção e qualidade das peças fabricadas =================
====================================================================================================
1.  Cadastrar nova peça
2.  Listar peças aprovadas/reprovadas
3.  Remover peça cadastrada
4.  Listar caixas fechadas 
5.  Gerar relatório final
0.  Sair
====================================================================================================
Escolha uma opção:
```

## 📝 Exemplos de Uso

### Exemplo 1: Cadastrar Peça Aprovada

**Entrada:**
```
Escolha uma opção: 1
Escolha uma opção: 1
Informe o peso da peça (g): 100
Informe a cor da peça: azul
Informe o comprimento da peça em cm: 15
```

**Saída:**
```
Peça cadastrada com sucesso!
ID: 10 | Peso: 100g | Cor: azul | Comprimento: 15cm | Status: APROVADA
Peça aprovada no controle de qualidade!
Peça adicionada na caixa ID: 1
Pressione Enter para continuar...
```

### Exemplo 2: Cadastrar Peça Reprovada (Peso Fora do Padrão)

**Entrada:**
```
Escolha uma opção: 1
Escolha uma opção: 1
Informe o peso da peça (g): 120
Informe a cor da peça: azul
Informe o comprimento da peça em cm: 15
```

**Saída:**
```
Peça cadastrada com sucesso!
ID: 11 | Peso: 120g | Cor: azul | Comprimento: 15cm | Status: REPROVADA
Peça reprovada no controle de qualidade!
Pressione Enter para continuar...
```

### Exemplo 3: Cadastrar Peça Reprovada (Cor Inválida)

**Entrada:**
```
Escolha uma opção: 1
Escolha uma opção: 1
Informe o peso da peça (g): 100
Informe a cor da peça: vermelho
Informe o comprimento da peça em cm: 15
```

**Saída:**
```
Peça cadastrada com sucesso!
ID: 12 | Peso: 100g | Cor: vermelho | Comprimento: 15cm | Status: REPROVADA
Peça reprovada no controle de qualidade!
Pressione Enter para continuar...
```

### Exemplo 4: Listar Peças Aprovadas

**Entrada:**
```
Escolha uma opção: 2
Escolha uma opção: 1
```

**Saída:**
```
ID: 1 | Peso: 100g | Cor: azul | Comprimento: 15cm | Status: APROVADA
ID: 3 | Peso: 97g | Cor: verde | Comprimento: 18cm | Status: APROVADA
ID: 5 | Peso: 102g | Cor: verde | Comprimento: 20cm | Status: APROVADA
ID: 7 | Peso: 99g | Cor: azul | Comprimento: 11cm | Status: APROVADA
ID: 9 | Peso: 95g | Cor: azul | Comprimento: 19cm | Status: APROVADA
ID: 10 | Peso: 100g | Cor: azul | Comprimento: 15cm | Status: APROVADA
Pressione Enter para continuar...
```

### Exemplo 5: Listar caixas fechadas

**Entrada:**
```
Escolha uma opção: 4
Escolha uma opção: 1
```

**Saída:**
```
Caixa ID: 1 | Status: fechada | Número de Peças: 10
Pressione Enter para continuar...
```


### Exemplo 6: Remover Peça

**Entrada:**
```
Escolha uma opção: 3
Escolha uma opção: 1
ID: 1 | Peso: 100g | Cor: azul | Comprimento: 15cm | Status: APROVADA
ID: 2 | Peso: 90g | Cor: vermelho | Comprimento: 25cm | Status: REPROVADA
ID: 3 | Peso: 97g | Cor: verde | Comprimento: 18cm | Status: APROVADA
ID: 4 | Peso: 110g | Cor: azul | Comprimento: 12cm | Status: REPROVADA
ID: 5 | Peso: 102g | Cor: verde | Comprimento: 20cm | Status: APROVADA
ID: 6 | Peso: 85g | Cor: amarelo | Comprimento: 15cm | Status: REPROVADA
ID: 7 | Peso: 99g | Cor: azul | Comprimento: 11cm | Status: APROVADA
ID: 8 | Peso: 105g | Cor: verde | Comprimento: 22cm | Status: REPROVADA
ID: 9 | Peso: 95g | Cor: azul | Comprimento: 19cm | Status: APROVADA
ID: 10 | Peso: 100g | Cor: azul | Comprimento: 15cm | Status: APROVADA
ID: 11 | Peso: 120g | Cor: azul | Comprimento: 15cm | Status: REPROVADA
ID: 12 | Peso: 100g | Cor: vermelho | Comprimento: 15cm | Status: REPROVADA
Informe o ID da peça que deseja remover: 5
```

**Saída:**
```
Peça removida de uma caixa fechada. Caixa reaberta para novas peças.
Peça removida com sucesso!
Pressione Enter para continuar...
```

### Exemplo 7: Gerar Relatório Consolidado

**Entrada:**
```
Escolha uma opção: 5
Escolha uma opção: 1
```

**Saída:**
```
====================================== Relatório Consolidado =======================================
====================================================================================================
Total de Caixas Fechadas: 1
Total de Peças Aprovadas: 10
Total de Peças Reprovadas: 6
====================================================================================================
Motivos de Reprovação:
Peça ID: 2 - Peso 90 fora do intervalo (95-105), Cor vermelho inválida (deve ser azul, verde), Comprimento 25 fora do intervalo (10-20)
Peça ID: 4 - Peso 110 fora do intervalo (95-105)
Peça ID: 6 - Peso 85 fora do intervalo (95-105), Cor amarelo inválida (deve ser azul, verde)
Peça ID: 8 - Comprimento 22 fora do intervalo (10-20)
Peça ID: 11 - Peso 120 fora do intervalo (95-105)
Peça ID: 12 - Cor vermelho inválida (deve ser azul, verde)
Pressione Enter para continuar...
```

