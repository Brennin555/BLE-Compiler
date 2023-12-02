# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = [
    'INICIO', 'FIM', 'LINETERMINATOR', 'NUM', 'TXT', 'VET', 'VF', 'CARACTERE',
    'DIGITO', 'ABREASPAS', 'FECHAASPAS', 'ABRECOLCHETE', 'FECHACOLCHETE',
    'IMP', 'LE', 'ATRIBUIR', 'ATRIBUICAO', 'SE', 'SENAO', 'ENQT', 'PRA',
    'RELACIONAL', 'LOGICO', 'E', 'OU', 'BLOCO', 'SIMBOLO', 'DEFVARIAVEL',
    'TIPO', 'OPERADOR_MAIS', 'OPERADOR_MENOS', 'OPERADOR_DIVISAO', 'VIRGULA',
    'OPERADOR_MULTIPLICACAO', 'ESPACO', 'PONTOEVIRGULA', 'ABREPARTESE',
    'FECHAPARENTESE', 'ABRECHAVE', 'FECHACHAVE', 'QUEBRALINHA', 'COMENTARIOS', 'ID'
]

# Definindo as regras de expressão regular para alguns tokens
t_INICIO = r'main'
t_FIM = r'end'
t_LINETERMINATOR = r'\n'
t_COMENTARIOS = r'\'[^\']*\''
t_NUM = r'\d+'
t_VET = r'vet'
t_VF = r'vf'
t_CARACTERE = r'[a-zA-Z]'
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
t_VIRGULA = r','
#t_DEFVARIAVEL = r' '
t_TIPO = r'txt|num|vet|vf'
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
t_TXT = r'"([^"\\]|\\.)*"'
t_ID = r'[a-z][a-zA-Z0-9]*'

# Ignorar espaços em branco
t_ignore = ' \t'

# Função para lidar com novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# def t_TXT(t):
#     r'"(?:\\"|.)*?"'
#     return t

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
    # print(token)
        # deixar alinhado os dados do print:
    print(
        token.type.ljust(15),
        str(token.value).ljust(15),
        str(token.lineno).ljust(10),
        str(token.lexpos).ljust(10)
    )