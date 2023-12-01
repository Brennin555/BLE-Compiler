
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEDIVIDE MINUS NUMBER NUMTXTVETVFDEFVARIAVELIMPLECONDICIONALENQTPRACCNNBLOCOATRIBUICAOOPERACAOVERDADEIROFALSOMAINCOMENTARIO PLUS TIMES\n    expression : expression PLUS term\n               | expression MINUS term\n               | term\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n         | factor\n    \n    factor : NUMBER\n    '
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,],[4,4,4,4,4,]),'$end':([1,2,3,4,9,10,11,12,],[0,-3,-6,-7,-1,-2,-4,-5,]),'PLUS':([1,2,3,4,9,10,11,12,],[5,-3,-6,-7,-1,-2,-4,-5,]),'MINUS':([1,2,3,4,9,10,11,12,],[6,-3,-6,-7,-1,-2,-4,-5,]),'TIMES':([2,3,4,9,10,11,12,],[7,-6,-7,7,7,-4,-5,]),'DIVIDE':([2,3,4,9,10,11,12,],[8,-6,-7,8,8,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'term':([0,5,6,],[2,9,10,]),'factor':([0,5,6,7,8,],[3,3,3,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression','calc.py',180),
  ('expression -> expression MINUS term','expression',3,'p_expression','calc.py',181),
  ('expression -> term','expression',1,'p_expression','calc.py',182),
  ('term -> term TIMES factor','term',3,'p_term','calc.py',195),
  ('term -> term DIVIDE factor','term',3,'p_term','calc.py',196),
  ('term -> factor','term',1,'p_term','calc.py',197),
  ('factor -> NUMBER','factor',1,'p_factor','calc.py',210),
]
