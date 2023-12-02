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
    programa : main
    '''
    # Adicione ações conforme necessário

def p_main(p):
    '''
    main : INICIO ABRECHAVE operacoes FECHACHAVE
    '''
    # Adicione ações conforme necessário

def p_imp(p):
    '''
    imp : IMP ABREPARTESE expressao FECHAPARENTESE SIMBOLO
        | IMP ABREPARTESE expressao FECHAPARENTESE
    '''
    # Adicione ações conforme necessário
    strings=str(p[3])
    print(f"{p[3]}")

def p_declaracoes(p):
    '''
    declaracoes : declaracao PONTOEVIRGULA declaracoes
                | QUEBRALINHA declaracoes
                | COMENTARIOS QUEBRALINHA declaracoes
                | QUEBRALINHA COMENTARIOS declaracoes
                | COMENTARIOS
    '''
    # Adicione ações conforme necessário

def p_declaracao(p):
    '''
    declaracao : TIPO ESPACO CARACTERE atribuir
               | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
               | ESPACO CARACTERE atribuir
               | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir
    '''
    # Adicione ações conforme necessário

def p_atribuir(p):
    '''
    atribuir : ATRIBUIR variavel
             | ATRIBUICAO variavel
    '''
    # Adicione ações conforme necessário

def p_variavel(p):
    '''
    variavel : ESPACO CARACTERE
    '''
    # Adicione ações conforme necessário

def p_operacoes(p):
    '''
    operacoes : expressao SIMBOLO operacoes
              | expressao
              | imp
    '''
    # Adicione ações conforme necessário

def p_expressao(p):
    '''
    expressao : NUM
              | variavel
              | TXT
              | ABREASPAS expressao FECHAASPAS
              | expressao OPERADOR_MAIS expressao
              | expressao OPERADOR_MENOS expressao
              | expressao OPERADOR_MULTIPLICACAO expressao
              | expressao OPERADOR_DIVISAO expressao
              | ABREPARTESE expressao FECHAPARENTESE
              | expressao SIMBOLO expressao
              | expressao SIMBOLO
    '''
    p[0]=p[1]
    # Adicione ações conforme necessário

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
