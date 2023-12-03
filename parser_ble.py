import ply.yacc as yacc
from lexer import tokens

# Lista de tokens (importada do lexer)
tk = tokens
variaveis = []

# Definindo precedência dos operadores
precedence = (
    ('left', 'OPERADOR_MAIS', 'OPERADOR_MENOS'),
    ('left', 'OPERADOR_MULTIPLICACAO', 'OPERADOR_DIVISAO'),
)

# Regras de produção e ações
def p_programa(p):
    '''
    programa : inicio
    '''
    # print("--------------PROGRAMA: ")
    # for i in p:
    #     print(i)

def p_inicio(p):
    '''
    inicio : INICIO ABRECHAVE blocos FECHACHAVE
    '''
    # f = open("ble_code.py", "w")
    # f.write(f"if __name__ == __main__:\n\t{p[3]}\n")
    # f.close()
    print(p[3])

def p_le(p):
    '''
    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA
    '''
    # print("LEITURA DE DADO:")
    # print("Tipo: ", p[3])
    # print("Variavel: ", p[4])
    if p[3] == 'txt':
        p[0] = f'{p[4]} = input()\n'
    elif p[3] == 'num':
        p[0] = f'{p[4]} = float(input())\n'
    elif p[3] == 'vet':
        p[0] = f'{p[4]} = input()\n{p[4]} = {p[4]}.split()\n{p[4]} = [int(valor) for valor in {p[4]}]\n'
    #variaveis[0] = nome variaveis[1] = valor
    # p[4] = input("")
    print("--------------LE: ")
    for i in p:
        print(i)

def p_imp(p):
    '''
    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA
    '''
    p[0] = f'print({p[3]})\n'
    # print("--------------IMP: ")
    # for i in p:
    #     print(i)


def p_blocos(p):
    '''
    blocos : bloco blocos
           | bloco
    '''
    if str(p[0]) == 'None':
        print(f'{p[0]} = {p[1]}')
        p[0] = p[1]
    else:
        print(f'{p[0]} + {p[1]}')
        p[0] = str(p[0]) + p[1]
    # print("--------------BLOCOS: ")
    # for i in p:
    #     print(i)

def p_bloco(p):
    '''
    bloco   : enqt
            | imp
            | le
            | atribuir
            | atribuicao
    '''
    p[0] = p[1]
    # print("--------------BLOCO: ")
    # for i in p:
    #     print(i)
    
def p_expressao(p):
    '''
    expressao : ID
              | NUM
              | aritimetico
              | ABREPARENTESE expressao FECHAPARENTESE
    '''
    # | expressao PONTOEVIRGULA expressao
    # | expressao PONTOEVIRGULA
    if len(p) == 4:
        p[0] = f'({p[2]})'
    else:
        p[0] = p[1]
        

    # print("--------------EXPRESSAO:")
    # for i in p:
    #     print(i)
    
def p_aritimetico(p):
    '''aritimetico  : expressao OPERADOR_DIVISAO expressao
                    | expressao OPERADOR_MULTIPLICACAO expressao
                    | expressao OPERADOR_MAIS expressao
                    | expressao OPERADOR_MENOS expressao
    '''
    match p[2]:
        case '+':
            p[0] = f'{p[1]} + {p[3]}'
        case '-':
            p[0] = f'{p[1]} - {p[3]}'
        case '*':
            p[0] = f'{p[1]} * {p[3]}'
        case '/':
            p[0] = f'{p[1]} / {p[3]}'
        
def p_atribuicao(p):
    '''
    atribuicao : ATRIBUIR expressao
               | ATRIBUIR ABRECOLCHETE lista FECHACOLCHETE   
    '''
    if len(p) == 3:
        p[0] = f'= {p[2]}'
    else:
        p[0] = f'= [{p[2]}]'

def p_lista(p):
    '''
    lista : NUM
          | ID
          | lista VIRGULA lista
    '''
    if len(p) == 2:
        p[0] = f'{p[1]}'
    else:
        p[0] = f'{p[1]} , {p[3]}'

def p_atribuir(p):
    '''
    atribuir : ID atribuicao PONTOEVIRGULA
             | TIPO ID atribuicao PONTOEVIRGULA 
             | TIPO ID ATRIBUIR expressao PONTOEVIRGULA 
    '''
    # print("--------------ATRIBUIR: ")
    # for i in p:
    #     print(i)
       
    variaveis.append({'nome': p[2], 'valor': p[4]})
    #imprimindo apenas valor:
    
    for i in variaveis:
        print("Nome: ", i['nome'], "Valor: ", i['valor'])

def p_condicional(p):
    '''
    condicional : atomica
                | atomica LOGICO atomica
    '''
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = p[1] and p[3]
        else:
            p[0] = p[1] or p[3]
    else:
        p[0] = p[1]
        

def p_condicional_atomica(p):
    '''
    atomica : RESPOSTABOOLEANA
            | ID
            | NUM
            | NAO condicional
            | condicional RELACIONAL condicional
            | condicional LOGICO condicional
    '''
    #se for um id, buscar na lista de variaveis

    tamanho = len(p)
    if tamanho == 2:
        for i in variaveis:
            if i['nome'] == p[1]:
                p[1] = int(i['valor'])

        p[0] = p[1]

    elif tamanho == 3:
        p[0] = not p[1]

    elif tamanho == 4:
        if p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '=':
            p[0] = p[1] = p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
        elif p[2] == '>=':
            p[0] = p[1] > p[3]
        elif p[2] == '<=':
            p[0] = p[1] > p[3]


    
def p_enqt(p):
    ''' 
    enqt : ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE bloco FECHACHAVE
    '''
    # while p[2]:
    #     print(p[6])
    #     break
    while true:
        if (p[2] == False) or (p[2] == 0):
            break
        else:
            p[0] = p[6]
    print("--------------ENQT:")
    for i in p:
        print(i)
# Tratamento de erro sintático
def p_error(p):
    print(f"Erro de sintaxe: Token inesperado '{p.value}' na linha {p.lineno}, coluna {p.lexpos}")

# Adicione as ações e regras conforme necessário

# Criando o analisador sintático
parser = yacc.yacc(debug=True, write_tables=True)

with open('main.ble', 'r') as file:
    code = file.read()

# Fazendo o parser do código
result = parser.parse(code)