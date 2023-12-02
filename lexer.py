# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = [
    'INICIO', 'FIM', 'LINETERMINATOR', 'NUM', 'TXT', 'VET', 'VF', 'CARACTERE',
    'DIGITO', 'ABREASPAS', 'FECHAASPAS', 'ABRECOLCHETE', 'FECHACOLCHETE',
    'IMP', 'LE', 'ATRIBUIR', 'ATRIBUICAO', 'SE', 'SENAO', 'ENQT', 'PRA',
    'RELACIONAL', 'LOGICO', 'E', 'OU', 'BLOCO', 'SIMBOLO', 'DEFVARIAVEL',
    'TIPO', 'OPERADOR_MAIS', 'OPERADOR_MENOS', 'OPERADOR_DIVISAO',
    'OPERADOR_MULTIPLICACAO', 'ESPACO', 'PONTOEVIRGULA', 'ABREPARTESE',
    'FECHAPARENTESE', 'ABRECHAVE', 'FECHACHAVE', 'QUEBRALINHA', 'COMENTARIOS'
]

# Definindo as regras de expressão regular para alguns tokens
t_INICIO = r'main'
t_FIM = r'end'
t_LINETERMINATOR = r'\n'
t_NUM = r'\d+'
t_TXT = r'"[^"]*"'
t_VET = r'vet'
t_VF = r'vf'
t_CARACTERE = r'car'
t_DIGITO = r'\d'
t_ABREASPAS = r'"'
t_FECHAASPAS = r'"'
t_ABRECOLCHETE = r'\['
t_FECHACOLCHETE = r'\]'
t_IMP = r'imp'
t_LE = r'le'
t_ATRIBUIR = r':'
t_ATRIBUICAO = r'='
t_SE = r'if'
t_SENAO = r'else'
t_ENQT = r'while'
t_PRA = r'for'
t_RELACIONAL = r'[<>=!]=?'
t_LOGICO = r'[&|]'
t_E = r'&&'
t_OU = r'\|\|'
t_BLOCO = r'\(\)'
t_SIMBOLO = r'[;,.]'
t_DEFVARIAVEL = r'txt|num|vet|vf'
t_TIPO = r'int|float|string|bool'
t_OPERADOR_MAIS = r'\+'
t_OPERADOR_MENOS = r'-'
t_OPERADOR_DIVISAO = r'/'
t_OPERADOR_MULTIPLICACAO = r'\*'
t_ESPACO = r'\s+'
t_PONTOEVIRGULA = r';'
t_ABREPARTESE = r'\('
t_FECHAPARENTESE = r'\)'
t_ABRECHAVE = r'\{'
t_FECHACHAVE = r'\}'
t_QUEBRALINHA = r'\/\/'
t_COMENTARIOS = r'/\*.*\*/'


ABREASPAS = r'"'
ABREPARTESE = r'\('
ATRIBUICAO = r'='
ATRIBUIR = r':'
BLOCO = r'\(\)'
DEFVARIAVEL = r'defvariavel'
DIGITO = r'\d'
E = r'&&'
ENQT = r'enqt'
FECHAASPAS = r'"'
FECHACHAVE = r'\}'
FECHAPARENTESE = r'\)'
IMP = r'imp'
LE = r'le'
LINETERMINATOR = r';'
LOGICO = r'[&|]'
OPERADOR_DIVISAO = r'/'
OPERADOR_MAIS = r'\+'
OPERADOR_MENOS = r'-'
OPERADOR_MULTIPLICACAO = r'\*'
OU = r'\|\|'
PRA = r'pra'
QUEBRALINHA = r'\/\/'
RELACIONAL = r'[<>=!]=?'
SE = r'se'
SENAO = r'senao'
SIMBOLO = r'[+,.\-;]'
TXT = r'txt'
VET = r'vet'
VF = r'vf'


# Ignorar espaços em branco
t_ignore = ' \t'

# Função para lidar com novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função para lidar com erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Criando o analisador léxico
lexer = lex.lex()

with open('main.ble', 'r') as file:
    input_string = file.read()

lexer.input(input_string)

# Agora você pode iterar sobre os tokens diretamente
for token in lexer:
    print(token)