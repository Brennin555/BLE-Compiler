# calc.py
import ply.lex as lex
import ply.yacc as yacc

# Definindo os tokens (símbolos a serem reconhecidos)
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    
    'NUM'
    'TXT'
    #'ESPACO'
    
    'VET'
    'VF'
    # 'DEFVARIAVEL'
    # 'IMP'
    # 'LE'
    # 'CONDICIONAL'
    # 'ENQT'
    # 'PRA'
    # 'C'
    # 'CNN'
    # 'BLOCO'
    # 'ATRIBUICAO'
    # 'OPERACAO'
    # 'VERDADEIRO'
    # 'FALSO'
    # 'MAIN'
    # 'COMENTARIO'
)

# Regras para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


# Regra para o token ESPACO
#t_ESPACO = r'\s+'

# Ignorando espaços em branco e tabulações
t_ignore = ' \t'

#regras para o token NUM
def t_NUM(t):
    r'-?\d+(\.\d+)?'  # Pode ser um número inteiro ou decimal, positivo ou negativo
    t.value = float(t.value)  # Convertendo para float para representar números decimais
    return t

# Regras para o token TXT
def t_TXT(t):
    r'(\'[^\']*\'|\"[^\"]*\")|[a-zA-Z0-9]'
    t.value = t.value.strip('\'\"')  # Removendo as aspas se presentes
    return t

# Regras para o token VET
def t_VET(t):
    r'\[\s*((\d+(\.\d+)?)\s*)*(\d+(\.\d+)?)?\s*\]'
    t.value = [float(num) if '.' in num else int(num) for num in t.value.split()]
    return t

# Regras para o token VF
def t_VF(t):
    r'Verdadeiro|Falso'
    t.value = True if t.value == 'Verdadeiro' else False
    return t

# # Regras para o token DEFVARIAVEL
# def t_DEFVARIAVEL(t):
#     r'def'
#     return t

# # Regras para o token IMP
# def t_IMP(t):
#     r'imp'
#     return t

# # Regras para o token LE
# def t_LE(t):
#     r'le'
#     return t

# # Regras para o token CONDICIONAL
# def t_CONDICIONAL(t):
#     r'condicional'
#     return t

# # Regras para o token ENQT
# def t_ENQT(t):
#     r'enqt'
#     return t

# # Regras para o token PRA
# def t_PRA(t):
#     r'pra'
#     return t

# # Regras para o token C
# def t_C(t):
#     r'c'
#     return t

# # Regras para o token CNN
# def t_CNN(t):
#     r'cnn'
#     return t

# # Regras para o token BLOCO
# def t_BLOCO(t):
#     r'bloco'
#     return t

# # Regras para o token ATRIBUICAO
# def t_ATRIBUICAO(t):
#     r'='
#     return t

# # Regras para o token OPERACAO
# def t_OPERACAO(t):
#     r'operacao'
#     return t

# # Regras para o token VERDADEIRO
# def t_VERDADEIRO(t):
#     r'verdadeiro'
#     return t

# # Regras para o token FALSO
# def t_FALSO(t):
#     r'falso'
#     return t

# # Regras para o token MAIN
# def t_MAIN(t):
#     r'main'
#     return t

# # Regra para comentários
# def t_COMENTARIO(t):
#     r'\#.*'
#     pass













# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Criando o analisador léxico
lexer = lex.lex()

# Regras de precedência
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regra para a expressão
def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

# Regra para o termo
def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

# Regra para o fator
def p_factor(p):
    '''
    factor : NUM
           | TXT
           | VET
           | VF
    '''
    p[0] = p[1]

# Tratamento de erros
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Criando o analisador sintático
parser = yacc.yacc()

# Testando o analisador com uma expressão
data = "[ 1 + 2.5 * 3 ]"
result = parser.parse(data)
print("Resultado:", result)
