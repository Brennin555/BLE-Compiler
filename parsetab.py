
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPERADOR_MAISOPERADOR_MENOSleftOPERADOR_MULTIPLICACAOOPERADOR_DIVISAOABREASPAS ABRECHAVE ABRECOLCHETE ABREPARTESE ATRIBUICAO ATRIBUIR BLOCO CARACTERE COMENTARIOS DEFVARIAVEL DIGITO E ENQT ESPACO FECHAASPAS FECHACHAVE FECHACOLCHETE FECHAPARENTESE FIM ID IMP INICIO LE LINETERMINATOR LOGICO NUM OPERADOR_DIVISAO OPERADOR_MAIS OPERADOR_MENOS OPERADOR_MULTIPLICACAO OU PONTOEVIRGULA PRA QUEBRALINHA RELACIONAL SE SENAO SIMBOLO TIPO TXT VET VF VIRGULA\n    programa : inicio\n    \n    inicio : INICIO ABRECHAVE operacoes FECHACHAVE\n    | INICIO ABRECHAVE\n    \n    tipo : TXT\n         | NUM\n    \n    txt : TXT\n    \n    le : LE ABREPARTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA\n       | LE ABREPARTESE ID FECHAPARENTESE\n    \n    imp : IMP ABREPARTESE expressao FECHAPARENTESE PONTOEVIRGULA\n        | IMP ABREPARTESE expressao FECHAPARENTESE\n    \n    declaracoes : declaracao PONTOEVIRGULA declaracoes\n                | QUEBRALINHA declaracoes\n                | COMENTARIOS QUEBRALINHA declaracoes\n                | QUEBRALINHA COMENTARIOS declaracoes\n                | COMENTARIOS\n                | TIPO ID ATRIBUIR expressao PONTOEVIRGULA\n                | TIPO ID ATRIBUICAO declaracao PONTOEVIRGULA\n    \n    declaracao : TIPO ESPACO CARACTERE atribuir\n               | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir\n               | ESPACO CARACTERE atribuir\n               | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir\n               | tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA\n               | tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA\n    \n    atribuir : ATRIBUIR variavel\n             | ATRIBUICAO variavel\n             | TIPO ID ATRIBUIR expressao \n    \n    variavel : ESPACO CARACTERE\n    \n    operacoes : expressao SIMBOLO operacoes\n              | expressao\n              | imp\n              | le\n    \n    expressao : NUM\n              | variavel\n              | TXT\n              | aritimetico\n              | ABREPARTESE expressao FECHAPARENTESE                      \n    aritimetico  : expressao OPERADOR_DIVISAO expressao\n                    | expressao OPERADOR_MULTIPLICACAO expressao\n                    | expressao OPERADOR_MAIS expressao\n                    | expressao OPERADOR_MENOS expressao\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,4,17,],[0,-1,-3,-2,]),'ABRECHAVE':([3,],[4,]),'NUM':([4,13,18,19,20,21,22,24,],[9,9,9,9,9,9,9,9,]),'TXT':([4,13,18,19,20,21,22,24,],[11,11,11,11,11,11,11,11,]),'ABREPARTESE':([4,13,14,15,18,19,20,21,22,24,],[13,13,24,25,13,13,13,13,13,13,]),'IMP':([4,18,],[14,14,]),'LE':([4,18,],[15,15,]),'ESPACO':([4,13,18,19,20,21,22,24,],[16,16,16,16,16,16,16,16,]),'FECHACHAVE':([5,6,7,8,9,10,11,12,26,27,28,29,30,31,32,36,38,39,41,],[17,-29,-30,-31,-32,-33,-34,-35,-27,-28,-37,-38,-39,-40,-36,-10,-8,-9,-7,]),'SIMBOLO':([6,9,10,11,12,26,28,29,30,31,32,],[18,-32,-33,-34,-35,-27,-37,-38,-39,-40,-36,]),'OPERADOR_DIVISAO':([6,9,10,11,12,23,26,28,29,30,31,32,33,],[19,-32,-33,-34,-35,19,-27,-37,-38,19,19,-36,19,]),'OPERADOR_MULTIPLICACAO':([6,9,10,11,12,23,26,28,29,30,31,32,33,],[20,-32,-33,-34,-35,20,-27,-37,-38,20,20,-36,20,]),'OPERADOR_MAIS':([6,9,10,11,12,23,26,28,29,30,31,32,33,],[21,-32,-33,-34,-35,21,-27,-37,-38,-39,-40,-36,21,]),'OPERADOR_MENOS':([6,9,10,11,12,23,26,28,29,30,31,32,33,],[22,-32,-33,-34,-35,22,-27,-37,-38,-39,-40,-36,22,]),'FECHAPARENTESE':([9,10,11,12,23,26,28,29,30,31,32,33,35,37,],[-32,-33,-34,-35,32,-27,-37,-38,-39,-40,-36,36,38,40,]),'CARACTERE':([16,],[26,]),'TIPO':([25,],[34,]),'ID':([25,34,],[35,37,]),'PONTOEVIRGULA':([36,40,],[39,41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'inicio':([0,],[2,]),'operacoes':([4,18,],[5,27,]),'expressao':([4,13,18,19,20,21,22,24,],[6,23,6,28,29,30,31,33,]),'imp':([4,18,],[7,7,]),'le':([4,18,],[8,8,]),'variavel':([4,13,18,19,20,21,22,24,],[10,10,10,10,10,10,10,10,]),'aritimetico':([4,13,18,19,20,21,22,24,],[12,12,12,12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> inicio','programa',1,'p_programa','parser_ble.py',16),
  ('inicio -> INICIO ABRECHAVE operacoes FECHACHAVE','inicio',4,'p_main','parser_ble.py',24),
  ('inicio -> INICIO ABRECHAVE','inicio',2,'p_main','parser_ble.py',25),
  ('tipo -> TXT','tipo',1,'p_tipo','parser_ble.py',33),
  ('tipo -> NUM','tipo',1,'p_tipo','parser_ble.py',34),
  ('txt -> TXT','txt',1,'p_txt','parser_ble.py',58),
  ('le -> LE ABREPARTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA','le',6,'p_le','parser_ble.py',68),
  ('le -> LE ABREPARTESE ID FECHAPARENTESE','le',4,'p_le','parser_ble.py',69),
  ('imp -> IMP ABREPARTESE expressao FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',78),
  ('imp -> IMP ABREPARTESE expressao FECHAPARENTESE','imp',4,'p_imp','parser_ble.py',79),
  ('declaracoes -> declaracao PONTOEVIRGULA declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',88),
  ('declaracoes -> QUEBRALINHA declaracoes','declaracoes',2,'p_declaracoes','parser_ble.py',89),
  ('declaracoes -> COMENTARIOS QUEBRALINHA declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',90),
  ('declaracoes -> QUEBRALINHA COMENTARIOS declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',91),
  ('declaracoes -> COMENTARIOS','declaracoes',1,'p_declaracoes','parser_ble.py',92),
  ('declaracoes -> TIPO ID ATRIBUIR expressao PONTOEVIRGULA','declaracoes',5,'p_declaracoes','parser_ble.py',93),
  ('declaracoes -> TIPO ID ATRIBUICAO declaracao PONTOEVIRGULA','declaracoes',5,'p_declaracoes','parser_ble.py',94),
  ('declaracao -> TIPO ESPACO CARACTERE atribuir','declaracao',4,'p_declaracao','parser_ble.py',102),
  ('declaracao -> TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir','declaracao',7,'p_declaracao','parser_ble.py',103),
  ('declaracao -> ESPACO CARACTERE atribuir','declaracao',3,'p_declaracao','parser_ble.py',104),
  ('declaracao -> ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir','declaracao',6,'p_declaracao','parser_ble.py',105),
  ('declaracao -> tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA','declaracao',6,'p_declaracao','parser_ble.py',106),
  ('declaracao -> tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA','declaracao',6,'p_declaracao','parser_ble.py',107),
  ('atribuir -> ATRIBUIR variavel','atribuir',2,'p_atribuir','parser_ble.py',115),
  ('atribuir -> ATRIBUICAO variavel','atribuir',2,'p_atribuir','parser_ble.py',116),
  ('atribuir -> TIPO ID ATRIBUIR expressao','atribuir',4,'p_atribuir','parser_ble.py',117),
  ('variavel -> ESPACO CARACTERE','variavel',2,'p_variavel','parser_ble.py',125),
  ('operacoes -> expressao SIMBOLO operacoes','operacoes',3,'p_operacoes','parser_ble.py',134),
  ('operacoes -> expressao','operacoes',1,'p_operacoes','parser_ble.py',135),
  ('operacoes -> imp','operacoes',1,'p_operacoes','parser_ble.py',136),
  ('operacoes -> le','operacoes',1,'p_operacoes','parser_ble.py',137),
  ('expressao -> NUM','expressao',1,'p_expressao','parser_ble.py',144),
  ('expressao -> variavel','expressao',1,'p_expressao','parser_ble.py',145),
  ('expressao -> TXT','expressao',1,'p_expressao','parser_ble.py',146),
  ('expressao -> aritimetico','expressao',1,'p_expressao','parser_ble.py',147),
  ('expressao -> ABREPARTESE expressao FECHAPARENTESE','expressao',3,'p_expressao','parser_ble.py',148),
  ('aritimetico -> expressao OPERADOR_DIVISAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',163),
  ('aritimetico -> expressao OPERADOR_MULTIPLICACAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',164),
  ('aritimetico -> expressao OPERADOR_MAIS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',165),
  ('aritimetico -> expressao OPERADOR_MENOS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',166),
]