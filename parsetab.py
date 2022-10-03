
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMA CTEF CTEL CTESTRING DIVIDE ELSE EQUAL FLOAT ID IF INT LCURLY LESSTHAN LPAREN MINUS MORETHAN NOTEQUAL NUMBER PLUS PRINT PROGRAM RCURLY RPAREN SEMICOLON TIMES VARprograma : PROGRAM ID SEMICOLON vars bloquevars : VAR var\n            | vars vars\n            | epsilonvar : vardef COLON tipo SEMICOLONvardef : ID\n              | vardef COMA vardeftipo : INT\n            | FLOATbloque : LCURLY estatuto RCURLY estatuto : asignacion \n                | condicion\n                | escritura\n                | epsilonasignacion : ID EQUAL expresion SEMICOLONescritura : PRINT LPAREN escrito RPAREN SEMICOLONescrito : impr\n               | impr COMA imprimpr : CTESTRING\n            | expresionexpresion : exp\n                | comparacion exp\n                | exp expresioncomparacion : LESSTHAN\n                   | MORETHAN\n                   | NOTEQUALcondicion : IF LPAREN expresion RPAREN bloque condicion\n                | ELSE bloque condicion\n                | SEMICOLON\n                | epsilonexp : termino\n           | termino signosigno : PLUS\n             | MINUStermino : factor\n               | factor operacionoperacion : TIMES exp\n                 | DIVIDE expfactor : LPAREN expresion RPAREN\n               | varcte\n               | signo varcteepsilon : varcte : ID \n              | CTEL\n              | CTEF'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,26,],[0,-1,-10,]),'ID':([2,6,10,25,27,28,30,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[3,13,19,13,35,35,35,-43,35,35,-31,35,-24,-25,-26,-35,35,-40,-44,-45,-33,-34,-32,-41,-36,35,35,35,-37,-38,-39,]),'SEMICOLON':([3,10,26,29,31,32,33,35,36,37,39,44,46,47,48,49,50,60,61,62,63,64,69,71,72,73,74,],[4,20,-10,20,58,-8,-9,-43,59,-21,-31,-35,-40,-44,-45,-33,-34,-23,-22,-32,-41,-36,75,-37,-38,-39,20,]),'VAR':([4,5,7,8,11,58,],[6,6,-4,6,-2,-5,]),'LCURLY':([4,5,7,8,11,22,58,68,],[-42,10,-4,-3,-2,10,-5,10,]),'IF':([10,26,29,74,],[21,-10,21,21,]),'ELSE':([10,26,29,74,],[22,-10,22,22,]),'PRINT':([10,],[23,]),'RCURLY':([10,14,15,16,17,18,20,26,29,52,53,59,74,75,77,],[-42,26,-11,-12,-13,-14,-29,-10,-42,-28,-30,-15,-42,-16,-27,]),'COLON':([12,13,34,],[24,-6,-7,]),'COMA':([12,13,34,35,37,39,44,46,47,48,49,50,55,56,57,60,61,62,63,64,71,72,73,],[25,-6,25,-43,-21,-31,-35,-40,-44,-45,-33,-34,70,-19,-20,-23,-22,-32,-41,-36,-37,-38,-39,]),'EQUAL':([19,],[27,]),'LPAREN':([21,23,27,28,30,35,37,38,39,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[28,30,45,45,45,-43,45,45,-31,-24,-25,-26,-35,45,-40,-44,-45,-33,-34,-32,-41,-36,45,45,45,-37,-38,-39,]),'INT':([24,],[32,]),'FLOAT':([24,],[33,]),'LESSTHAN':([27,28,30,35,37,39,44,45,46,47,48,49,50,62,63,64,70,71,72,73,],[41,41,41,-43,41,-31,-35,41,-40,-44,-45,-33,-34,-32,-41,-36,41,-37,-38,-39,]),'MORETHAN':([27,28,30,35,37,39,44,45,46,47,48,49,50,62,63,64,70,71,72,73,],[42,42,42,-43,42,-31,-35,42,-40,-44,-45,-33,-34,-32,-41,-36,42,-37,-38,-39,]),'NOTEQUAL':([27,28,30,35,37,39,44,45,46,47,48,49,50,62,63,64,70,71,72,73,],[43,43,43,-43,43,-31,-35,43,-40,-44,-45,-33,-34,-32,-41,-36,43,-37,-38,-39,]),'CTEL':([27,28,30,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[47,47,47,-43,47,47,-31,47,-24,-25,-26,-35,47,-40,-44,-45,-33,-34,-32,-41,-36,47,47,47,-37,-38,-39,]),'CTEF':([27,28,30,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[48,48,48,-43,48,48,-31,48,-24,-25,-26,-35,48,-40,-44,-45,-33,-34,-32,-41,-36,48,48,48,-37,-38,-39,]),'PLUS':([27,28,30,35,37,38,39,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[49,49,49,-43,49,49,49,-24,-25,-26,-35,49,-40,-44,-45,-33,-34,-32,-41,-36,49,49,49,-37,-38,-39,]),'MINUS':([27,28,30,35,37,38,39,41,42,43,44,45,46,47,48,49,50,62,63,64,65,66,70,71,72,73,],[50,50,50,-43,50,50,50,-24,-25,-26,-35,50,-40,-44,-45,-33,-34,-32,-41,-36,50,50,50,-37,-38,-39,]),'CTESTRING':([30,70,],[56,56,]),'TIMES':([35,44,46,47,48,63,73,],[-43,65,-40,-44,-45,-41,-39,]),'DIVIDE':([35,44,46,47,48,63,73,],[-43,66,-40,-44,-45,-41,-39,]),'RPAREN':([35,37,39,44,46,47,48,49,50,51,54,55,56,57,60,61,62,63,64,67,71,72,73,76,],[-43,-21,-31,-35,-40,-44,-45,-33,-34,68,69,-17,-19,-20,-23,-22,-32,-41,-36,73,-37,-38,-39,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([4,5,8,],[5,8,8,]),'epsilon':([4,5,8,10,29,74,],[7,7,7,18,53,53,]),'bloque':([5,22,68,],[9,29,74,]),'var':([6,],[11,]),'vardef':([6,25,],[12,34,]),'estatuto':([10,],[14,]),'asignacion':([10,],[15,]),'condicion':([10,29,74,],[16,52,77,]),'escritura':([10,],[17,]),'tipo':([24,],[31,]),'expresion':([27,28,30,37,45,70,],[36,51,57,60,67,57,]),'exp':([27,28,30,37,38,45,65,66,70,],[37,37,37,37,61,37,71,72,37,]),'comparacion':([27,28,30,37,45,70,],[38,38,38,38,38,38,]),'termino':([27,28,30,37,38,45,65,66,70,],[39,39,39,39,39,39,39,39,39,]),'signo':([27,28,30,37,38,39,45,65,66,70,],[40,40,40,40,40,62,40,40,40,40,]),'factor':([27,28,30,37,38,45,65,66,70,],[44,44,44,44,44,44,44,44,44,]),'varcte':([27,28,30,37,38,40,45,65,66,70,],[46,46,46,46,46,63,46,46,46,46,]),'escrito':([30,],[54,]),'impr':([30,70,],[55,76,]),'operacion':([44,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON vars bloque','programa',5,'p_programa','ply_yac_example.py',8),
  ('vars -> VAR var','vars',2,'p_vars','ply_yac_example.py',12),
  ('vars -> vars vars','vars',2,'p_vars','ply_yac_example.py',13),
  ('vars -> epsilon','vars',1,'p_vars','ply_yac_example.py',14),
  ('var -> vardef COLON tipo SEMICOLON','var',4,'p_var','ply_yac_example.py',18),
  ('vardef -> ID','vardef',1,'p_vardef','ply_yac_example.py',22),
  ('vardef -> vardef COMA vardef','vardef',3,'p_vardef','ply_yac_example.py',23),
  ('tipo -> INT','tipo',1,'p_tipo','ply_yac_example.py',27),
  ('tipo -> FLOAT','tipo',1,'p_tipo','ply_yac_example.py',28),
  ('bloque -> LCURLY estatuto RCURLY','bloque',3,'p_bloque','ply_yac_example.py',32),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','ply_yac_example.py',36),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','ply_yac_example.py',37),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','ply_yac_example.py',38),
  ('estatuto -> epsilon','estatuto',1,'p_estatuto','ply_yac_example.py',39),
  ('asignacion -> ID EQUAL expresion SEMICOLON','asignacion',4,'p_asignacion','ply_yac_example.py',43),
  ('escritura -> PRINT LPAREN escrito RPAREN SEMICOLON','escritura',5,'p_escritura','ply_yac_example.py',47),
  ('escrito -> impr','escrito',1,'p_escrito','ply_yac_example.py',51),
  ('escrito -> impr COMA impr','escrito',3,'p_escrito','ply_yac_example.py',52),
  ('impr -> CTESTRING','impr',1,'p_impr','ply_yac_example.py',56),
  ('impr -> expresion','impr',1,'p_impr','ply_yac_example.py',57),
  ('expresion -> exp','expresion',1,'p_expresion','ply_yac_example.py',61),
  ('expresion -> comparacion exp','expresion',2,'p_expresion','ply_yac_example.py',62),
  ('expresion -> exp expresion','expresion',2,'p_expresion','ply_yac_example.py',63),
  ('comparacion -> LESSTHAN','comparacion',1,'p_comparacion','ply_yac_example.py',71),
  ('comparacion -> MORETHAN','comparacion',1,'p_comparacion','ply_yac_example.py',72),
  ('comparacion -> NOTEQUAL','comparacion',1,'p_comparacion','ply_yac_example.py',73),
  ('condicion -> IF LPAREN expresion RPAREN bloque condicion','condicion',6,'p_condicion','ply_yac_example.py',77),
  ('condicion -> ELSE bloque condicion','condicion',3,'p_condicion','ply_yac_example.py',78),
  ('condicion -> SEMICOLON','condicion',1,'p_condicion','ply_yac_example.py',79),
  ('condicion -> epsilon','condicion',1,'p_condicion','ply_yac_example.py',80),
  ('exp -> termino','exp',1,'p_exp','ply_yac_example.py',84),
  ('exp -> termino signo','exp',2,'p_exp','ply_yac_example.py',85),
  ('signo -> PLUS','signo',1,'p_signo','ply_yac_example.py',89),
  ('signo -> MINUS','signo',1,'p_signo','ply_yac_example.py',90),
  ('termino -> factor','termino',1,'p_termino','ply_yac_example.py',94),
  ('termino -> factor operacion','termino',2,'p_termino','ply_yac_example.py',95),
  ('operacion -> TIMES exp','operacion',2,'p_operacion','ply_yac_example.py',99),
  ('operacion -> DIVIDE exp','operacion',2,'p_operacion','ply_yac_example.py',100),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','ply_yac_example.py',104),
  ('factor -> varcte','factor',1,'p_factor','ply_yac_example.py',105),
  ('factor -> signo varcte','factor',2,'p_factor','ply_yac_example.py',106),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','ply_yac_example.py',110),
  ('varcte -> ID','varcte',1,'p_varcte','ply_yac_example.py',114),
  ('varcte -> CTEL','varcte',1,'p_varcte','ply_yac_example.py',115),
  ('varcte -> CTEF','varcte',1,'p_varcte','ply_yac_example.py',116),
]
