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
    print("--------------PROGRAMA: ")
    for i in p:
        print(i)

def p_inicio(p):
    '''
    inicio : INICIO ABRECHAVE operacoes FECHACHAVE
    '''
    print("--------------INICIO: ")
    for i in p:
        print(i)
                
def p_tipo(p):
    '''
    tipo : TXT
         | NUM
    '''
    # Adicione ações conforme necessário
    p[0] = p[1]
    print("O TIPO EH: ",p[0])
    print("--------------TIPO: ")
    for i in p:
        print(i)
          
def p_txt(p):
    '''
    txt : TXT
    '''
    p[0] = p[1]
    print(p[0])
    print("--------------TXT: ")
    for i in p:
        print(i)
    
# def p_senao(p):
#     '''
#     senao : SENAO ABRECHAVE operacoes FECHACHAVE
#     '''
#     print("--------------SENAO: ")
#     for i in p:
#         print(i)
      
# def p_se(p):
#     '''
#     se : SE ABREPARENTESE expressao FECHAPARENTESE ABRECHAVE operacoes FECHACHAVE
#        | SE ABREPARENTESE expressao FECHAPARENTESE ABRECHAVE operacoes FECHACHAVE senao
#        | SE ABREPARENTESE ID RELACIONAL NUM FECHAPARENTESE ABRECHAVE imp FECHACHAVE
#        | SE ABREPARENTESE ID relacional ID FECHAPARENTESE ABRECHAVE imp FECHACHAVE
#     '''
#     # p[0] = (p[2], p[4])
#     print("--------------SE: ")
#     for i in p:
#         print(i)
    
def p_le(p):
    '''
    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA
       | LE ABREPARENTESE ID FECHAPARENTESE
    '''
    print("LEITURA DE DADO:")
    print("Tipo: ", p[3])
    print("Variavel: ", p[4])
    
    #variaveis[0] = nome variaveis[1] = valor
    p[4] = input("")
    print("--------------LE: ")
    for i in p:
        print(i)

def p_imp(p):
    '''
    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA
        | IMP ABREPARENTESE expressao FECHAPARENTESE
    '''
    print(p[3])
    print("--------------IMP: ")
    for i in p:
        print(i)

def p_declaracoes(p):
    '''
    declaracoes : declaracao PONTOEVIRGULA declaracoes
                | QUEBRALINHA declaracoes
                | COMENTARIOS QUEBRALINHA declaracoes
                | QUEBRALINHA COMENTARIOS declaracoes
                | COMENTARIOS
                | TIPO ID ATRIBUIR expressao PONTOEVIRGULA
                | TIPO ID ATRIBUICAO declaracao PONTOEVIRGULA
                | TIPO ID ATRIBUIR TXT
    '''
    print("--------------DECLARACOES: ")
    for i in p:
        print(i)

def p_declaracao(p):
    '''
    declaracao : TIPO ESPACO CARACTERE atribuir
               | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
               | ESPACO CARACTERE atribuir
               | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
               | tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA
               | tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA
               
                 
    '''
    print("--------------DECLARACAO: ")
    for i in p:
        print(i)

def p_variavel(p):
    '''
    variavel : ESPACO CARACTERE
    '''
    # Adicione ações conforme necessário
    print("--------------VARIAVEL: ")
    for i in p:
        print(i)
    
def p_operacoes(p):
    '''
    operacoes :
              | expressao
              | imp
              | le
              | atribuir
              | atribuicao
              | operacoes
    '''
    # Adicione ações conforme necessário
    print("--------------OPERACOES: ")
    for i in p:
        print(i)
    
def p_expressao(p):
    '''
    expressao : NUM
              | variavel
              | ID
              | TXT
              | aritimetico
              | ABREPARENTESE expressao FECHAPARENTESE
              | RESPOSTABOOLEANA
              
                         
    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]
    print("--------------EXPRESSAO:")
    for i in p:
        print(i)
    
def p_aritimetico(p):
    '''aritimetico  : expressao OPERADOR_DIVISAO expressao
                    | expressao OPERADOR_MULTIPLICACAO expressao
                    | expressao OPERADOR_MAIS expressao
                    | expressao OPERADOR_MENOS expressao
    '''
    if p[2] == '+':
        p[0] = float(p[1]) + float(p[3])
    elif p[2] == '-':
        p[0] = float(p[1]) - float(p[3])
    elif p[2] == '*':
        p[0] = float(p[1]) * float(p[3])
    elif p[2] == '/':
        p[0] = float(p[1]) /  float(p[3])
    print("ARITIMETICO: ",p)
    for i in p:
        print(i)
        
def p_atribuicao(p):
    '''
    atribuicao : ATRIBUIR expressao
               | ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE   
    '''

def p_atribuir(p):
    '''
    atribuir : TIPO ID atribuicao PONTOEVIRGULA 
             | TIPO ID ATRIBUIR expressao PONTOEVIRGULA 
             | ID atribuicao PONTOEVIRGULA
             
    '''
    print("--------------ATRIBUIR: ")
    for i in p:
        print(i)
        
    variaveis.append({'nome': p[2], 'valor': p[4]})
    #imprimindo apenas valor:
    print(variaveis[0]['valor'])
    
    print("Variáveis: ", variaveis)

def p_bloco(p):
    '''
    bloco   : enqt
            | imp
            | bloco
    '''
    # p[0] = p[1]

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
            | NUM
            | ID
            | NAO condicional
            | condicional RELACIONAL condicional
            | condicional LOGICO condicional
    '''
    tamanho = len(p)
    if tamanho == 2:
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