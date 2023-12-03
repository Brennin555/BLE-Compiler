
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPERADOR_MAISOPERADOR_MENOSleftOPERADOR_MULTIPLICACAOOPERADOR_DIVISAOABREASPAS ABRECHAVE ABRECOLCHETE ABREPARENTESE ATRIBUICAO ATRIBUIR BLOCO BLOCOS CARACTERE COMENTARIOS DEFVARIAVEL DIGITO E ENQT ESPACO FECHAASPAS FECHACHAVE FECHACOLCHETE FECHAPARENTESE FIM ID IMP INICIO LE LINETERMINATOR LOGICO NAO NUM OPERADOR_DIVISAO OPERADOR_MAIS OPERADOR_MENOS OPERADOR_MULTIPLICACAO OU PONTOEVIRGULA PRA QUEBRALINHA RELACIONAL RESPOSTABOOLEANA SE SENAO SIMBOLO TIPO TXT VET VF VIRGULA\n    programa : inicio\n    \n    inicio : INICIO ABRECHAVE blocos FECHACHAVE\n    \n    le : LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA\n    \n    imp : IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA\n    \n    blocos : bloco blocos\n           | bloco\n    \n    bloco   : enqt\n            | imp\n            | le\n            | atribuir\n            | atribuicao\n            | expressao\n    \n    expressao : ID\n              | NUM\n              | TXT\n              | aritimetico\n              | ABREPARENTESE expressao FECHAPARENTESE\n              | RESPOSTABOOLEANA\n              \n                         \n    aritimetico  : expressao OPERADOR_DIVISAO expressao\n                    | expressao OPERADOR_MULTIPLICACAO expressao\n                    | expressao OPERADOR_MAIS expressao\n                    | expressao OPERADOR_MENOS expressao\n    \n    atribuicao : ATRIBUIR expressao\n               | ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE   \n    \n    atribuir : ID atribuicao PONTOEVIRGULA\n             | TIPO ID atribuicao PONTOEVIRGULA \n             | TIPO ID ATRIBUIR expressao PONTOEVIRGULA \n    \n    condicional : atomica\n                | atomica LOGICO atomica\n    \n    atomica : RESPOSTABOOLEANA\n            | ID\n            | NUM\n            | NAO condicional\n            | condicional RELACIONAL condicional\n            | condicional LOGICO condicional\n     \n    enqt : ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE bloco FECHACHAVE\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,23,],[0,-1,-2,]),'ABRECHAVE':([3,63,],[4,73,]),'ABREPARENTESE':([4,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,25,26,27,28,29,37,41,42,43,44,45,46,47,51,60,61,70,72,73,74,76,78,79,],[13,13,-7,-8,-9,-10,-11,-12,29,37,38,-13,29,-14,-15,-16,-18,29,29,29,29,29,29,-23,29,-13,-19,-20,-21,-22,-17,29,-25,-26,-24,13,-4,-27,-3,-36,]),'IMP':([4,6,7,8,9,10,11,12,17,19,20,21,22,41,43,44,45,46,47,51,61,70,72,73,74,76,78,79,],[14,14,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-18,-23,-13,-19,-20,-21,-22,-17,-25,-26,-24,14,-4,-27,-3,-36,]),'LE':([4,6,7,8,9,10,11,12,17,19,20,21,22,41,43,44,45,46,47,51,61,70,72,73,74,76,78,79,],[15,15,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-18,-23,-13,-19,-20,-21,-22,-17,-25,-26,-24,15,-4,-27,-3,-36,]),'ID':([4,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,25,26,27,28,29,36,37,41,42,43,44,45,46,47,49,50,51,52,58,60,61,70,72,73,74,76,78,79,],[17,17,-7,-8,-9,-10,-11,-12,33,39,-13,43,-14,-15,-16,-18,43,43,43,43,43,55,43,-23,43,-13,-19,-20,-21,-22,55,55,-17,55,69,43,-25,-26,-24,17,-4,-27,-3,-36,]),'TIPO':([4,6,7,8,9,10,11,12,17,19,20,21,22,38,41,43,44,45,46,47,51,61,70,72,73,74,76,78,79,],[16,16,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-18,58,-23,-13,-19,-20,-21,-22,-17,-25,-26,-24,16,-4,-27,-3,-36,]),'ATRIBUIR':([4,6,7,8,9,10,11,12,17,19,20,21,22,39,41,43,44,45,46,47,51,61,70,72,73,74,76,78,79,],[18,18,-7,-8,-9,-10,-11,-12,18,-14,-15,-16,-18,60,-23,-13,-19,-20,-21,-22,-17,-25,-26,-24,18,-4,-27,-3,-36,]),'NUM':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,36,37,41,42,43,44,45,46,47,49,50,51,52,60,61,70,72,73,74,76,78,79,],[19,19,-7,-8,-9,-10,-11,-12,34,-13,19,-14,-15,-16,-18,19,19,19,19,19,56,19,-23,19,-13,-19,-20,-21,-22,56,56,-17,56,19,-25,-26,-24,19,-4,-27,-3,-36,]),'TXT':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,37,41,42,43,44,45,46,47,51,60,61,70,72,73,74,76,78,79,],[20,20,-7,-8,-9,-10,-11,-12,20,-13,20,-14,-15,-16,-18,20,20,20,20,20,20,-23,20,-13,-19,-20,-21,-22,-17,20,-25,-26,-24,20,-4,-27,-3,-36,]),'RESPOSTABOOLEANA':([4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,25,26,27,28,29,36,37,41,42,43,44,45,46,47,49,50,51,52,60,61,70,72,73,74,76,78,79,],[22,22,-7,-8,-9,-10,-11,-12,35,-13,22,-14,-15,-16,-18,22,22,22,22,22,54,22,-23,22,-13,-19,-20,-21,-22,54,54,-17,54,22,-25,-26,-24,22,-4,-27,-3,-36,]),'FECHACHAVE':([5,6,7,8,9,10,11,12,17,19,20,21,22,24,41,43,44,45,46,47,51,61,70,72,74,76,77,78,79,],[23,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-18,-5,-23,-13,-19,-20,-21,-22,-17,-25,-26,-24,-4,-27,79,-3,-36,]),'OPERADOR_DIVISAO':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,62,71,],[25,-13,-14,-15,-16,-18,25,-13,-14,-18,25,-13,-19,-20,25,25,-17,25,25,25,]),'OPERADOR_MULTIPLICACAO':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,62,71,],[26,-13,-14,-15,-16,-18,26,-13,-14,-18,26,-13,-19,-20,26,26,-17,26,26,26,]),'OPERADOR_MAIS':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,62,71,],[27,-13,-14,-15,-16,-18,27,-13,-14,-18,27,-13,-19,-20,-21,-22,-17,27,27,27,]),'OPERADOR_MENOS':([12,17,19,20,21,22,31,33,34,35,41,43,44,45,46,47,51,57,62,71,],[28,-13,-14,-15,-16,-18,28,-13,-14,-18,28,-13,-19,-20,-21,-22,-17,28,28,28,]),'NAO':([13,36,49,50,52,],[36,36,36,36,36,]),'ABRECOLCHETE':([18,60,],[42,42,]),'PONTOEVIRGULA':([19,20,21,22,40,41,43,44,45,46,47,51,59,68,71,72,75,],[-14,-15,-16,-18,61,-23,-13,-19,-20,-21,-22,-17,70,74,76,-24,78,]),'FECHAPARENTESE':([19,20,21,22,30,31,32,33,34,35,43,44,45,46,47,51,53,54,55,56,57,64,65,66,69,],[-14,-15,-16,-18,48,51,-28,-13,-14,-18,-13,-19,-20,-21,-22,-17,-33,-30,-31,-32,68,-34,-35,-29,75,]),'FECHACOLCHETE':([19,20,21,22,43,44,45,46,47,51,62,],[-14,-15,-16,-18,-13,-19,-20,-21,-22,-17,72,]),'RELACIONAL':([30,32,33,34,35,53,54,55,56,64,65,66,67,],[49,-28,-31,-32,-30,49,-30,-31,-32,49,49,-28,49,]),'LOGICO':([30,32,33,34,35,53,54,55,56,64,65,66,67,],[50,52,-31,-32,-30,50,-30,-31,-32,50,50,52,50,]),'ENQT':([48,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'inicio':([0,],[2,]),'blocos':([4,6,],[5,24,]),'bloco':([4,6,73,],[6,6,77,]),'enqt':([4,6,73,],[7,7,7,]),'imp':([4,6,73,],[8,8,8,]),'le':([4,6,73,],[9,9,9,]),'atribuir':([4,6,73,],[10,10,10,]),'atribuicao':([4,6,17,39,73,],[11,11,40,59,11,]),'expressao':([4,6,13,18,25,26,27,28,29,37,42,60,73,],[12,12,31,41,44,45,46,47,31,57,62,71,12,]),'aritimetico':([4,6,13,18,25,26,27,28,29,37,42,60,73,],[21,21,21,21,21,21,21,21,21,21,21,21,21,]),'condicional':([13,36,49,50,52,],[30,53,64,65,67,]),'atomica':([13,36,49,50,52,],[32,32,32,32,66,]),}

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
  ('le -> LE ABREPARENTESE TIPO ID FECHAPARENTESE PONTOEVIRGULA','le',6,'p_le','parser_ble.py',34),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',53),
  ('blocos -> bloco blocos','blocos',2,'p_blocos','parser_ble.py',63),
  ('blocos -> bloco','blocos',1,'p_blocos','parser_ble.py',64),
  ('bloco -> enqt','bloco',1,'p_bloco','parser_ble.py',73),
  ('bloco -> imp','bloco',1,'p_bloco','parser_ble.py',74),
  ('bloco -> le','bloco',1,'p_bloco','parser_ble.py',75),
  ('bloco -> atribuir','bloco',1,'p_bloco','parser_ble.py',76),
  ('bloco -> atribuicao','bloco',1,'p_bloco','parser_ble.py',77),
  ('bloco -> expressao','bloco',1,'p_bloco','parser_ble.py',78),
  ('expressao -> ID','expressao',1,'p_expressao','parser_ble.py',87),
  ('expressao -> NUM','expressao',1,'p_expressao','parser_ble.py',88),
  ('expressao -> TXT','expressao',1,'p_expressao','parser_ble.py',89),
  ('expressao -> aritimetico','expressao',1,'p_expressao','parser_ble.py',90),
  ('expressao -> ABREPARENTESE expressao FECHAPARENTESE','expressao',3,'p_expressao','parser_ble.py',91),
  ('expressao -> RESPOSTABOOLEANA','expressao',1,'p_expressao','parser_ble.py',92),
  ('aritimetico -> expressao OPERADOR_DIVISAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',109),
  ('aritimetico -> expressao OPERADOR_MULTIPLICACAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',110),
  ('aritimetico -> expressao OPERADOR_MAIS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',111),
  ('aritimetico -> expressao OPERADOR_MENOS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',112),
  ('atribuicao -> ATRIBUIR expressao','atribuicao',2,'p_atribuicao','parser_ble.py',128),
  ('atribuicao -> ATRIBUIR ABRECOLCHETE expressao FECHACOLCHETE','atribuicao',4,'p_atribuicao','parser_ble.py',129),
  ('atribuir -> ID atribuicao PONTOEVIRGULA','atribuir',3,'p_atribuir','parser_ble.py',134),
  ('atribuir -> TIPO ID atribuicao PONTOEVIRGULA','atribuir',4,'p_atribuir','parser_ble.py',135),
  ('atribuir -> TIPO ID ATRIBUIR expressao PONTOEVIRGULA','atribuir',5,'p_atribuir','parser_ble.py',136),
  ('condicional -> atomica','condicional',1,'p_condicional','parser_ble.py',150),
  ('condicional -> atomica LOGICO atomica','condicional',3,'p_condicional','parser_ble.py',151),
  ('atomica -> RESPOSTABOOLEANA','atomica',1,'p_condicional_atomica','parser_ble.py',164),
  ('atomica -> ID','atomica',1,'p_condicional_atomica','parser_ble.py',165),
  ('atomica -> NUM','atomica',1,'p_condicional_atomica','parser_ble.py',166),
  ('atomica -> NAO condicional','atomica',2,'p_condicional_atomica','parser_ble.py',167),
  ('atomica -> condicional RELACIONAL condicional','atomica',3,'p_condicional_atomica','parser_ble.py',168),
  ('atomica -> condicional LOGICO condicional','atomica',3,'p_condicional_atomica','parser_ble.py',169),
  ('enqt -> ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE bloco FECHACHAVE','enqt',7,'p_enqt','parser_ble.py',202),
]
