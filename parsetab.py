
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COLON COMA CTEF CTEL DIFF DIVIDE DO ELSE EQUAL EXP FLOAT FOR FUNCTION ID IF INT ISEQUAL LBRACKET LCURLY LESSTHAN LPAREN MINUS MORETHAN NOTEQUAL OR PLUS PRINT RBRACKET RCURLY RETURN RPAREN SEMICOLON START STRING TIMES VAR VOID WHILEprograma : START LPAREN RPAREN bloquedeclaracion : vars\n                   | epsilonvars : VAR var\n            | vars varsvar : vardef COLON tipo SEMICOLONvardef : IDtipo : INT\n            | FLOAT\n            | BOOL\n            | STRINGlista : ID\n             | ID COMAarreglo : LBRACKET lista RBRACKET bloque : LCURLY declaracion estatutoExp RCURLYestatutoExp : estatuto SEMICOLON\n                    | estatutoExp estatutoExpestatuto : asignacion \n                | condicion\n                | whileLoop\n                | doWhile\n                | forLoop\n                | escritura\n                | funcion\n                | returnexpreturnexp : RETURN expresionasignacion : ID EQUAL expresionescritura : PRINT LPAREN escrito RPARENescrito : impr\n               | impr COMA imprimpr : STRING\n            | expresionexpresion : exp\n                | condition\n                | arreglo condition : exp comparacion expresioncomparacion : LESSTHAN\n                   | MORETHAN\n                   | ISEQUAL\n                   | NOTEQUAL\n                   | AND\n                   | OR doWhile : do bloque WHILE LPAREN expresion RPARENdo : DOwhileLoop : WHILE startCondition expresion endCondition bloquestartCondition : LPAREN\n                     |  SEMICOLONforLoop : FOR LPAREN argumentos startCondition expresion endCondition asignacion RPAREN bloquecondicion : IF LPAREN expresion endCondition bloque condicionelseendCondition : RPAREN\n                    | SEMICOLONcondicionelse : else bloque\n                     | epsilonelse : ELSEfuncion : FUNCTION funcdef LPAREN declaracion RPAREN COLON tiposreturn bloquefuncdef : IDtiposreturn : tipo\n                    | VOIDargumentos : args\n                  | epsilonargs : asignacion\n            | args COMA argsexp : termino\n           | termino signo expsigno : PLUS\n             | MINUStermino : factor\n               | factor operacion terminooperacion : TIMES\n                 | DIVIDE\n                 | DIFF\n                 | EXPfactor : paren expresion paren\n               | varcteparen : LPAREN\n            | RPARENepsilon : varcte : ID \n              | int\n              | float\n              | bool\n              | stringint : INTfloat : FLOATbool : BOOLstring : STRING'
    
_lr_action_items = {'START':([0,],[2,]),'$end':([1,5,35,],[0,-1,-15,]),'LPAREN':([2,22,23,25,26,28,37,38,39,40,41,43,44,45,46,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,72,73,74,75,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,98,108,109,112,114,115,116,118,119,125,],[3,38,40,43,44,56,56,56,56,-46,-47,-77,56,80,-56,-33,-34,-35,-63,-67,56,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-27,108,40,-61,-59,-60,56,-37,-38,-39,-40,-41,-42,56,-65,-66,56,-69,-70,-71,-72,56,56,56,56,-36,-64,-14,-68,-73,-62,]),'RPAREN':([3,8,9,28,30,31,37,38,39,40,41,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,98,108,109,112,113,114,115,116,118,119,120,123,124,126,136,],[4,-2,-3,57,-5,-4,57,57,57,-46,-47,57,-33,-34,-35,-63,-67,57,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-27,105,105,111,-29,-31,-32,-77,57,-37,-38,-39,-40,-41,-42,57,-65,-66,57,-69,-70,-71,-72,57,57,57,57,127,-36,-64,-14,-68,-73,-6,132,105,-30,140,]),'LCURLY':([4,24,29,100,101,102,103,104,105,106,107,129,131,137,138,139,140,],[6,6,-44,-8,-9,-10,-11,6,-50,-51,6,6,-54,6,-57,-58,6,]),'VAR':([6,8,30,31,80,120,],[10,10,10,-4,10,-6,]),'ID':([6,7,8,9,10,11,27,28,30,31,34,36,37,38,39,40,41,43,44,52,54,56,57,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,105,106,108,109,110,112,120,133,],[-77,21,-2,-3,33,21,46,58,-5,-4,21,-16,58,58,58,-46,-47,21,58,92,58,-75,-76,58,-37,-38,-39,-40,-41,-42,58,-65,-66,58,-69,-70,-71,-72,-50,-51,58,58,21,58,-6,21,]),'IF':([6,7,8,9,11,30,31,34,36,120,],[-77,22,-2,-3,22,-5,-4,22,-16,-6,]),'WHILE':([6,7,8,9,11,30,31,34,35,36,42,120,],[-77,23,-2,-3,23,-5,-4,23,-15,-16,71,-6,]),'FOR':([6,7,8,9,11,30,31,34,36,120,],[-77,25,-2,-3,25,-5,-4,25,-16,-6,]),'PRINT':([6,7,8,9,11,30,31,34,36,120,],[-77,26,-2,-3,26,-5,-4,26,-16,-6,]),'FUNCTION':([6,7,8,9,11,30,31,34,36,120,],[-77,27,-2,-3,27,-5,-4,27,-16,-6,]),'RETURN':([6,7,8,9,11,30,31,34,36,120,],[-77,28,-2,-3,28,-5,-4,28,-16,-6,]),'DO':([6,7,8,9,11,30,31,34,36,120,],[-77,29,-2,-3,29,-5,-4,29,-16,-6,]),'RCURLY':([11,34,36,],[35,-17,-16,]),'SEMICOLON':([12,13,14,15,16,17,18,19,20,23,35,43,47,48,49,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,74,75,99,100,101,102,103,111,114,115,116,118,119,121,122,124,125,128,130,132,135,141,142,],[36,-18,-19,-20,-21,-22,-23,-24,-25,41,-15,-77,-26,-33,-34,-35,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-27,106,106,41,-61,-59,-60,120,-8,-9,-10,-11,-28,-36,-64,-14,-68,-73,-77,-45,106,-62,-49,-53,-43,-52,-55,-48,]),'EQUAL':([21,],[37,]),'LBRACKET':([28,37,38,39,40,41,44,54,56,57,81,82,83,84,85,86,87,108,109,112,],[52,52,52,52,-46,-47,52,52,-75,-76,52,-37,-38,-39,-40,-41,-42,52,52,52,]),'INT':([28,37,38,39,40,41,44,54,56,57,67,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,108,109,112,134,],[63,63,63,63,-46,-47,63,63,-75,-76,100,63,-37,-38,-39,-40,-41,-42,63,-65,-66,63,-69,-70,-71,-72,63,63,63,100,]),'FLOAT':([28,37,38,39,40,41,44,54,56,57,67,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,108,109,112,134,],[64,64,64,64,-46,-47,64,64,-75,-76,101,64,-37,-38,-39,-40,-41,-42,64,-65,-66,64,-69,-70,-71,-72,64,64,64,101,]),'BOOL':([28,37,38,39,40,41,44,54,56,57,67,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,108,109,112,134,],[65,65,65,65,-46,-47,65,65,-75,-76,102,65,-37,-38,-39,-40,-41,-42,65,-65,-66,65,-69,-70,-71,-72,65,65,65,102,]),'STRING':([28,37,38,39,40,41,44,54,56,57,67,81,82,83,84,85,86,87,88,89,90,93,94,95,96,97,108,109,112,134,],[66,66,66,66,-46,-47,78,66,-75,-76,103,66,-37,-38,-39,-40,-41,-42,66,-65,-66,66,-69,-70,-71,-72,66,66,78,103,]),'COLON':([32,33,127,],[67,-7,134,]),'ELSE':([35,121,],[-15,131,]),'COMA':([48,49,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,68,73,74,77,78,79,92,114,115,116,118,119,125,],[-33,-34,-35,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-27,-61,110,112,-31,-32,117,-36,-64,-14,-68,-73,110,]),'LESSTHAN':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[82,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'MORETHAN':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[83,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'ISEQUAL':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[84,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'NOTEQUAL':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[85,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'AND':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[86,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'OR':([48,51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,115,118,119,],[87,-63,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-64,-68,-73,]),'PLUS':([51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,118,119,],[89,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-68,-73,]),'MINUS':([51,53,55,56,57,58,59,60,61,62,63,64,65,66,78,118,119,],[90,-67,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-68,-73,]),'TIMES':([53,55,56,57,58,59,60,61,62,63,64,65,66,78,119,],[94,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-73,]),'DIVIDE':([53,55,56,57,58,59,60,61,62,63,64,65,66,78,119,],[95,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-73,]),'DIFF':([53,55,56,57,58,59,60,61,62,63,64,65,66,78,119,],[96,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-73,]),'EXP':([53,55,56,57,58,59,60,61,62,63,64,65,66,78,119,],[97,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-86,-73,]),'RBRACKET':([91,92,117,],[116,-12,-13,]),'VOID':([134,],[139,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque':([4,24,104,107,129,137,140,],[5,42,121,122,135,141,142,]),'declaracion':([6,80,],[7,113,]),'vars':([6,8,30,80,],[8,30,30,8,]),'epsilon':([6,43,80,121,],[9,75,9,130,]),'estatutoExp':([7,11,34,],[11,34,34,]),'estatuto':([7,11,34,],[12,12,12,]),'asignacion':([7,11,34,43,110,133,],[13,13,13,73,73,136,]),'condicion':([7,11,34,],[14,14,14,]),'whileLoop':([7,11,34,],[15,15,15,]),'doWhile':([7,11,34,],[16,16,16,]),'forLoop':([7,11,34,],[17,17,17,]),'escritura':([7,11,34,],[18,18,18,]),'funcion':([7,11,34,],[19,19,19,]),'returnexp':([7,11,34,],[20,20,20,]),'do':([7,11,34,],[24,24,24,]),'var':([10,],[31,]),'vardef':([10,],[32,]),'startCondition':([23,72,],[39,109,]),'funcdef':([27,],[45,]),'expresion':([28,37,38,39,44,54,81,108,109,112,],[47,68,69,70,79,98,114,123,124,79,]),'exp':([28,37,38,39,44,54,81,88,108,109,112,],[48,48,48,48,48,48,48,115,48,48,48,]),'condition':([28,37,38,39,44,54,81,108,109,112,],[49,49,49,49,49,49,49,49,49,49,]),'arreglo':([28,37,38,39,44,54,81,108,109,112,],[50,50,50,50,50,50,50,50,50,50,]),'termino':([28,37,38,39,44,54,81,88,93,108,109,112,],[51,51,51,51,51,51,51,51,118,51,51,51,]),'factor':([28,37,38,39,44,54,81,88,93,108,109,112,],[53,53,53,53,53,53,53,53,53,53,53,53,]),'paren':([28,37,38,39,44,54,81,88,93,98,108,109,112,],[54,54,54,54,54,54,54,54,54,119,54,54,54,]),'varcte':([28,37,38,39,44,54,81,88,93,108,109,112,],[55,55,55,55,55,55,55,55,55,55,55,55,]),'int':([28,37,38,39,44,54,81,88,93,108,109,112,],[59,59,59,59,59,59,59,59,59,59,59,59,]),'float':([28,37,38,39,44,54,81,88,93,108,109,112,],[60,60,60,60,60,60,60,60,60,60,60,60,]),'bool':([28,37,38,39,44,54,81,88,93,108,109,112,],[61,61,61,61,61,61,61,61,61,61,61,61,]),'string':([28,37,38,39,44,54,81,88,93,108,109,112,],[62,62,62,62,62,62,62,62,62,62,62,62,]),'argumentos':([43,],[72,]),'args':([43,110,],[74,125,]),'escrito':([44,],[76,]),'impr':([44,112,],[77,126,]),'comparacion':([48,],[81,]),'signo':([51,],[88,]),'lista':([52,],[91,]),'operacion':([53,],[93,]),'tipo':([67,134,],[99,138,]),'endCondition':([69,70,124,],[104,107,133,]),'condicionelse':([121,],[128,]),'else':([121,],[129,]),'tiposreturn':([134,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> START LPAREN RPAREN bloque','programa',4,'p_programa','ply_sintax.py',16),
  ('declaracion -> vars','declaracion',1,'p_declaracion','ply_sintax.py',22),
  ('declaracion -> epsilon','declaracion',1,'p_declaracion','ply_sintax.py',23),
  ('vars -> VAR var','vars',2,'p_vars','ply_sintax.py',27),
  ('vars -> vars vars','vars',2,'p_vars','ply_sintax.py',28),
  ('var -> vardef COLON tipo SEMICOLON','var',4,'p_var','ply_sintax.py',32),
  ('vardef -> ID','vardef',1,'p_vardef','ply_sintax.py',36),
  ('tipo -> INT','tipo',1,'p_tipo','ply_sintax.py',45),
  ('tipo -> FLOAT','tipo',1,'p_tipo','ply_sintax.py',46),
  ('tipo -> BOOL','tipo',1,'p_tipo','ply_sintax.py',47),
  ('tipo -> STRING','tipo',1,'p_tipo','ply_sintax.py',48),
  ('lista -> ID','lista',1,'p_lista','ply_sintax.py',55),
  ('lista -> ID COMA','lista',2,'p_lista','ply_sintax.py',56),
  ('arreglo -> LBRACKET lista RBRACKET','arreglo',3,'p_arreglo','ply_sintax.py',60),
  ('bloque -> LCURLY declaracion estatutoExp RCURLY','bloque',4,'p_bloque','ply_sintax.py',64),
  ('estatutoExp -> estatuto SEMICOLON','estatutoExp',2,'p_estatutoExp','ply_sintax.py',68),
  ('estatutoExp -> estatutoExp estatutoExp','estatutoExp',2,'p_estatutoExp','ply_sintax.py',69),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','ply_sintax.py',73),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','ply_sintax.py',74),
  ('estatuto -> whileLoop','estatuto',1,'p_estatuto','ply_sintax.py',75),
  ('estatuto -> doWhile','estatuto',1,'p_estatuto','ply_sintax.py',76),
  ('estatuto -> forLoop','estatuto',1,'p_estatuto','ply_sintax.py',77),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','ply_sintax.py',78),
  ('estatuto -> funcion','estatuto',1,'p_estatuto','ply_sintax.py',79),
  ('estatuto -> returnexp','estatuto',1,'p_estatuto','ply_sintax.py',80),
  ('returnexp -> RETURN expresion','returnexp',2,'p_returnexp','ply_sintax.py',84),
  ('asignacion -> ID EQUAL expresion','asignacion',3,'p_asignacion','ply_sintax.py',88),
  ('escritura -> PRINT LPAREN escrito RPAREN','escritura',4,'p_escritura','ply_sintax.py',98),
  ('escrito -> impr','escrito',1,'p_escrito','ply_sintax.py',102),
  ('escrito -> impr COMA impr','escrito',3,'p_escrito','ply_sintax.py',103),
  ('impr -> STRING','impr',1,'p_impr','ply_sintax.py',107),
  ('impr -> expresion','impr',1,'p_impr','ply_sintax.py',108),
  ('expresion -> exp','expresion',1,'p_expresion','ply_sintax.py',112),
  ('expresion -> condition','expresion',1,'p_expresion','ply_sintax.py',113),
  ('expresion -> arreglo','expresion',1,'p_expresion','ply_sintax.py',114),
  ('condition -> exp comparacion expresion','condition',3,'p_condition','ply_sintax.py',122),
  ('comparacion -> LESSTHAN','comparacion',1,'p_comparacion','ply_sintax.py',126),
  ('comparacion -> MORETHAN','comparacion',1,'p_comparacion','ply_sintax.py',127),
  ('comparacion -> ISEQUAL','comparacion',1,'p_comparacion','ply_sintax.py',128),
  ('comparacion -> NOTEQUAL','comparacion',1,'p_comparacion','ply_sintax.py',129),
  ('comparacion -> AND','comparacion',1,'p_comparacion','ply_sintax.py',130),
  ('comparacion -> OR','comparacion',1,'p_comparacion','ply_sintax.py',131),
  ('doWhile -> do bloque WHILE LPAREN expresion RPAREN','doWhile',6,'p_doWhile','ply_sintax.py',136),
  ('do -> DO','do',1,'p_do','ply_sintax.py',142),
  ('whileLoop -> WHILE startCondition expresion endCondition bloque','whileLoop',5,'p_whileLoop','ply_sintax.py',147),
  ('startCondition -> LPAREN','startCondition',1,'p_startCondition','ply_sintax.py',153),
  ('startCondition -> SEMICOLON','startCondition',1,'p_startCondition','ply_sintax.py',154),
  ('forLoop -> FOR LPAREN argumentos startCondition expresion endCondition asignacion RPAREN bloque','forLoop',9,'p_forLoop','ply_sintax.py',159),
  ('condicion -> IF LPAREN expresion endCondition bloque condicionelse','condicion',6,'p_condicion','ply_sintax.py',165),
  ('endCondition -> RPAREN','endCondition',1,'p_endCondition','ply_sintax.py',169),
  ('endCondition -> SEMICOLON','endCondition',1,'p_endCondition','ply_sintax.py',170),
  ('condicionelse -> else bloque','condicionelse',2,'p_condicionelse','ply_sintax.py',175),
  ('condicionelse -> epsilon','condicionelse',1,'p_condicionelse','ply_sintax.py',176),
  ('else -> ELSE','else',1,'p_else','ply_sintax.py',181),
  ('funcion -> FUNCTION funcdef LPAREN declaracion RPAREN COLON tiposreturn bloque','funcion',8,'p_funcion','ply_sintax.py',187),
  ('funcdef -> ID','funcdef',1,'p_funcdef','ply_sintax.py',192),
  ('tiposreturn -> tipo','tiposreturn',1,'p_tiposreturn','ply_sintax.py',198),
  ('tiposreturn -> VOID','tiposreturn',1,'p_tiposreturn','ply_sintax.py',199),
  ('argumentos -> args','argumentos',1,'p_argumentos','ply_sintax.py',205),
  ('argumentos -> epsilon','argumentos',1,'p_argumentos','ply_sintax.py',206),
  ('args -> asignacion','args',1,'p_args','ply_sintax.py',210),
  ('args -> args COMA args','args',3,'p_args','ply_sintax.py',211),
  ('exp -> termino','exp',1,'p_exp','ply_sintax.py',215),
  ('exp -> termino signo exp','exp',3,'p_exp','ply_sintax.py',216),
  ('signo -> PLUS','signo',1,'p_signo','ply_sintax.py',221),
  ('signo -> MINUS','signo',1,'p_signo','ply_sintax.py',222),
  ('termino -> factor','termino',1,'p_termino','ply_sintax.py',228),
  ('termino -> factor operacion termino','termino',3,'p_termino','ply_sintax.py',229),
  ('operacion -> TIMES','operacion',1,'p_operacion','ply_sintax.py',235),
  ('operacion -> DIVIDE','operacion',1,'p_operacion','ply_sintax.py',236),
  ('operacion -> DIFF','operacion',1,'p_operacion','ply_sintax.py',237),
  ('operacion -> EXP','operacion',1,'p_operacion','ply_sintax.py',238),
  ('factor -> paren expresion paren','factor',3,'p_factor','ply_sintax.py',244),
  ('factor -> varcte','factor',1,'p_factor','ply_sintax.py',245),
  ('paren -> LPAREN','paren',1,'p_paren','ply_sintax.py',251),
  ('paren -> RPAREN','paren',1,'p_paren','ply_sintax.py',252),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','ply_sintax.py',265),
  ('varcte -> ID','varcte',1,'p_varcte','ply_sintax.py',269),
  ('varcte -> int','varcte',1,'p_varcte','ply_sintax.py',270),
  ('varcte -> float','varcte',1,'p_varcte','ply_sintax.py',271),
  ('varcte -> bool','varcte',1,'p_varcte','ply_sintax.py',272),
  ('varcte -> string','varcte',1,'p_varcte','ply_sintax.py',273),
  ('int -> INT','int',1,'p_int','ply_sintax.py',282),
  ('float -> FLOAT','float',1,'p_float','ply_sintax.py',288),
  ('bool -> BOOL','bool',1,'p_bool','ply_sintax.py',294),
  ('string -> STRING','string',1,'p_string','ply_sintax.py',300),
]
