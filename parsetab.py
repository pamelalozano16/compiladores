
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COLON COMA CTEF CTEL DIFF DIVIDE ELSE EQUAL EXP FLOAT FOR FUNCTION ID IF INT ISEQUAL LBRACKET LCURLY LESSTHAN LPAREN MINUS MORETHAN NOTEQUAL OR PLUS PRINT RBRACKET RCURLY RETURN RPAREN SEMICOLON START STRING TIMES VAR VOID WHILEprograma : START LPAREN RPAREN bloquedeclaracion : vars\n                   | epsilonvars : VAR var\n            | vars varsvar : vardef COLON tipo SEMICOLONvardef : IDtipo : INT\n            | FLOAT\n            | BOOL\n            | STRINGlista : ID\n             | ID COMAarreglo : LBRACKET lista RBRACKET bloque : LCURLY declaracion estatutoExp RCURLYestatutoExp : estatuto SEMICOLON\n                    | estatutoExp estatutoExpestatuto : asignacion \n                | condicion\n                | whileLoop\n                | forLoop\n                | escritura\n                | funcion\n                | returnexpreturnexp : RETURN expresionasignacion : ID EQUAL expresionescritura : PRINT LPAREN escrito RPARENescrito : impr\n               | impr COMA imprimpr : STRING\n            | expresionexpresion : exp\n                | comparacion exp\n                | AND exp\n                | OR exp\n                | arreglo comparacion : LESSTHAN\n                   | MORETHAN\n                   | ISEQUAL\n                   | NOTEQUALwhileLoop : WHILE LPAREN expresion RPAREN bloqueforLoop : FOR LPAREN argumentos expresion SEMICOLON expresion RPAREN bloquecondicion : IF LPAREN expresion RPAREN bloque condicionelsecondicionelse : ELSE bloque\n                     | epsilonfuncion : FUNCTION funcdef LPAREN argumentos RPAREN COLON tiposreturn bloquefuncdef : IDtiposreturn : tipo\n                    | VOIDargumentos : args\n                  | epsilonargs : ID COLON tipo\n            | args COMA argsexp : termino\n           | termino signo expsigno : PLUS\n             | MINUStermino : factor\n               | factor operacion terminooperacion : TIMES\n                 | DIVIDE\n                 | DIFF\n                 | EXPfactor : paren expresion paren\n               | varcteparen : LPAREN\n            | RPARENepsilon : varcte : ID \n              | CTEL\n              | CTEF'
    
_lr_action_items = {'START':([0,],[2,]),'$end':([1,5,32,],[0,-1,-15,]),'LPAREN':([2,21,22,23,24,26,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,65,66,67,74,75,76,77,78,79,82,83,84,85,86,87,89,90,91,92,99,101,102,104,105,109,110,111,],[3,35,36,37,38,56,56,56,56,-68,56,73,-47,-32,56,56,56,-36,-54,-37,-38,-39,-40,-58,56,-65,-66,-67,-69,-70,-71,56,-50,-51,-33,-34,-35,56,-56,-57,56,-60,-61,-62,-63,56,-8,-9,-10,-11,56,-55,-14,-59,-64,56,-53,-52,]),'RPAREN':([3,26,34,35,36,37,38,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,82,83,84,85,86,87,89,90,91,92,99,100,101,102,104,105,109,110,111,112,117,],[4,57,57,57,57,-68,57,-32,57,57,57,-36,-54,-37,-38,-39,-40,-58,57,-65,-66,-67,-69,-70,-71,93,94,57,-50,-51,98,-28,-30,-31,-68,-33,-34,-35,57,-56,-57,57,-60,-61,-62,-63,57,-8,-9,-10,-11,57,113,-55,-14,-59,-64,57,-53,-52,-29,120,]),'LCURLY':([4,89,90,91,92,93,94,115,120,121,122,123,],[6,-8,-9,-10,-11,6,6,6,6,6,-48,-49,]),'VAR':([6,8,27,28,106,],[10,10,10,-4,-6,]),'ID':([6,7,8,9,10,11,25,26,27,28,31,33,34,35,36,37,38,43,44,45,48,49,50,51,52,54,56,57,65,66,67,73,77,78,79,82,83,84,85,86,89,90,91,92,96,99,106,109,110,111,],[-68,20,-2,-3,30,20,40,58,-5,-4,20,-16,58,58,58,68,58,58,58,58,-37,-38,-39,-40,81,58,-66,-67,58,-50,-51,68,58,-56,-57,58,-60,-61,-62,-63,-8,-9,-10,-11,68,58,-6,58,-53,-52,]),'IF':([6,7,8,9,11,27,28,31,33,106,],[-68,21,-2,-3,21,-5,-4,21,-16,-6,]),'WHILE':([6,7,8,9,11,27,28,31,33,106,],[-68,22,-2,-3,22,-5,-4,22,-16,-6,]),'FOR':([6,7,8,9,11,27,28,31,33,106,],[-68,23,-2,-3,23,-5,-4,23,-16,-6,]),'PRINT':([6,7,8,9,11,27,28,31,33,106,],[-68,24,-2,-3,24,-5,-4,24,-16,-6,]),'FUNCTION':([6,7,8,9,11,27,28,31,33,106,],[-68,25,-2,-3,25,-5,-4,25,-16,-6,]),'RETURN':([6,7,8,9,11,27,28,31,33,106,],[-68,26,-2,-3,26,-5,-4,26,-16,-6,]),'RCURLY':([11,31,33,],[32,-17,-16,]),'SEMICOLON':([12,13,14,15,16,17,18,19,32,41,42,46,47,53,55,56,57,58,59,60,62,74,75,76,88,89,90,91,92,95,98,101,102,104,105,107,108,114,116,119,124,125,],[33,-18,-19,-20,-21,-22,-23,-24,-15,-25,-32,-36,-54,-58,-65,-66,-67,-69,-70,-71,-26,-33,-34,-35,106,-8,-9,-10,-11,109,-27,-55,-14,-59,-64,-68,-41,-43,-45,-44,-42,-46,]),'EQUAL':([20,],[34,]),'AND':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[44,44,44,44,-68,44,44,-66,-67,44,-50,-51,-8,-9,-10,-11,44,44,-53,-52,]),'OR':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[45,45,45,45,-68,45,45,-66,-67,45,-50,-51,-8,-9,-10,-11,45,45,-53,-52,]),'LESSTHAN':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[48,48,48,48,-68,48,48,-66,-67,48,-50,-51,-8,-9,-10,-11,48,48,-53,-52,]),'MORETHAN':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[49,49,49,49,-68,49,49,-66,-67,49,-50,-51,-8,-9,-10,-11,49,49,-53,-52,]),'ISEQUAL':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[50,50,50,50,-68,50,50,-66,-67,50,-50,-51,-8,-9,-10,-11,50,50,-53,-52,]),'NOTEQUAL':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[51,51,51,51,-68,51,51,-66,-67,51,-50,-51,-8,-9,-10,-11,51,51,-53,-52,]),'LBRACKET':([26,34,35,36,37,38,54,56,57,65,66,67,89,90,91,92,99,109,110,111,],[52,52,52,52,-68,52,52,-66,-67,52,-50,-51,-8,-9,-10,-11,52,52,-53,-52,]),'CTEL':([26,34,35,36,37,38,43,44,45,48,49,50,51,54,56,57,65,66,67,77,78,79,82,83,84,85,86,89,90,91,92,99,109,110,111,],[59,59,59,59,-68,59,59,59,59,-37,-38,-39,-40,59,-66,-67,59,-50,-51,59,-56,-57,59,-60,-61,-62,-63,-8,-9,-10,-11,59,59,-53,-52,]),'CTEF':([26,34,35,36,37,38,43,44,45,48,49,50,51,54,56,57,65,66,67,77,78,79,82,83,84,85,86,89,90,91,92,99,109,110,111,],[60,60,60,60,-68,60,60,60,60,-37,-38,-39,-40,60,-66,-67,60,-50,-51,60,-56,-57,60,-60,-61,-62,-63,-8,-9,-10,-11,60,60,-53,-52,]),'COLON':([29,30,68,113,],[61,-7,97,118,]),'ELSE':([32,107,],[-15,115,]),'STRING':([38,61,97,99,118,],[71,92,92,71,92,]),'COMA':([42,46,47,53,55,56,57,58,59,60,66,70,71,72,74,75,76,81,89,90,91,92,101,102,104,105,110,111,],[-32,-36,-54,-58,-65,-66,-67,-69,-70,-71,96,99,-30,-31,-33,-34,-35,103,-8,-9,-10,-11,-55,-14,-59,-64,96,-52,]),'PLUS':([47,53,55,56,57,58,59,60,104,105,],[78,-58,-65,-66,-67,-69,-70,-71,-59,-64,]),'MINUS':([47,53,55,56,57,58,59,60,104,105,],[79,-58,-65,-66,-67,-69,-70,-71,-59,-64,]),'TIMES':([53,55,56,57,58,59,60,105,],[83,-65,-66,-67,-69,-70,-71,-64,]),'DIVIDE':([53,55,56,57,58,59,60,105,],[84,-65,-66,-67,-69,-70,-71,-64,]),'DIFF':([53,55,56,57,58,59,60,105,],[85,-65,-66,-67,-69,-70,-71,-64,]),'EXP':([53,55,56,57,58,59,60,105,],[86,-65,-66,-67,-69,-70,-71,-64,]),'INT':([61,97,118,],[89,89,89,]),'FLOAT':([61,97,118,],[90,90,90,]),'BOOL':([61,97,118,],[91,91,91,]),'RBRACKET':([80,81,103,],[102,-12,-13,]),'VOID':([118,],[123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque':([4,93,94,115,120,121,],[5,107,108,119,124,125,]),'declaracion':([6,],[7,]),'vars':([6,8,27,],[8,27,27,]),'epsilon':([6,37,73,107,],[9,67,67,116,]),'estatutoExp':([7,11,31,],[11,31,31,]),'estatuto':([7,11,31,],[12,12,12,]),'asignacion':([7,11,31,],[13,13,13,]),'condicion':([7,11,31,],[14,14,14,]),'whileLoop':([7,11,31,],[15,15,15,]),'forLoop':([7,11,31,],[16,16,16,]),'escritura':([7,11,31,],[17,17,17,]),'funcion':([7,11,31,],[18,18,18,]),'returnexp':([7,11,31,],[19,19,19,]),'var':([10,],[28,]),'vardef':([10,],[29,]),'funcdef':([25,],[39,]),'expresion':([26,34,35,36,38,54,65,99,109,],[41,62,63,64,72,87,95,72,117,]),'exp':([26,34,35,36,38,43,44,45,54,65,77,99,109,],[42,42,42,42,42,74,75,76,42,42,101,42,42,]),'comparacion':([26,34,35,36,38,54,65,99,109,],[43,43,43,43,43,43,43,43,43,]),'arreglo':([26,34,35,36,38,54,65,99,109,],[46,46,46,46,46,46,46,46,46,]),'termino':([26,34,35,36,38,43,44,45,54,65,77,82,99,109,],[47,47,47,47,47,47,47,47,47,47,47,104,47,47,]),'factor':([26,34,35,36,38,43,44,45,54,65,77,82,99,109,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'paren':([26,34,35,36,38,43,44,45,54,65,77,82,87,99,109,],[54,54,54,54,54,54,54,54,54,54,54,54,105,54,54,]),'varcte':([26,34,35,36,38,43,44,45,54,65,77,82,99,109,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'argumentos':([37,73,],[65,100,]),'args':([37,73,96,],[66,66,110,]),'escrito':([38,],[69,]),'impr':([38,99,],[70,112,]),'signo':([47,],[77,]),'lista':([52,],[80,]),'operacion':([53,],[82,]),'tipo':([61,97,118,],[88,111,122,]),'condicionelse':([107,],[114,]),'tiposreturn':([118,],[121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> START LPAREN RPAREN bloque','programa',4,'p_programa','ply_sintax.py',16),
  ('declaracion -> vars','declaracion',1,'p_declaracion','ply_sintax.py',20),
  ('declaracion -> epsilon','declaracion',1,'p_declaracion','ply_sintax.py',21),
  ('vars -> VAR var','vars',2,'p_vars','ply_sintax.py',25),
  ('vars -> vars vars','vars',2,'p_vars','ply_sintax.py',26),
  ('var -> vardef COLON tipo SEMICOLON','var',4,'p_var','ply_sintax.py',30),
  ('vardef -> ID','vardef',1,'p_vardef','ply_sintax.py',34),
  ('tipo -> INT','tipo',1,'p_tipo','ply_sintax.py',43),
  ('tipo -> FLOAT','tipo',1,'p_tipo','ply_sintax.py',44),
  ('tipo -> BOOL','tipo',1,'p_tipo','ply_sintax.py',45),
  ('tipo -> STRING','tipo',1,'p_tipo','ply_sintax.py',46),
  ('lista -> ID','lista',1,'p_lista','ply_sintax.py',53),
  ('lista -> ID COMA','lista',2,'p_lista','ply_sintax.py',54),
  ('arreglo -> LBRACKET lista RBRACKET','arreglo',3,'p_arreglo','ply_sintax.py',58),
  ('bloque -> LCURLY declaracion estatutoExp RCURLY','bloque',4,'p_bloque','ply_sintax.py',62),
  ('estatutoExp -> estatuto SEMICOLON','estatutoExp',2,'p_estatutoExp','ply_sintax.py',66),
  ('estatutoExp -> estatutoExp estatutoExp','estatutoExp',2,'p_estatutoExp','ply_sintax.py',67),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','ply_sintax.py',71),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','ply_sintax.py',72),
  ('estatuto -> whileLoop','estatuto',1,'p_estatuto','ply_sintax.py',73),
  ('estatuto -> forLoop','estatuto',1,'p_estatuto','ply_sintax.py',74),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','ply_sintax.py',75),
  ('estatuto -> funcion','estatuto',1,'p_estatuto','ply_sintax.py',76),
  ('estatuto -> returnexp','estatuto',1,'p_estatuto','ply_sintax.py',77),
  ('returnexp -> RETURN expresion','returnexp',2,'p_returnexp','ply_sintax.py',81),
  ('asignacion -> ID EQUAL expresion','asignacion',3,'p_asignacion','ply_sintax.py',85),
  ('escritura -> PRINT LPAREN escrito RPAREN','escritura',4,'p_escritura','ply_sintax.py',95),
  ('escrito -> impr','escrito',1,'p_escrito','ply_sintax.py',99),
  ('escrito -> impr COMA impr','escrito',3,'p_escrito','ply_sintax.py',100),
  ('impr -> STRING','impr',1,'p_impr','ply_sintax.py',104),
  ('impr -> expresion','impr',1,'p_impr','ply_sintax.py',105),
  ('expresion -> exp','expresion',1,'p_expresion','ply_sintax.py',109),
  ('expresion -> comparacion exp','expresion',2,'p_expresion','ply_sintax.py',110),
  ('expresion -> AND exp','expresion',2,'p_expresion','ply_sintax.py',111),
  ('expresion -> OR exp','expresion',2,'p_expresion','ply_sintax.py',112),
  ('expresion -> arreglo','expresion',1,'p_expresion','ply_sintax.py',113),
  ('comparacion -> LESSTHAN','comparacion',1,'p_comparacion','ply_sintax.py',121),
  ('comparacion -> MORETHAN','comparacion',1,'p_comparacion','ply_sintax.py',122),
  ('comparacion -> ISEQUAL','comparacion',1,'p_comparacion','ply_sintax.py',123),
  ('comparacion -> NOTEQUAL','comparacion',1,'p_comparacion','ply_sintax.py',124),
  ('whileLoop -> WHILE LPAREN expresion RPAREN bloque','whileLoop',5,'p_whileLoop','ply_sintax.py',128),
  ('forLoop -> FOR LPAREN argumentos expresion SEMICOLON expresion RPAREN bloque','forLoop',8,'p_forLoop','ply_sintax.py',131),
  ('condicion -> IF LPAREN expresion RPAREN bloque condicionelse','condicion',6,'p_condicion','ply_sintax.py',134),
  ('condicionelse -> ELSE bloque','condicionelse',2,'p_condicionelse','ply_sintax.py',138),
  ('condicionelse -> epsilon','condicionelse',1,'p_condicionelse','ply_sintax.py',139),
  ('funcion -> FUNCTION funcdef LPAREN argumentos RPAREN COLON tiposreturn bloque','funcion',8,'p_funcion','ply_sintax.py',143),
  ('funcdef -> ID','funcdef',1,'p_funcdef','ply_sintax.py',148),
  ('tiposreturn -> tipo','tiposreturn',1,'p_tiposreturn','ply_sintax.py',154),
  ('tiposreturn -> VOID','tiposreturn',1,'p_tiposreturn','ply_sintax.py',155),
  ('argumentos -> args','argumentos',1,'p_argumentos','ply_sintax.py',162),
  ('argumentos -> epsilon','argumentos',1,'p_argumentos','ply_sintax.py',163),
  ('args -> ID COLON tipo','args',3,'p_args','ply_sintax.py',167),
  ('args -> args COMA args','args',3,'p_args','ply_sintax.py',168),
  ('exp -> termino','exp',1,'p_exp','ply_sintax.py',172),
  ('exp -> termino signo exp','exp',3,'p_exp','ply_sintax.py',173),
  ('signo -> PLUS','signo',1,'p_signo','ply_sintax.py',177),
  ('signo -> MINUS','signo',1,'p_signo','ply_sintax.py',178),
  ('termino -> factor','termino',1,'p_termino','ply_sintax.py',184),
  ('termino -> factor operacion termino','termino',3,'p_termino','ply_sintax.py',185),
  ('operacion -> TIMES','operacion',1,'p_operacion','ply_sintax.py',191),
  ('operacion -> DIVIDE','operacion',1,'p_operacion','ply_sintax.py',192),
  ('operacion -> DIFF','operacion',1,'p_operacion','ply_sintax.py',193),
  ('operacion -> EXP','operacion',1,'p_operacion','ply_sintax.py',194),
  ('factor -> paren expresion paren','factor',3,'p_factor','ply_sintax.py',200),
  ('factor -> varcte','factor',1,'p_factor','ply_sintax.py',201),
  ('paren -> LPAREN','paren',1,'p_paren','ply_sintax.py',207),
  ('paren -> RPAREN','paren',1,'p_paren','ply_sintax.py',208),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','ply_sintax.py',214),
  ('varcte -> ID','varcte',1,'p_varcte','ply_sintax.py',218),
  ('varcte -> CTEL','varcte',1,'p_varcte','ply_sintax.py',219),
  ('varcte -> CTEF','varcte',1,'p_varcte','ply_sintax.py',220),
]
