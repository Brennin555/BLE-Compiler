# lexer.py
import ply.lex as lex

reserved_words = {
    'main': 'INICIO',
    'end': 'FIM',
    'imp': 'IMP',
    'le': 'LE',
    'num': 'TIPO',
    'txt': 'TIPO',
    'vet': 'TIPO',
    'vf': 'TIPO',
    'c': 'SE',
    'cnn': 'SENAO',
    '->': 'ENQT',
    'pra': 'PRA',
    'V': 'RESPOSTABOOLEANA',
    'F': 'RESPOSTABOOLEANA',
    'nao': 'NAO',
    
    # Adicione outras palavras reservadas aqui
}

# Lista de tokens
tokens = [
    'INICIO', 'FIM', 'LINETERMINATOR', 'NUM', 'TXT', 'VET', 'VF', 'CARACTERE',
    'DIGITO', 'ABREASPAS', 'FECHAASPAS', 'ABRECOLCHETE', 'FECHACOLCHETE',
    'IMP', 'LE', 'ATRIBUIR', 'ATRIBUICAO', 'SE', 'SENAO', 'ENQT', 'PRA',
    'RELACIONAL', 'LOGICO', 'E', 'OU', 'NAO', 'BLOCO', 'BLOCOS', 'SIMBOLO', 'DEFVARIAVEL',
    'TIPO', 'OPERADOR_MAIS', 'OPERADOR_MENOS', 'OPERADOR_DIVISAO', 'VIRGULA',
    'OPERADOR_MULTIPLICACAO', 'ESPACO', 'PONTOEVIRGULA', 'ABREPARENTESE',
    'FECHAPARENTESE', 'ABRECHAVE', 'FECHACHAVE', 'QUEBRALINHA', 'COMENTARIOS', 'ID', 'RESPOSTABOOLEANA'
]

# Definindo as regras de expressão regular para alguns tokens
t_RESPOSTABOOLEANA = r'V|F'
t_INICIO = r'main'
t_FIM = r'end'
t_LINETERMINATOR = r'\n'
t_COMENTARIOS = r'\'[^\']*\''
t_TIPO = r'txt|num|vet|vf'
# t_NUM = r'\d+'
t_VET = r'vet'
t_VF = r'vf'
# t_CARACTERE = r'[a-zA-Z]'
t_DIGITO = r'\d'
t_ABREASPAS = r'"'
t_FECHAASPAS = r'"'
t_ABRECOLCHETE = r'\['
t_FECHACOLCHETE = r'\]'
t_IMP = r'imp'
t_LE = r'le'
t_ATRIBUIR = r':'
t_ATRIBUICAO = r'='
t_SE = r'c'
t_SENAO = r'cnn'
t_ENQT = r'while'
t_PRA = r'for'
t_RELACIONAL = r'[<>!]=? | [=]'
t_LOGICO = r'[&|]'
t_E = r'&&'
t_OU = r'\|\|'
t_NAO = r'nao'
t_BLOCO = r'\(\)'
t_VIRGULA = r','
#t_DEFVARIAVEL = r' '
t_OPERADOR_MAIS = r'\+'
t_OPERADOR_MENOS = r'-'
t_OPERADOR_DIVISAO = r'/'
t_OPERADOR_MULTIPLICACAO = r'\*'
t_ESPACO = r'\s+'
t_PONTOEVIRGULA = r';'
t_ABREPARENTESE = r'\('
t_FECHAPARENTESE = r'\)'
t_ABRECHAVE = r'\{'
t_FECHACHAVE = r'\}'
# t_QUEBRALINHA = r'\/\/'
t_QUEBRALINHA = r'---'
t_TXT = r'"([^"\\]|\\.)*"'
#t_ID = r'[a-z][a-zA-Z0-9]*'

def t_CARACTERE(t):
    r'[a-z][a-zA-Z0-9]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t

#regras para o token NUM
def t_NUM(t):
    r'-?\d+(\,\d+)?'  # Pode ser um número inteiro ou decimal, positivo ou negativo
    t.value = t.value.replace(',', '.')
    t.value = float(t.value)  # Convertendo para float para representar números decimais
    return t


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
print("\n\n\n")