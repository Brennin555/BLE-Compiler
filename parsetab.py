
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPERADOR_MAISOPERADOR_MENOSleftOPERADOR_MULTIPLICACAOOPERADOR_DIVISAOrightNAOABREASPAS ABRECHAVE ABRECOLCHETE ABREPARENTESE ATRIBUICAO ATRIBUIR BLOCO BLOCOS CARACTERE COMENTARIOS DEFVARIAVEL DIGITO E ENQT ESPACO FECHAASPAS FECHACHAVE FECHACOLCHETE FECHAPARENTESE FIM ID IMP INICIO LE LINETERMINATOR LOGICO NAO NUM OPERADOR_DIVISAO OPERADOR_MAIS OPERADOR_MENOS OPERADOR_MULTIPLICACAO OU PONTOEVIRGULA PRA QUEBRALINHA RELACIONAL RESPOSTABOOLEANA SE SENAO SIMBOLO TIPO TXT VET VF VIRGULA\n    programa : inicio\n    \n    inicio : INICIO ABRECHAVE blocos FECHACHAVE\n    \n    id : ID\n    \n    le : LE ABREPARENTESE TIPO id FECHAPARENTESE PONTOEVIRGULA\n    \n    imp : IMP ABREPARENTESE str FECHAPARENTESE PONTOEVIRGULA\n        | IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA\n    str  : TXT\n    \n    blocos : bloco blocos\n           | bloco\n    \n    comentarios : COMENTARIOS\n    \n    bloco : enqt\n             | pra\n             | se\n             | imp\n             | le\n             | atribuir\n             | atribuicao\n             | comentarios\n    \n    expressao : id\n              | NUM\n              | aritimetico\n              | ABREPARENTESE expressao FECHAPARENTESE\n              | RESPOSTABOOLEANA                     \n    aritimetico  : expressao OPERADOR_DIVISAO expressao\n                    | expressao OPERADOR_MULTIPLICACAO expressao\n                    | expressao OPERADOR_MAIS expressao\n                    | expressao OPERADOR_MENOS expressao\n    \n    atribuicao : ATRIBUIR expressao\n               | ATRIBUIR ABRECOLCHETE lista FECHACOLCHETE   \n    \n    lista : NUM\n          | id\n          | lista VIRGULA lista\n    \n    atribuir : id atribuicao PONTOEVIRGULA\n             | TIPO ID atribuicao PONTOEVIRGULA \n    \n    condicional : atomica\n                | atomica LOGICO atomica\n    \n    atomica : RESPOSTABOOLEANA\n            | NUM\n            | id\n            | NAO condicional\n            | condicional RELACIONAL condicional\n     \n    enqt : ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE blocos FECHACHAVE\n    \n    senao : SENAO ABRECHAVE bloco FECHACHAVE\n    \n    se : SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE\n        | SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE senao\n      \n    pra : PRA ABREPARENTESE id expressao expressao FECHAPARENTESE ABRECHAVE bloco FECHACHAVE\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,25,],[0,-1,-2,]),'ABRECHAVE':([3,66,71,91,99,],[4,83,85,95,101,]),'ABREPARENTESE':([4,6,7,8,9,10,11,12,13,14,16,18,19,20,22,23,24,36,39,41,42,43,44,45,50,51,58,59,60,61,70,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[15,15,-11,-12,-13,-14,-15,-16,-17,-18,33,35,36,37,-3,44,-10,44,-28,-19,-20,-21,44,-23,44,-33,44,44,44,44,44,-34,-24,-25,-26,-27,-29,-22,15,15,-5,-6,-4,-42,15,-44,-45,-46,15,-43,]),'PRA':([4,6,7,8,9,10,11,12,13,14,22,24,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[16,16,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,16,16,-5,-6,-4,-42,16,-44,-45,-46,16,-43,]),'SE':([4,6,7,8,9,10,11,12,13,14,22,24,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[18,18,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,18,18,-5,-6,-4,-42,18,-44,-45,-46,18,-43,]),'IMP':([4,6,7,8,9,10,11,12,13,14,22,24,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[19,19,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,19,19,-5,-6,-4,-42,19,-44,-45,-46,19,-43,]),'LE':([4,6,7,8,9,10,11,12,13,14,22,24,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[20,20,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,20,20,-5,-6,-4,-42,20,-44,-45,-46,20,-43,]),'TIPO':([4,6,7,8,9,10,11,12,13,14,22,24,37,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[21,21,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,56,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,21,21,-5,-6,-4,-42,21,-44,-45,-46,21,-43,]),'ATRIBUIR':([4,6,7,8,9,10,11,12,13,14,17,22,24,38,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[23,23,-11,-12,-13,-14,-15,-16,-17,-18,23,-3,-10,23,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,23,23,-5,-6,-4,-42,23,-44,-45,-46,23,-43,]),'COMENTARIOS':([4,6,7,8,9,10,11,12,13,14,22,24,39,41,42,43,45,51,75,76,77,78,79,80,82,83,85,86,87,93,94,95,96,98,100,101,103,],[24,24,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,24,24,-5,-6,-4,-42,24,-44,-45,-46,24,-43,]),'ID':([4,6,7,8,9,10,11,12,13,14,15,21,22,23,24,32,33,35,36,39,40,41,42,43,44,45,47,48,50,51,56,58,59,60,61,70,75,76,77,78,79,80,81,82,83,85,86,87,93,94,95,96,98,100,101,103,],[22,22,-11,-12,-13,-14,-15,-16,-17,-18,22,38,-3,22,-10,22,22,22,22,-28,22,-19,-20,-21,22,-23,22,22,22,-33,22,22,22,22,22,22,-34,-24,-25,-26,-27,-29,22,-22,22,22,-5,-6,-4,-42,22,-44,-45,-46,22,-43,]),'FECHACHAVE':([5,6,7,8,9,10,11,12,13,14,22,24,26,39,41,42,43,45,51,75,76,77,78,79,80,82,86,87,90,92,93,94,96,97,98,100,102,103,],[25,-9,-11,-12,-13,-14,-15,-16,-17,-18,-3,-10,-8,-28,-19,-20,-21,-23,-33,-34,-24,-25,-26,-27,-29,-22,-5,-6,94,96,-4,-42,-44,100,-45,-46,103,-43,]),'RESPOSTABOOLEANA':([15,22,23,32,35,36,41,42,43,44,45,47,48,50,58,59,60,61,70,76,77,78,79,82,],[29,-3,45,29,29,45,-19,-20,-21,45,-23,29,29,45,45,45,45,45,45,-24,-25,-26,-27,-22,]),'NUM':([15,22,23,32,35,36,40,41,42,43,44,45,47,48,50,58,59,60,61,70,76,77,78,79,81,82,],[30,-3,42,30,30,42,63,-19,-20,-21,42,-23,30,30,42,42,42,42,42,42,-24,-25,-26,-27,63,-22,]),'NAO':([15,32,35,47,48,],[32,32,32,32,32,]),'LOGICO':([22,28,29,30,31,49,67,68,],[-3,48,-37,-38,-39,-40,-41,48,]),'FECHAPARENTESE':([22,27,28,29,30,31,41,42,43,45,49,52,53,54,55,65,67,68,74,76,77,78,79,82,84,],[-3,46,-35,-37,-38,-39,-19,-20,-21,-23,-40,71,72,73,-7,82,-41,-36,88,-24,-25,-26,-27,-22,91,]),'RELACIONAL':([22,27,28,29,30,31,49,52,67,68,69,],[-3,47,-35,-37,-38,-39,-40,47,47,-35,47,]),'OPERADOR_DIVISAO':([22,39,41,42,43,45,54,65,70,76,77,78,79,82,84,],[-3,58,-19,-20,-21,-23,58,58,58,-24,-25,58,58,-22,58,]),'OPERADOR_MULTIPLICACAO':([22,39,41,42,43,45,54,65,70,76,77,78,79,82,84,],[-3,59,-19,-20,-21,-23,59,59,59,-24,-25,59,59,-22,59,]),'OPERADOR_MAIS':([22,39,41,42,43,45,54,65,70,76,77,78,79,82,84,],[-3,60,-19,-20,-21,-23,60,60,60,-24,-25,-26,-27,-22,60,]),'OPERADOR_MENOS':([22,39,41,42,43,45,54,65,70,76,77,78,79,82,84,],[-3,61,-19,-20,-21,-23,61,61,61,-24,-25,-26,-27,-22,61,]),'PONTOEVIRGULA':([22,34,39,41,42,43,45,57,72,73,76,77,78,79,80,82,88,],[-3,51,-28,-19,-20,-21,-23,75,86,87,-24,-25,-26,-27,-29,-22,93,]),'FECHACOLCHETE':([22,62,63,64,89,],[-3,80,-30,-31,-32,]),'VIRGULA':([22,62,63,64,89,],[-3,81,-30,-31,81,]),'ABRECOLCHETE':([23,],[40,]),'TXT':([36,],[55,]),'ENQT':([46,],[66,]),'SENAO':([96,],[99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'inicio':([0,],[2,]),'blocos':([4,6,83,85,],[5,26,90,92,]),'bloco':([4,6,83,85,95,101,],[6,6,6,6,97,102,]),'enqt':([4,6,83,85,95,101,],[7,7,7,7,7,7,]),'pra':([4,6,83,85,95,101,],[8,8,8,8,8,8,]),'se':([4,6,83,85,95,101,],[9,9,9,9,9,9,]),'imp':([4,6,83,85,95,101,],[10,10,10,10,10,10,]),'le':([4,6,83,85,95,101,],[11,11,11,11,11,11,]),'atribuir':([4,6,83,85,95,101,],[12,12,12,12,12,12,]),'atribuicao':([4,6,17,38,83,85,95,101,],[13,13,34,57,13,13,13,13,]),'comentarios':([4,6,83,85,95,101,],[14,14,14,14,14,14,]),'id':([4,6,15,23,32,33,35,36,40,44,47,48,50,56,58,59,60,61,70,81,83,85,95,101,],[17,17,31,41,31,50,31,41,64,41,31,31,41,74,41,41,41,41,41,64,17,17,17,17,]),'condicional':([15,32,35,47,48,],[27,49,52,67,69,]),'atomica':([15,32,35,47,48,],[28,28,28,28,68,]),'expressao':([23,36,44,50,58,59,60,61,70,],[39,54,65,70,76,77,78,79,84,]),'aritimetico':([23,36,44,50,58,59,60,61,70,],[43,43,43,43,43,43,43,43,43,]),'str':([36,],[53,]),'lista':([40,81,],[62,89,]),'senao':([96,],[98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> inicio','programa',1,'p_programa','parser_ble.py',19),
  ('inicio -> INICIO ABRECHAVE blocos FECHACHAVE','inicio',4,'p_inicio','parser_ble.py',27),
  ('id -> ID','id',1,'p_id','parser_ble.py',41),
  ('le -> LE ABREPARENTESE TIPO id FECHAPARENTESE PONTOEVIRGULA','le',6,'p_le','parser_ble.py',52),
  ('imp -> IMP ABREPARENTESE str FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',66),
  ('imp -> IMP ABREPARENTESE expressao FECHAPARENTESE PONTOEVIRGULA','imp',5,'p_imp','parser_ble.py',67),
  ('str -> TXT','str',1,'p_str','parser_ble.py',76),
  ('blocos -> bloco blocos','blocos',2,'p_blocos','parser_ble.py',82),
  ('blocos -> bloco','blocos',1,'p_blocos','parser_ble.py',83),
  ('comentarios -> COMENTARIOS','comentarios',1,'p_comentarios','parser_ble.py',95),
  ('bloco -> enqt','bloco',1,'p_bloco','parser_ble.py',101),
  ('bloco -> pra','bloco',1,'p_bloco','parser_ble.py',102),
  ('bloco -> se','bloco',1,'p_bloco','parser_ble.py',103),
  ('bloco -> imp','bloco',1,'p_bloco','parser_ble.py',104),
  ('bloco -> le','bloco',1,'p_bloco','parser_ble.py',105),
  ('bloco -> atribuir','bloco',1,'p_bloco','parser_ble.py',106),
  ('bloco -> atribuicao','bloco',1,'p_bloco','parser_ble.py',107),
  ('bloco -> comentarios','bloco',1,'p_bloco','parser_ble.py',108),
  ('expressao -> id','expressao',1,'p_expressao','parser_ble.py',117),
  ('expressao -> NUM','expressao',1,'p_expressao','parser_ble.py',118),
  ('expressao -> aritimetico','expressao',1,'p_expressao','parser_ble.py',119),
  ('expressao -> ABREPARENTESE expressao FECHAPARENTESE','expressao',3,'p_expressao','parser_ble.py',120),
  ('expressao -> RESPOSTABOOLEANA','expressao',1,'p_expressao','parser_ble.py',121),
  ('aritimetico -> expressao OPERADOR_DIVISAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',136),
  ('aritimetico -> expressao OPERADOR_MULTIPLICACAO expressao','aritimetico',3,'p_aritimetico','parser_ble.py',137),
  ('aritimetico -> expressao OPERADOR_MAIS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',138),
  ('aritimetico -> expressao OPERADOR_MENOS expressao','aritimetico',3,'p_aritimetico','parser_ble.py',139),
  ('atribuicao -> ATRIBUIR expressao','atribuicao',2,'p_atribuicao','parser_ble.py',153),
  ('atribuicao -> ATRIBUIR ABRECOLCHETE lista FECHACOLCHETE','atribuicao',4,'p_atribuicao','parser_ble.py',154),
  ('lista -> NUM','lista',1,'p_lista','parser_ble.py',163),
  ('lista -> id','lista',1,'p_lista','parser_ble.py',164),
  ('lista -> lista VIRGULA lista','lista',3,'p_lista','parser_ble.py',165),
  ('atribuir -> id atribuicao PONTOEVIRGULA','atribuir',3,'p_atribuir','parser_ble.py',174),
  ('atribuir -> TIPO ID atribuicao PONTOEVIRGULA','atribuir',4,'p_atribuir','parser_ble.py',175),
  ('condicional -> atomica','condicional',1,'p_condicional','parser_ble.py',190),
  ('condicional -> atomica LOGICO atomica','condicional',3,'p_condicional','parser_ble.py',191),
  ('atomica -> RESPOSTABOOLEANA','atomica',1,'p_condicional_atomica','parser_ble.py',204),
  ('atomica -> NUM','atomica',1,'p_condicional_atomica','parser_ble.py',205),
  ('atomica -> id','atomica',1,'p_condicional_atomica','parser_ble.py',206),
  ('atomica -> NAO condicional','atomica',2,'p_condicional_atomica','parser_ble.py',207),
  ('atomica -> condicional RELACIONAL condicional','atomica',3,'p_condicional_atomica','parser_ble.py',208),
  ('enqt -> ABREPARENTESE condicional FECHAPARENTESE ENQT ABRECHAVE blocos FECHACHAVE','enqt',7,'p_enqt','parser_ble.py',242),
  ('senao -> SENAO ABRECHAVE bloco FECHACHAVE','senao',4,'p_senao','parser_ble.py',253),
  ('se -> SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE','se',7,'p_se','parser_ble.py',262),
  ('se -> SE ABREPARENTESE condicional FECHAPARENTESE ABRECHAVE blocos FECHACHAVE senao','se',8,'p_se','parser_ble.py',263),
  ('pra -> PRA ABREPARENTESE id expressao expressao FECHAPARENTESE ABRECHAVE bloco FECHACHAVE','pra',9,'p_pra','parser_ble.py',275),
]
