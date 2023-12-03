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
    inicio : INICIO ABRECHAVE blocos FECHACHAVE
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
    p[0] = p[3]
    print(p[3])

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
    # for i in variaveis:
    #     print("Nome: ", i['nome'], "Valor: ", i['valor'])

def p_incremento(p):
    '''
    incremento : ID OPERADOR_MAIS NUM
               | ID OPERADOR_MENOS NUM
               | ID OPERADOR_MAIS ID
               | ID OPERADOR_MENOS ID
    '''

def p_blocos(p):
    '''
    blocos : bloco blocos
           | bloco
    '''

def p_bloco(p):
    '''
    bloco   : imp
            | pra
            | le
            | atribuir
            | atribuicao
            | expressao
    '''
    p[0] = p[1]

def p_pra(p):
    '''
    pra : PRA ABREPARENTESE ID expressao expressao FECHAPARENTESE ABRECHAVE bloco FECHACHAVE
    '''
    inc=int(p[5])
    final=int(p[4])

    for x in variaveis:
       if(x['nome'] == p[3]):
          inicio=int(x['valor']) 
    for i in range(inicio,final,inc):
        print(p[8])

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