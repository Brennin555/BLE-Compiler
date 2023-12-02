import ply.yacc as yacc
from lexer import tokens

# Lista de tokens (importada do lexer)
tk = tokens

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
    print("PROGRAMA: ")
    for i in p:
        print(i)

def p_main(p):
    '''
    inicio : INICIO ABRECHAVE operacoes FECHACHAVE
    | INICIO ABRECHAVE
    '''
    print("INICIO: ")
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
    print("TIPO: ")
    for i in p:
        print(i)
    
# def p_num(p):
#     '''
#     num : NUM
#     | NUM VIRGULA NUM
#     '''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[1] + p[2] + p[3]
#         p[0] = p[0].replace(',', '.')
#         p[0] = float(p[0])
        
    
def p_txt(p):
    '''
    txt : TXT
    '''
    p[0] = p[1]
    print(p[0])
    print("TXT: ")
    for i in p:
        print(i)
    
def p_le(p):
    '''
    le : LE ABREPARTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA
       | LE ABREPARTESE ID FECHAPARENTESE
    '''
    print(p[3])
    print("LE: ")
    for i in p:
        print(i)

def p_imp(p):
    '''
    imp : IMP ABREPARTESE expressao FECHAPARENTESE PONTOEVIRGULA
        | IMP ABREPARTESE expressao FECHAPARENTESE
    '''
    print(p[3])
    print("IMP: ")
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
    '''
    print("DECLARACOES: ")
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
    print("DECLARACAO: ")
    for i in p:
        print(i)

def p_atribuir(p):
    '''
    atribuir : ATRIBUIR variavel
             | ATRIBUICAO variavel
             | TIPO ID ATRIBUIR expressao 
    '''
    print("ATRIBUIR: ")
    for i in p:
        print(i)

def p_variavel(p):
    '''
    variavel : ESPACO CARACTERE
    '''
    # Adicione ações conforme necessário
    print("VARIAVEL: ")
    for i in p:
        print(i)
    
def p_operacoes(p):
    '''
    operacoes : expressao SIMBOLO operacoes
              | expressao
              | imp
              | le
    '''
    # Adicione ações conforme necessário
    print("OPERACOES: ",p)
    
def p_expressao(p):
    '''
    expressao : NUM
              | variavel
              | TXT
              | aritimetico
              | ABREPARTESE expressao FECHAPARENTESE                      
    '''
    # | expressao PONTOEVIRGULA expressao
    # | expressao PONTOEVIRGULA
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]
        

    print("EXPRESSAO:")
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