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
    inicio : INICIO ABRECHAVE blocos FECHACHAVE
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

def p_variavel(p):
    '''
    variavel : ESPACO CARACTERE
    '''
    # Adicione ações conforme necessário
    print("--------------VARIAVEL: ")
    for i in p:
        print(i)

def p_blocos(p):
    '''
    blocos : bloco blocos
           | bloco
    '''
    print("--------------BLOCOS: ")
    for i in p:
        print(i)

def p_bloco(p):
    '''
    bloco : expressao
             | imp
             | le
             | atribuir
             | atribuicao
    '''
    print("--------------BLOCO: ")
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
    # | expressao PONTOEVIRGULA expressao
    # | expressao PONTOEVIRGULA
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
    # for i in variaveis:
    #     if i['nome'] == p[2]:
    #         i['valor'] = p[4]
    #         print("Valor de", i['nome'], "atualizado para ", i['valor'])
    #     else:
    #         variaveis.append({'nome': p[2], 'valor': p[4]})
    variaveis.append({'nome': p[2], 'valor': p[4]})
    #imprimindo apenas valor:
    print(variaveis[0]['valor'])
    
    for i in variaveis:
        print("Nome: ", i['nome'], "Valor: ", i['valor'])
    
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