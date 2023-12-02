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
# t_INICIO = r'main'
t_FIM = r'end'
t_LINETERMINATOR = r'\n'
#t_NUM = r'\d+'
#t_TXT = r'"[^"]*"'
#t_VET = r'vet'
#t_VF = r'vf'

#Dúvida: Precisará desses 4 tokens? 
t_CARACTERE = r'car'
t_DIGITO = r'\d'
t_ABREASPAS = r'"'
t_FECHAASPAS = r'"'

t_ABRECOLCHETE = r'\['
t_FECHACOLCHETE = r'\]'

#t_IMP = r'imp'
#t_LE = r'le'

t_ATRIBUIR = r':'
t_ATRIBUICAO = r':'

# t_SE = r'if'
# t_SENAO = r'else'

t_ENQT = r'while'
t_PRA = r'for'

t_RELACIONAL = r'[<>!]=? | ='
t_LOGICO = r'[&|]'

t_E = r'&&'
t_OU = r'\|\|'
t_BLOCO = r'\(\)'
t_SIMBOLO = r'[;,.]'

# t_DEFVARIAVEL = r'txt|num|vet|vf' #manter
t_TIPO = r'int|float|string|bool'

# Operadores funcionam
t_OPERADOR_MAIS = r'\+'
t_OPERADOR_MENOS = r'-'
t_OPERADOR_DIVISAO = r'/'
t_OPERADOR_MULTIPLICACAO = r'\*'
t_ESPACO = r'\s+'

# t_PONTOEVIRGULA = r';'
t_ABREPARTESE = r'\('
t_FECHAPARENTESE = r'\)'
t_ABRECHAVE = r'\{'
t_FECHACHAVE = r'\}'

# t_QUEBRALINHA = r'\/\/'
# t_COMENTARIOS = r'\'[^\']*\''

# Regras para o token COMENTARIOS
def t_COMENTARIOS(t):
    r'\'[^\']*\''
    return t

# Regras para o token inicio
def t_INICIO(t):
    r'main'
    return t

# Regras para o token QUEBRALINHA
def t_QUEBRALINHA(t):
    r'\/\/'
    return t

# Regras para o token SENAO
def t_SENAO(t):
    r'cnn'
    return t

# Regras para o token SE
def t_SE(t):
    r'c'
    return t

# Regras para o token DEFVARIAVEL
def t_DEFVARIAVEL(t):
    r'txt|num|vet|vf'
    return t


# Regras para o token PONTOEVIRGULA
def t_PONTOEVIRGULA(t):
    r';'
    return t

# Regras para o token IMP
def t_IMP(t):
    r'imp'
    return t

# Regras para o token LE
def t_LE(t):
    r'le'
    return t

#regras para o token NUM
def t_NUM(t):
    r'-?\d+(\,\d+)?'  # Pode ser um número inteiro ou decimal, positivo ou negativo
    #troca virgula por ponto:
    t.value = t.value.replace(',', '.')
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


#----------------------------------------------------------------

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
    # lines = input_string.split('\n')
    # print("\n\n\n", lines)
lexer.input(input_string)

# Agora você pode iterar sobre os tokens
for token in lexer:
    # deixar alinhado os dados do print:
        print(
        token.type.ljust(15),
        str(token.value).ljust(15),
        str(token.lineno).ljust(10),
        str(token.lexpos).ljust(10)
    )

