#parser_ble.py
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

def p_main(p):
    '''
    inicio : INICIO ABRECHAVE bloco FECHACHAVE
    '''
                
def p_tipo(p):
    '''
    tipo : TXT
         | NUM
    '''
    # Adicione ações conforme necessário
    p[0] = p[1]

          
def p_txt(p):
    '''
    txt : TXT
    '''
    p[0] = p[1]
    
def p_le(p):
    '''
    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA
       | LE ABREPARENTESE ID FECHAPARENTESE
    ''' 
    #variaveis[0] = nome variaveis[1] = valor
    p[4] = input("")

def p_imp(p):
    '''
    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA
        | IMP ABREPARENTESE expressao FECHAPARENTESE
    '''
    print(p[3])


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

def p_declaracao(p):
    '''
    declaracao : TIPO ESPACO CARACTERE atribuir
               | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
               | ESPACO CARACTERE atribuir
               | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
               | tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA
               | tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA
               
                 
    '''

def p_variavel(p):
    '''
    variavel : ESPACO CARACTERE
    '''
    # Adicione ações conforme necessário
    
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
    # | expressao PONTOEVIRGULA expressao
    # | expressao PONTOEVIRGULA
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]
    
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
    variaveis.append({'nome': p[2], 'valor': p[4]})
    print(variaveis[0]['valor'])

def p_incremento(p):
    '''
    incremento : ID OPERADOR_MAIS NUM
               | ID OPERADOR_MENOS NUM
    '''

def p_pra(p):
    '''
    pra : PRA ABREPARENTESE ID ESPACO incremento FECHAPARENTESE ABRECHAVE bloco FECHACHAVE
    '''


def p_bloco(p):
    '''
    bloco   : imp
            | pra
            | le
            | atribuir
            | atribuicao
            | expressao PONTOEVIRGULA bloco
            | expressao PONTOEVIRGULA
            
    '''
    p[0] = p[1]
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