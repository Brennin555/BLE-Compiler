# parser.py
import ply.yacc as yacc
from lexer import tokens, lexer


# Lista de tokens (importada do lexer)
tokens = lexer.tokens

# Definindo precedência dos operadores
precedence = (
    ('left', 'OPERADOR_MAIS', 'OPERADOR_MENOS'),
    ('left', 'OPERADOR_MULTIPLICACAO', 'OPERADOR_DIVISAO'),
)

# Regras de produção e ações
def p_main(p):
    '''
    main : INICIO ABRECHAVE declaracoes operacoes FIM
    '''
    # Aqui você pode executar as ações desejadas para o bloco principal

def p_declaracoes(p):
    '''
    declaracoes : TIPO ESPACO CARACTERE atribuir PONTOEVIRGULA declaracoes
                | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir PONTOEVIRGULA declaracoes
                | ESPACO CARACTERE atribuir PONTOEVIRGULA declaracoes
                | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir PONTOEVIRGULA declaracoes
                | ESPACO CARACTERE atribuir PONTOEVIRGULA
                | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir PONTOEVIRGULA
                | QUEBRALINHA COMENTARIOS QUEBRALINHA declaracoes
                | COMENTARIOS QUEBRALINHA declaracoes
                | QUEBRALINHA COMENTARIOS declaracoes
                | COMENTARIOS declaracoes
    '''
    # Aqui você pode executar as ações desejadas para as declarações

# Adicione outras regras conforme necessário

# ...

# Tratamento de erro sintático
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Criando o analisador sintático
parser = yacc.yacc()
