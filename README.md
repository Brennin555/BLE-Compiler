<div align="center">
         <img src="./preg.png" alt="Preguiça computeira" width="250">
    <h1>
        Linguagem BLE  
    </h1>
</div>


Linguagem desenvolvida para a matéria de ECOM06A, ministrada pela professora Thatyana Seraphim

Este projeto consiste na linguagem BLE, desenvolvida pelos alunos:

[Brenno de Oliveira da Rosa](https://github.com/Brennin555) - 2021029935<br>
[Eduardo Alves Carvalho](https://github.com/Eduardo2021017550) - 2021017550<br>
[Lucas Luan Belarmino Barbosa](https://github.com/luc-llb) - 2021017872<br>

A linguagem BLE foi desenvolvida utilizando Python, mais especificamente a biblioteca PLY (Python Lex Yacc)

Foram desenvolvidos 3 códigos utilizando a linguagem para apresentação da mesma. Os arquivos são `main.ble`, `main2.ble` e `main3.ble`.

Para executar esta linguagem, é necessário:

1. Instalar o python (utilizamos a versão 3.11)

2. Clonar este repositório:
   
```
    git clone https://github.com/Brennin555/BLE-Compiler.git
```
 3. Instalar a biblioteca PLY:

```
    pip install ply
```
 
4. Abrir o terminal e executar o arquivo `parser_ble.py`

```
    python parser_ble.py
```

Ao executar o programa, ele te oferecerá 3 possibilidades de código para rodar. Escolha o que desejar.

Executando esse comando, os analisadores léxico e sintático (`lexer.py` e `parser_ble.py`) realizaram a analise e transcrição do arquivo `.ble` escolhido para a linguagem Python. 

Após escolher e o programa rodar, execute o comando:

```
    python ble_code.py
```

Após isso comando compilará o código python proveniente do código `.ble` gerado. 

OBS: Os tokens identificados ao compilar o código (gerados pelo lexer) estarão impressos no arquivo `tokens.txt`. Cada vez que um novo código for compilado, a `tokens.txt` será sobreescrita. A pasta `tokens` contém os tokens referentes aos arquivos testes solicitados pela professora.

Além disso, os identificadores identificados ao compilar o código (gerados pelo parser) estarão impressos no arquivo `identificadores.txt`. Cada vez que um novo código for compilado, a `identificadores.txt` será sobreescrita. A pasta `identificadores` contém os identificadores referentes aos arquivos testes solicitados pela professora.
