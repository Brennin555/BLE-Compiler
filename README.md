# BLE

Linguagem desenvolvida para a matéria de ECOM06A, ministrada pela professora Thatyana Seraphim

A linguagem desenvolvida neste projeto é a BLE, desenvolvida pelos alunos:

Brenno de Oliveira da Rosa - 2021029935<br>
Eduardo Alves Carvalho - 20210175570<br>
Lucas Luan Belarmino Barbosa - 2021017872<br>

A linguagem BLE foi desenvolvida utilizando Python, mais especificamente a biblioteca PLY (Python Lex Yacc)

Foram desenvolvidos 3 códigos utilizando a linguagem para apresentação da mesma. Os arquivos são main.ble, main2.ble e main3.ble (deixar o nome dos arquivos marcado)

Para executar esta linguagem, é necessário:

<li> Instalar o python (utilizamos a versão 3.11)</li>


<li> Clonar este repositório:</li>

```
    git clone https://github.com/Brennin555/BLE-Compiler.git
```
<li> Instalar a biblioteca PLY: </li>

```
    pip install ply
```
 
<li> Abrir o terminal e executar o arquivo `parser_ble.py`</li>

```
    python parser_ble.py

```

Ao executar o programa, ele te oferecerá 3 possibilidades de código para rodar. Escolha o que desejar.

Executando esse comando, os analisadores léxico e sintático (lexer.py e parser_ble.py) realizaram a analise e transcrição do arquivo .ble escolhido para a linguagem Python. 

Após escolher e o programa rodar, execute o comando:

```
    python ble_code.py

```

Apoós isso comando compilará o código python proveniente do código .ble gerado. 

OBS: Os tokens identificados ao compilar o código estarão impressos no arquivo tokens.txt.