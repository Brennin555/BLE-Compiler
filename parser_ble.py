import ply.yacc as yacc
from lexer import tokens, programaEscolhido

# Lista de tokens (importada do lexer)
tk = tokens
variaveis = []
variaveis.append({'nome': '', 'valor': '', 'tipo': ''})

# Definindo precedência dos operadores
precedence = (
    ('left', 'OPERADOR_MAIS', 'OPERADOR_MENOS'),
    ('left', 'OPERADOR_MULTIPLICACAO', 'OPERADOR_DIVISAO'),
    ('right', 'NAO')
)

# Regras de produção e ações
def p_programa(p):
    '''
    programa : inicio
    '''

def p_inicio(p):
    '''
    inicio : INICIO ABRECHAVE blocos FECHACHAVE
    '''
    f = open("ble_code.py", "w")
    f.write(f'{p[3]}')
    f.close()
    
def p_id(p):
    '''
    id : ID
    '''
    for i in variaveis:
        if i['nome'] == f'{p[1]}':
            p[0] = f'{p[1]}'
    
    if str(p[0]) == 'None':     
        raise NameError(f"Variavel '{p[1]}' não definida")

def p_le(p):
    '''
    le : LE ABREPARENTESE TIPO id FECHAPARENTESE PONTOEVIRGULA
    '''
        
    if compara_var(p[4],p[3]):
        if p[3] == 'txt':
            p[0] = f'{p[4]} = input()\n'
        elif p[3] == 'num':
            p[0] = f'{p[4]} = float(input())\n'
        elif p[3] == 'vet':
            p[0] = f'{p[4]} = input()\n{p[4]} = {p[4]}.split()\n{p[4]} = [int(valor) for valor in {p[4]}]\n'

def p_operacao(p):
    '''
    operacao : str OPERADOR_MAIS str
             | str OPERADOR_MAIS operacao
             | expressao OPERADOR_MAIS operacao
             | str OPERADOR_MAIS expressao
             | expressao OPERADOR_MAIS str
    ''' 
    
    if p[1] == 'str' and p[3] == 'str':
        p[0] = f'{p[1]} + {p[3]}'
    elif p[1] == 'str' and p[3] != 'str':
        p[0] = f'{p[1]} + str({p[3]})'
    elif p[1] != 'str' and p[3] == 'str':
        p[0] = f'str({p[1]}) + {p[3]}'
    else:
        p[0] = f'str({p[1]}) + str({p[3]})'

def p_imp(p):
    '''
    imp : IMP ABREPARENTESE str FECHAPARENTESE PONTOEVIRGULA
        | IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA
        | IMP ABREPARENTESE operacao FECHAPARENTESE PONTOEVIRGULA
    '''
    
    p[0] = f'print({p[3]})\n'                  

def p_str(p):
    '''str  : TXT
    '''
    p[0] = p[1]
    
def p_blocos(p):
    '''
    blocos : bloco blocos
           | bloco
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_comentarios(p):
    '''
    comentarios : COMENTARIOS
    '''
    p[0] = ''

def p_bloco(p):
    '''
    bloco : enqt
             | pra
             | se
             | imp
             | le
             | defvariavel
             | atribuir
             | atribuicao
             | comentarios
    '''
    p[0] = p[1]
    
def p_expressao(p):
    '''
    expressao : id
              | NUM
              | aritimetico
              | ABREPARENTESE expressao FECHAPARENTESE                     
    '''
    if len(p) == 4:
        p[0] = f'({p[2]})'
    else:
        p[0] = p[1]
        
def p_aritimetico(p):
    '''aritimetico  : expressao OPERADOR_DIVISAO expressao
                    | expressao OPERADOR_MULTIPLICACAO expressao
                    | expressao OPERADOR_MAIS expressao
                    | expressao OPERADOR_MENOS expressao
    '''
    match p[2]:
        case '+':
            p[0] = f'{p[1]} + {p[3]}'
        case '-':
            p[0] = f'{p[1]} - {p[3]}'
        case '*':
            p[0] = f'{p[1]} * {p[3]}'
        case '/':
            p[0] = f'{p[1]} / {p[3]}'

def p_atribuicao(p):
    '''
    atribuicao : ATRIBUIR expressao
               | ATRIBUIR str
               | ATRIBUIR ABRECOLCHETE lista FECHACOLCHETE   
               | ATRIBUIR RESPOSTABOOLEANA
    '''
    if len(p) == 3:
        if p[2] == 'F':
            p[0] = 'False'
        elif p[2] == 'V':
            p[0] = 'True'
        else:
            p[0] = f'{p[2]}'
    else:
        p[0] = f'[{p[3]}]'
        
        
def p_atribuir(p):
    '''
    atribuir : id atribuicao PONTOEVIRGULA
             | TIPO ID atribuicao PONTOEVIRGULA
             | TIPO ID ABRECOLCHETE NUM FECHACOLCHETE atribuicao PONTOEVIRGULA  
    '''
    if len(p) == 5:
        p[0] = f'{p[2]} = {p[3]}\n'
        variaveis.append({'nome': p[2], 'valor': p[3], 'tipo': p[1]})
    elif len(p) == 8:
            p[0] = f'{p[2]} = {p[6]}\n'
            variaveis.append({'nome': p[2], 'valor': p[6], 'tipo': p[1]})
    else:
        p[0] = f'{p[1]} = {p[2]}\n'
  
def p_lista(p):
    '''
    lista : NUM
          | id
          | lista lista
    '''
    if len(p) == 2:
        p[0] = f'{p[1]}'
    else:
        p[0] = f'{p[1]} , {p[2]}'
        
def p_defvarivale(p):
    '''
    defvariavel : TIPO ID PONTOEVIRGULA
    '''
    if p[1] == 'txt':
        variaveis.append({'nome': p[2], 'valor': '', 'tipo': p[1]})
        p[0] = f'{p[2]} = ""\n'
    elif p[1] == 'num':
        variaveis.append({'nome': p[2], 'valor': '0', 'tipo': p[1]})
        p[0] = f'{p[2]} = 0\n'
    elif p[1] == 'vf':
        variaveis.append({'nome': p[2], 'valor': 'False', 'tipo': p[1]})
        p[0] = f'{p[2]} = False\n'
    else:
        variaveis.append({'nome': p[2], 'valor': '[]', 'tipo': p[1]})
        p[0] = f'{p[2]} = []\n'

def p_logico(p):
    '''
    logico : E
           | OU
    '''
    p[0] = f'{p[1]}'
      
def p_condicional(p):
    '''
    condicional : atomica
                | atomica logico atomica
                | condicional logico condicional
                
    '''
    if len(p) == 4:
        if p[2] == 'e':
            p[0] = f'{p[1]} and {p[3]}'
        elif p[2] == 'ou':
            p[0]= f'{p[1]} or {p[3]}'
    else:
        p[0] = f'{p[1]}'

def p_condicional_atomica(p):
    '''
    atomica : RESPOSTABOOLEANA
            | NUM
            | id
            | str
            | NAO condicional
            | atomica RELACIONAL atomica
    '''

    tamanho = len(p)
    if tamanho == 2:
        if p[1] == 'V':
            p[0] = 'True'
        elif p[1] == 'F':
            p[0] = 'False'
        else:
            p[0] = f'{p[1]}'

    elif tamanho == 3:
        p[0] = f'not {p[1]}'

    elif tamanho == 4:
        match(p[2]):
            case '>':
                p[0] = f'{p[1]} > {p[3]}'
            case '<':
                p[0] = f'{p[1]} < {p[3]}'
            case '=':
                p[0] = f'{p[1]} == {p[3]}'
            case '!=':
                p[0] = f'{p[1]} != {p[3]}'
            case '>=':
                p[0] = f'{p[1]} >= {p[3]}'
            case '<=':
                p[0] = f'{p[1]} <= {p[3]}'

def p_enqt(p):
    ''' 
    enqt : ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE blocos FECHACHAVE
    '''
    p[0] = f'while {p[2]} :\n{tabulacao(p[6])}'
    
def tabulacao(s):
    aux = s.split('\n')
    aux = ['\t'+i for i in aux]
    return '\n'.join(aux)    

def compara_var(nome, tipo):
    for var in variaveis:
        if var['nome'] == nome:
            break
    if var['tipo'] == tipo:
        return True
    raise TypeError(f"Variavel '{nome}' não é do tipo '{tipo}'")

def p_senao(p):
    '''
    senao : SENAO ABRECHAVE bloco FECHACHAVE
    '''
    p[0] = f'else:\n{tabulacao(p[3])}\n'
    
def p_se(p):
    '''
    se : SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE
        | SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE senao
      '''
    p[0] = ''
    if len(p) == 8:
        p[0] = f'if {p[3]}:\n{tabulacao(p[6])}\n'
    else:
        p[0] = f'if {p[3]}:\n{tabulacao(p[6])}\n{p[8]}'
    
    
def p_pra(p):
    '''
    pra : PRA ABREPARENTESE id expressao expressao FECHAPARENTESE ABRECHAVE bloco FECHACHAVE
    '''
    p[0] = ''
    final=int(p[4])
    inc=int(p[5])

    for x in variaveis:
       if(x['nome'] == p[3]):
          inicio=float(x['valor'])
          
    p[0] = f'for {p[3]} in range({int(inicio)},{final},{inc}):\n{tabulacao(p[8])}\n'
# ---------------------------------------------------------------------   

    
# Tratamento de erro sintático
def p_error(p):
    print(f"Erro de sintaxe: Token inesperado '{p.value}' na linha {p.lineno}, coluna {p.lexpos}")


# Criando o analisador sintático
parser = yacc.yacc(debug=True, write_tables=True)

if programaEscolhido == 1:
    with open('main.ble', 'r') as file:
        code = file.read()
elif programaEscolhido == 2:
    with open('main2.ble', 'r') as file:
        code = file.read()
elif programaEscolhido == 3:
    with open('main3.ble', 'r') as file:
        code = file.read()
        
# Fazendo o parser do código
try:
    result = parser.parse(code)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)