# lexer.py
import ply.lex as lex

# Definindo os tokens (símbolos a serem reconhecidos)
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Regras para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Ignorando espaços em branco e tabulações
t_ignore = ' \t'

# Regra para números inteiros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Criando o analisador léxico
lexer = lex.lex()

# Testando o analisador léxico
data = "3 + 4 * 5"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
