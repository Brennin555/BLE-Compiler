
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPERADOR_MAISOPERADOR_MENOSleftOPERADOR_MULTIPLICACAOOPERADOR_DIVISAOABREASPAS ABRECHAVE ABRECOLCHETE ABREPARENTESE ATRIBUICAO ATRIBUIR BLOCO CARACTERE COMENTARIOS DEFVARIAVEL DIGITO E ENQT ESPACO FECHAASPAS FECHACHAVE FECHACOLCHETE FECHAPARENTESE FIM ID IMP INICIO LE LINETERMINATOR LOGICO NUM OPERADOR_DIVISAO OPERADOR_MAIS OPERADOR_MENOS OPERADOR_MULTIPLICACAO OU PONTOEVIRGULA PRA QUEBRALINHA RELACIONAL RESPOSTABOOLEANA SE SENAO SIMBOLO TIPO TXT VET VF VIRGULA\n    programa : inicio\n    \n    inicio : INICIO ABRECHAVE bloco FECHACHAVE\n    \n    tipo : TXT\n         | NUM\n    \n    txt : TXT\n    \n    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA\n       | LE ABREPARENTESE ID FECHAPARENTESE\n    \n    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA\n        | IMP ABREPARENTESE expressao FECHAPARENTESE\n    \n    declaracoes : declaracao PONTOEVIRGULA declaracoes\n                | QUEBRALINHA declaracoes\n                | COMENTARIOS QUEBRALINHA declaracoes\n                | QUEBRALINHA COMENTARIOS declaracoes\n                | COMENTARIOS\n                | TIPO ID ATRIBUIR expressao PONTOEVIRGULA\n                | TIPO ID ATRIBUICAO declaracao PONTOEVIRGULA\n                | TIPO ID ATRIBUIR TXT\n    \n    declaracao : TIPO ESPACO CARACTERE atribuir\n               | TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir\n               | ESPACO CARACTERE atribuir\n               | ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir\n               | tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA\n               | tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA\n               \n                 \n    \n    variavel : ESPACO CARACTERE\n    \n    expressao : NUM\n              | variavel\n              | ID\n              | TXT\n              | aritimetico\n              | ABREPARENTESE expressao FECHAPARENTESE\n              | RESPOSTABOOLEANA\n              \n                         \n    aritimetico  : expressao OPERADOR_DIVISAO expressao\n                    | expressao OPERADOR_MULTIPLICACAO expressao\n                    | expressao OPERADOR_MAIS expressao\n                    | expressao OPERADOR_MENOS expressao\n    \n    atribuicao : ATRIBUIR expressao\n               | ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE   \n    \n    atribuir : TIPO ID atribuicao PONTOEVIRGULA \n             | TIPO ID ATRIBUIR expressao PONTOEVIRGULA \n             | ID atribuicao PONTOEVIRGULA\n             \n    \n    incremento : ID OPERADOR_MAIS NUM\n               | ID OPERADOR_MENOS NUM\n    \n    pra : PRA ABREPARENTESE ID ESPACO incremento FECHAPARENTESE ABRECHAVE bloco FECHACHAVE\n    \n    bloco   : imp\n            | pra\n            | le\n            | atribuir\n            | atribuicao\n            | expressao PONTOEVIRGULA bloco\n            | expressao PONTOEVIRGULA\n            \n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,25,],[0,-1,-2,]),'ABRECHAVE':([3,69,],[4,73,]),'IMP':([4,26,73,],[12,12,12,]),'PRA':([4,26,73,],[14,14,14,]),'LE':([4,26,73,],[17,17,17,]),'TIPO':([4,26,37,73,],[18,18,50,18,]),'ID':([4,13,18,19,26,27,28,29,30,31,34,37,40,50,53,56,73,],[15,33,38,33,15,33,33,33,33,33,48,51,33,57,33,63,15,]),'ATRIBUIR':([4,15,26,38,73,],[19,19,19,53,19,]),'NUM':([4,13,19,26,27,28,29,30,31,40,53,67,68,73,],[20,20,20,20,20,20,20,20,20,20,20,71,72,20,]),'TXT':([4,13,19,26,27,28,29,30,31,40,53,73,],[22,22,22,22,22,22,22,22,22,22,22,22,]),'ABREPARENTESE':([4,12,13,14,17,19,26,27,28,29,30,31,40,53,73,],[13,31,13,34,37,13,13,13,13,13,13,13,13,13,13,]),'RESPOSTABOOLEANA':([4,13,19,26,27,28,29,30,31,40,53,73,],[24,24,24,24,24,24,24,24,24,24,24,24,]),'ESPACO':([4,13,19,26,27,28,29,30,31,40,48,53,73,],[16,16,16,16,16,16,16,16,16,16,56,16,16,]),'FECHACHAVE':([5,6,7,8,9,10,20,21,22,23,24,26,33,36,39,41,42,43,44,45,47,49,55,58,59,61,62,66,70,74,75,],[25,-44,-45,-46,-47,-48,-25,-26,-28,-29,-31,-50,-27,-24,-36,-49,-32,-33,-34,-35,-30,-40,-9,-7,-38,-37,-8,-39,-6,75,-43,]),'PONTOEVIRGULA':([11,15,20,21,22,23,24,33,35,36,39,42,43,44,45,47,52,55,60,61,65,],[26,-27,-25,-26,-28,-29,-31,-27,49,-24,-36,-32,-33,-34,-35,-30,59,62,66,-37,70,]),'OPERADOR_DIVISAO':([11,15,20,21,22,23,24,32,33,36,39,42,43,44,45,46,47,54,60,],[27,-27,-25,-26,-28,-29,-31,27,-27,-24,27,-32,-33,27,27,27,-30,27,27,]),'OPERADOR_MULTIPLICACAO':([11,15,20,21,22,23,24,32,33,36,39,42,43,44,45,46,47,54,60,],[28,-27,-25,-26,-28,-29,-31,28,-27,-24,28,-32,-33,28,28,28,-30,28,28,]),'OPERADOR_MAIS':([11,15,20,21,22,23,24,32,33,36,39,42,43,44,45,46,47,54,60,63,],[29,-27,-25,-26,-28,-29,-31,29,-27,-24,29,-32,-33,-34,-35,29,-30,29,29,67,]),'OPERADOR_MENOS':([11,15,20,21,22,23,24,32,33,36,39,42,43,44,45,46,47,54,60,63,],[30,-27,-25,-26,-28,-29,-31,30,-27,-24,30,-32,-33,-34,-35,30,-30,30,30,68,]),'CARACTERE':([16,],[36,]),'ABRECOLCHETE':([19,53,],[40,40,]),'FECHAPARENTESE':([20,21,22,23,24,32,33,36,42,43,44,45,46,47,51,57,64,71,72,],[-25,-26,-28,-29,-31,47,-27,-24,-32,-33,-34,-35,55,-30,58,65,69,-41,-42,]),'FECHACOLCHETE':([20,21,22,23,24,33,36,42,43,44,45,47,54,],[-25,-26,-28,-29,-31,-27,-24,-32,-33,-34,-35,-30,61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'inicio':([0,],[2,]),'bloco':([4,26,73,],[5,41,74,]),'imp':([4,26,73,],[6,6,6,]),'pra':([4,26,73,],[7,7,7,]),'le':([4,26,73,],[8,8,8,]),'atribuir':([4,26,73,],[9,9,9,]),'atribuicao':([4,15,26,38,73,],[10,35,10,52,10,]),'expressao':([4,13,19,26,27,28,29,30,31,40,53,73,],[11,32,39,11,42,43,44,45,46,54,60,11,]),'variavel':([4,13,19,26,27,28,29,30,31,40,53,73,],[21,21,21,21,21,21,21,21,21,21,21,21,]),'aritimetico':([4,13,19,26,27,28,29,30,31,40,53,73,],[23,23,23,23,23,23,23,23,23,23,23,23,]),'incremento':([56,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> inicio','programa',1,'p_programa','parser_ble.py',18),
  ('inicio -> INICIO ABRECHAVE bloco FECHACHAVE','inicio',4,'p_main','parser_ble.py',23),
  ('tipo -> TXT','tipo',1,'p_tipo','parser_ble.py',28),
  ('tipo -> NUM','tipo',1,'p_tipo','parser_ble.py',29),
  ('txt -> TXT','txt',1,'p_txt','parser_ble.py',37),
  ('le -> LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA','le',6,'p_le','parser_ble.py',43),
  ('le -> LE ABREPARENTESE ID FECHAPARENTESE','le',4,'p_le','parser_ble.py',44),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',51),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE','imp',4,'p_imp','parser_ble.py',52),
  ('declaracoes -> declaracao PONTOEVIRGULA declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',59),
  ('declaracoes -> QUEBRALINHA declaracoes','declaracoes',2,'p_declaracoes','parser_ble.py',60),
  ('declaracoes -> COMENTARIOS QUEBRALINHA declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',61),
  ('declaracoes -> QUEBRALINHA COMENTARIOS declaracoes','declaracoes',3,'p_declaracoes','parser_ble.py',62),
  ('declaracoes -> COMENTARIOS','declaracoes',1,'p_declaracoes','parser_ble.py',63),
  ('declaracoes -> TIPO ID ATRIBUIR expressao PONTOEVIRGULA','declaracoes',5,'p_declaracoes','parser_ble.py',64),
  ('declaracoes -> TIPO ID ATRIBUICAO declaracao PONTOEVIRGULA','declaracoes',5,'p_declaracoes','parser_ble.py',65),
  ('declaracoes -> TIPO ID ATRIBUIR TXT','declaracoes',4,'p_declaracoes','parser_ble.py',66),
  ('declaracao -> TIPO ESPACO CARACTERE atribuir','declaracao',4,'p_declaracao','parser_ble.py',71),
  ('declaracao -> TIPO ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir','declaracao',7,'p_declaracao','parser_ble.py',72),
  ('declaracao -> ESPACO CARACTERE atribuir','declaracao',3,'p_declaracao','parser_ble.py',73),
  ('declaracao -> ESPACO CARACTERE ABRECOLCHETE NUM FECHACOLCHETE atribuir','declaracao',6,'p_declaracao','parser_ble.py',74),
  ('declaracao -> tipo ESPACO ID ATRIBUIR expressao PONTOEVIRGULA','declaracao',6,'p_declaracao','parser_ble.py',75),
  ('declaracao -> tipo ESPACO ID ATRIBUICAO expressao PONTOEVIRGULA','declaracao',6,'p_declaracao','parser_ble.py',76),
  ('variavel -> ESPACO CARACTERE','variavel',2,'p_variavel','parser_ble.py',83),
  ('expressao -> NUM','expressao',1,'p_expressao','parser_ble.py',89),
  ('expressao -> variavel','expressao',1,'p_expressao','parser_ble.py',90),
  ('expressao -> ID','expressao',1,'p_expressao','parser_ble.py',91),
  ('expressao -> TXT','expressao',1,'p_expressao','parser_ble.py',92),
  ('expressao -> aritimetico','expressao',1,'p_expressao','parser_ble.py',93),
  ('expressao -> ABREPARENTESE expressao FECHAPARENTESE','expressao',3,'p_expressao','parser_ble.py',94),
  ('expressao -> RESPOSTABOOLEANA','expressao',1,'p_expressao','parser_ble.py',95),
  ('aritimetico -> expressao OPERADOR_DIVISAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',107),
  ('aritimetico -> expressao OPERADOR_MULTIPLICACAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',108),
  ('aritimetico -> expressao OPERADOR_MAIS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',109),
  ('aritimetico -> expressao OPERADOR_MENOS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',110),
  ('atribuicao -> ATRIBUIR expressao','atribuicao',2,'p_atribuicao','parser_ble.py',124),
  ('atribuicao -> ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE','atribuicao',4,'p_atribuicao','parser_ble.py',125),
  ('atribuir -> TIPO ID atribuicao PONTOEVIRGULA','atribuir',4,'p_atribuir','parser_ble.py',130),
  ('atribuir -> TIPO ID ATRIBUIR expressao PONTOEVIRGULA','atribuir',5,'p_atribuir','parser_ble.py',131),
  ('atribuir -> ID atribuicao PONTOEVIRGULA','atribuir',3,'p_atribuir','parser_ble.py',132),
  ('incremento -> ID OPERADOR_MAIS NUM','incremento',3,'p_incremento','parser_ble.py',140),
  ('incremento -> ID OPERADOR_MENOS NUM','incremento',3,'p_incremento','parser_ble.py',141),
  ('pra -> PRA ABREPARENTESE ID ESPACO incremento FECHAPARENTESE ABRECHAVE bloco FECHACHAVE','pra',9,'p_pra','parser_ble.py',146),
  ('bloco -> imp','bloco',1,'p_bloco','parser_ble.py',165),
  ('bloco -> pra','bloco',1,'p_bloco','parser_ble.py',166),
  ('bloco -> le','bloco',1,'p_bloco','parser_ble.py',167),
  ('bloco -> atribuir','bloco',1,'p_bloco','parser_ble.py',168),
  ('bloco -> atribuicao','bloco',1,'p_bloco','parser_ble.py',169),
  ('bloco -> expressao PONTOEVIRGULA bloco','bloco',3,'p_bloco','parser_ble.py',170),
  ('bloco -> expressao PONTOEVIRGULA','bloco',2,'p_bloco','parser_ble.py',171),
]
