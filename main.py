# main.py
from lexer import lexer
from parser_ble import parser

# Seu código principal aqui
codigo_exemplo = '''
main{
    imp("Hello World");
}
'''

# Parsing do código de exemplo
parser.parse(codigo_exemplo)
