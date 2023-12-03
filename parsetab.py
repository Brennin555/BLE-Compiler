
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPERADOR_MAISOPERADOR_MENOSleftOPERADOR_MULTIPLICACAOOPERADOR_DIVISAOABREASPAS ABRECHAVE ABRECOLCHETE ABREPARENTESE ATRIBUICAO ATRIBUIR BLOCO BLOCOS CARACTERE COMENTARIOS DEFVARIAVEL DIGITO E ENQT ESPACO FECHAASPAS FECHACHAVE FECHACOLCHETE FECHAPARENTESE FIM ID IMP INICIO LE LINETERMINATOR LOGICO NAO NUM OPERADOR_DIVISAO OPERADOR_MAIS OPERADOR_MENOS OPERADOR_MULTIPLICACAO OU PONTOEVIRGULA PRA QUEBRALINHA RELACIONAL RESPOSTABOOLEANA SE SENAO SIMBOLO TIPO TXT VET VF VIRGULA\n    programa : inicio\n    \n    inicio : INICIO ABRECHAVE blocos FECHACHAVE\n    \n    tipo : TXT\n         | NUM\n    \n    txt : TXT\n    \n    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA\n       | LE ABREPARENTESE ID FECHAPARENTESE\n    \n    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA\n        | IMP ABREPARENTESE expressao FECHAPARENTESE\n    \n    blocos : bloco blocos\n           | bloco\n    \n    bloco   :  enqt\n            | imp\n            | le\n            | atribuir\n            | atribuicao\n            | expressao\n    \n    expressao : ID\n              | NUM\n              | TXT\n              | aritimetico\n              | ABREPARENTESE expressao FECHAPARENTESE\n              | RESPOSTABOOLEANA\n              \n                         \n    aritimetico  : expressao OPERADOR_DIVISAO expressao\n                    | expressao OPERADOR_MULTIPLICACAO expressao\n                    | expressao OPERADOR_MAIS expressao\n                    | expressao OPERADOR_MENOS expressao\n    \n    atribuicao : ATRIBUIR expressao\n               | ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE   \n    \n    atribuir : ID atribuicao PONTOEVIRGULA\n             | TIPO ID atribuicao PONTOEVIRGULA \n             | TIPO ID ATRIBUIR expressao PONTOEVIRGULA \n    \n    condicional : atomica\n                | atomica LOGICO atomica\n    \n    atomica : RESPOSTABOOLEANA\n            | NUM\n            | ID\n            | NAO condicional\n            | condicional RELACIONAL condicional\n            | condicional LOGICO condicional\n     \n    enqt : ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE bloco FECHACHAVE\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,23,],[0,-1,-2,]),'ABRECHAVE':([3,64,],[4,75,]),'ABREPARENTESE':([4,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,25,26,27,28,29,37,41,42,43,44,45,46,47,51,61,62,69,71,72,74,75,76,78,80,81,],[13,13,-12,-13,-14,-15,-16,-17,29,37,38,-18,29,-19,-20,-21,-23,29,29,29,29,29,29,-28,29,-18,-24,-25,-26,-27,-22,29,-30,-9,-7,-31,-29,13,-8,-32,-6,-41,]),'IMP':([4,6,7,8,9,10,11,12,17,19,20,21,22,41,43,44,45,46,47,51,62,69,71,72,74,75,76,78,80,81,],[14,14,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-28,-18,-24,-25,-26,-27,-22,-30,-9,-7,-31,-29,14,-8,-32,-6,-41,]),'LE':([4,6,7,8,9,10,11,12,17,19,20,21,22,41,43,44,45,46,47,51,62,69,71,72,74,75,76,78,80,81,],[15,15,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-28,-18,-24,-25,-26,-27,-22,-30,-9,-7,-31,-29,15,-8,-32,-6,-41,]),'ID':([4,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,25,26,27,28,29,36,37,38,41,42,43,44,45,46,47,49,50,51,52,58,61,62,69,71,72,74,75,76,78,80,81,],[17,17,-12,-13,-14,-15,-16,-17,33,39,-18,43,-19,-20,-21,-23,43,43,43,43,43,56,43,59,-28,43,-18,-24,-25,-26,-27,56,56,-22,56,70,43,-30,-9,-7,-31,-29,17,-8,-32,-6,-41,]),'TIPO':([4,6,7,8,9,10,11,12,17,19,20,21,22,38,41,43,44,45,46,47,51,62,69,71,72,74,75,76,78,80,81,],[16,16,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,58,-28,-18,-24,-25,-26,-27,-22,-30,-9,-7,-31,-29,16,-8,-32,-6,-41,]),'ATRIBUIR':([4,6,7,8,9,10,11,12,17,19,20,21,22,39,41,43,44,45,46,47,51,62,69,71,72,74,75,76,78,80,81,],[18,18,-12,-13,-14,-15,-16,-17,18,-19,-20,-21,-23,61,-28,-18,-24,-25,-26,-27,-22,-30,-9,-7,-31,-29,18,-8,-32,-6,-41,]),'NUM':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,36,37,41,42,43,44,45,46,47,49,50,51,52,61,62,69,71,72,74,75,76,78,80,81,],[19,19,-12,-13,-14,-15,-16,-17,34,-18,19,-19,-20,-21,-23,19,19,19,19,19,55,19,-28,19,-18,-24,-25,-26,-27,55,55,-22,55,19,-30,-9,-7,-31,-29,19,-8,-32,-6,-41,]),'TXT':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,37,41,42,43,44,45,46,47,51,61,62,69,71,72,74,75,76,78,80,81,],[20,20,-12,-13,-14,-15,-16,-17,20,-18,20,-19,-20,-21,-23,20,20,20,20,20,20,-28,20,-18,-24,-25,-26,-27,-22,20,-30,-9,-7,-31,-29,20,-8,-32,-6,-41,]),'RESPOSTABOOLEANA':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,36,37,41,42,43,44,45,46,47,49,50,51,52,61,62,69,71,72,74,75,76,78,80,81,],[22,22,-12,-13,-14,-15,-16,-17,35,-18,22,-19,-20,-21,-23,22,22,22,22,22,54,22,-28,22,-18,-24,-25,-26,-27,54,54,-22,54,22,-30,-9,-7,-31,-29,22,-8,-32,-6,-41,]),'FECHACHAVE':([5,6,7,8,9,10,11,12,17,19,20,21,22,24,41,43,44,45,46,47,51,62,69,71,72,74,76,78,79,80,81,],[23,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-23,-10,-28,-18,-24,-25,-26,-27,-22,-30,-9,-7,-31,-29,-8,-32,81,-6,-41,]),'OPERADOR_DIVISAO':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,63,73,],[25,-18,-19,-20,-21,-23,25,-18,-19,-23,25,-18,-24,-25,25,25,-22,25,25,25,]),'OPERADOR_MULTIPLICACAO':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,63,73,],[26,-18,-19,-20,-21,-23,26,-18,-19,-23,26,-18,-24,-25,26,26,-22,26,26,26,]),'OPERADOR_MAIS':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,63,73,],[27,-18,-19,-20,-21,-23,27,-18,-19,-23,27,-18,-24,-25,-26,-27,-22,27,27,27,]),'OPERADOR_MENOS':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,63,73,],[28,-18,-19,-20,-21,-23,28,-18,-19,-23,28,-18,-24,-25,-26,-27,-22,28,28,28,]),'NAO':([13,36,49,50,52,],[36,36,36,36,36,]),'ABRECOLCHETE':([18,61,],[42,42,]),'PONTOEVIRGULA':([19,20,21,22,40,41,43,44,45,46,47,51,60,69,73,74,77,],[-19,-20,-21,-23,62,-28,-18,-24,-25,-26,-27,-22,72,76,78,-29,80,]),'FECHAPARENTESE':([19,20,21,22,30,31,32,33,34,35,43,44,45,46,47,51,53,54,55,56,57,59,65,66,67,70,],[-19,-20,-21,-23,48,51,-33,-18,-19,-23,-18,-24,-25,-26,-27,-22,-38,-35,-36,-37,69,71,-39,-40,-34,77,]),'FECHACOLCHETE':([19,20,21,22,43,44,45,46,47,51,63,],[-19,-20,-21,-23,-18,-24,-25,-26,-27,-22,74,]),'RELACIONAL':([30,32,33,34,35,53,54,55,56,65,66,67,68,],[49,-33,-37,-36,-35,49,-35,-36,-37,49,49,-33,49,]),'LOGICO':([30,32,33,34,35,53,54,55,56,65,66,67,68,],[50,52,-37,-36,-35,50,-35,-36,-37,50,50,52,50,]),'ENQT':([48,],[64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'inicio':([0,],[2,]),'blocos':([4,6,],[5,24,]),'bloco':([4,6,75,],[6,6,79,]),'enqt':([4,6,75,],[7,7,7,]),'imp':([4,6,75,],[8,8,8,]),'le':([4,6,75,],[9,9,9,]),'atribuir':([4,6,75,],[10,10,10,]),'atribuicao':([4,6,17,39,75,],[11,11,40,60,11,]),'expressao':([4,6,13,18,25,26,27,28,29,37,42,61,75,],[12,12,31,41,44,45,46,47,31,57,63,73,12,]),'aritimetico':([4,6,13,18,25,26,27,28,29,37,42,61,75,],[21,21,21,21,21,21,21,21,21,21,21,21,21,]),'condicional':([13,36,49,50,52,],[30,53,65,66,68,]),'atomica':([13,36,49,50,52,],[32,32,32,32,67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> inicio','programa',1,'p_programa','parser_ble.py',17),
  ('inicio -> INICIO ABRECHAVE blocos FECHACHAVE','inicio',4,'p_inicio','parser_ble.py',25),
  ('tipo -> TXT','tipo',1,'p_tipo','parser_ble.py',33),
  ('tipo -> NUM','tipo',1,'p_tipo','parser_ble.py',34),
  ('txt -> TXT','txt',1,'p_txt','parser_ble.py',45),
  ('le -> LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA','le',6,'p_le','parser_ble.py',75),
  ('le -> LE ABREPARENTESE ID FECHAPARENTESE','le',4,'p_le','parser_ble.py',76),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',90),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE','imp',4,'p_imp','parser_ble.py',91),
  ('blocos -> bloco blocos','blocos',2,'p_blocos','parser_ble.py',101),
  ('blocos -> bloco','blocos',1,'p_blocos','parser_ble.py',102),
  ('bloco -> enqt','bloco',1,'p_bloco','parser_ble.py',110),
  ('bloco -> imp','bloco',1,'p_bloco','parser_ble.py',111),
  ('bloco -> le','bloco',1,'p_bloco','parser_ble.py',112),
  ('bloco -> atribuir','bloco',1,'p_bloco','parser_ble.py',113),
  ('bloco -> atribuicao','bloco',1,'p_bloco','parser_ble.py',114),
  ('bloco -> expressao','bloco',1,'p_bloco','parser_ble.py',115),
  ('expressao -> ID','expressao',1,'p_expressao','parser_ble.py',123),
  ('expressao -> NUM','expressao',1,'p_expressao','parser_ble.py',124),
  ('expressao -> TXT','expressao',1,'p_expressao','parser_ble.py',125),
  ('expressao -> aritimetico','expressao',1,'p_expressao','parser_ble.py',126),
  ('expressao -> ABREPARENTESE expressao FECHAPARENTESE','expressao',3,'p_expressao','parser_ble.py',127),
  ('expressao -> RESPOSTABOOLEANA','expressao',1,'p_expressao','parser_ble.py',128),
  ('aritimetico -> expressao OPERADOR_DIVISAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',145),
  ('aritimetico -> expressao OPERADOR_MULTIPLICACAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',146),
  ('aritimetico -> expressao OPERADOR_MAIS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',147),
  ('aritimetico -> expressao OPERADOR_MENOS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',148),
  ('atribuicao -> ATRIBUIR expressao','atribuicao',2,'p_atribuicao','parser_ble.py',164),
  ('atribuicao -> ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE','atribuicao',4,'p_atribuicao','parser_ble.py',165),
  ('atribuir -> ID atribuicao PONTOEVIRGULA','atribuir',3,'p_atribuir','parser_ble.py',170),
  ('atribuir -> TIPO ID atribuicao PONTOEVIRGULA','atribuir',4,'p_atribuir','parser_ble.py',171),
  ('atribuir -> TIPO ID ATRIBUIR expressao PONTOEVIRGULA','atribuir',5,'p_atribuir','parser_ble.py',172),
  ('condicional -> atomica','condicional',1,'p_condicional','parser_ble.py',186),
  ('condicional -> atomica LOGICO atomica','condicional',3,'p_condicional','parser_ble.py',187),
  ('atomica -> RESPOSTABOOLEANA','atomica',1,'p_condicional_atomica','parser_ble.py',200),
  ('atomica -> NUM','atomica',1,'p_condicional_atomica','parser_ble.py',201),
  ('atomica -> ID','atomica',1,'p_condicional_atomica','parser_ble.py',202),
  ('atomica -> NAO condicional','atomica',2,'p_condicional_atomica','parser_ble.py',203),
  ('atomica -> condicional RELACIONAL condicional','atomica',3,'p_condicional_atomica','parser_ble.py',204),
  ('atomica -> condicional LOGICO condicional','atomica',3,'p_condicional_atomica','parser_ble.py',205),
  ('enqt -> ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE bloco FECHACHAVE','enqt',7,'p_enqt','parser_ble.py',232),
]
