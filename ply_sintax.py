 # Yacc example
import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from ply_lex import tokens
from variables_control import VariableControl
from semantics import Semantics

variables_control = VariableControl()
semantics = Semantics(variables_control)
declaring_variable = [] #Which variable am I declaring
declaring_types = [] #Which variable type am I declaring
opers = []

def p_programa(p):
    '''programa : START LPAREN RPAREN bloque'''
    semantics.endProgram()
    semantics.endStatus()
    pass

def p_declaracion(p):
    '''declaracion : vars
                   | epsilon'''
    pass

def p_vars(p):
    '''vars : VAR var
            | vars vars'''
    pass

def p_var(p):
    '''var : vardef COLON tipo SEMICOLON'''
    pass

def p_vardef(p):
    '''vardef : ID'''
            #   | vardef COMA vardef
    if(variables_control.find_var(p[1]) == None):
        declaring_variable.append(p[1])
    else:
        print('Variable is already declared')
    pass

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | BOOL
            | STRING'''
    if(0<len(declaring_variable)):
        variables_control.add_var(declaring_variable.pop(), p[1])
     #   variables_control.print_table()
    pass

def p_lista(p):
    '''lista : ID
             | ID COMA'''
    pass

def p_arreglo(p):
    '''arreglo : LBRACKET lista RBRACKET '''
    pass

def p_bloque(p):
    '''bloque : LCURLY declaracion estatutoExp RCURLY'''
    pass

def p_estatutoExp(p):
    '''estatutoExp : estatuto SEMICOLON
                    | estatutoExp estatutoExp'''
    pass

def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion
                | whileLoop
                | doWhile
                | forLoop
                | escritura
                | funcion
                | returnexp'''
    pass
                    
def p_returnexp(p):
    '''returnexp : RETURN expresion'''
    pass

def p_asignacion(p):
    '''asignacion : ID EQUAL expresion'''
    if(variables_control.find_var(p[1]) == None):
        print("Error: Variable "+str(p[1])+" is not declared")
    else:
        semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
        semantics.addAssign()
        semantics.checkAssign()
    pass

def p_escritura(p):
    '''escritura : PRINT LPAREN escrito RPAREN'''
    pass

def p_escrito(p):
    '''escrito : impr
               | impr COMA impr'''
    pass

def p_impr(p):
    '''impr : STRING
            | expresion'''
    pass

def p_expresion(p): 
    #a => expresion -> exp-> termino -> factor-> varcte -> ID
    #a<b => expresion -> exp expresion -> exp comparacion exp -> termimno comparacion termino -> factor comparacion factor
    #a+b => expresion -> exp expresion -> exp exp -> termino signo exp -> termino signo termino -> factor signo factor
    #a/b => expresion -> exp expresion -> exp exp -> termino termino -> factor operacion factor
    '''expresion : exp
                | condition
                | arreglo '''
        #       | expresion expresion ''' 

def p_condition(p):
    '''condition : exp comparacion expresion'''
    pass

def p_comparacion(p):
    '''comparacion : LESSTHAN
                   | MORETHAN
                   | ISEQUAL
                   | NOTEQUAL
                   | AND
                   | OR '''
    semantics.addOper(p[1])
    pass

def p_doWhile(p):
   '''doWhile : do bloque WHILE LPAREN expresion RPAREN'''
   semantics.createGoToV()
   semantics.assignCrumb()
   pass

def p_do(p):
   '''do : DO'''
   semantics.addCounterToSaltos()
   pass

def p_whileLoop(p):
   '''whileLoop : WHILE startCondition expresion endCondition bloque'''
   semantics.createGoTo()
   semantics.assignEndLoop()
   pass

def p_startCondition(p):
   '''startCondition : LPAREN
                     |  SEMICOLON'''
   semantics.addCounterToSaltos()
   pass

def p_forLoop(p):
   '''forLoop : FOR LPAREN argumentos startCondition expresion endCondition asignacion RPAREN bloque'''
   semantics.createGoTo()
   semantics.assignEndLoop()
   pass

def p_condicion(p):
    '''condicion : IF LPAREN expresion endCondition bloque condicionelse'''
    pass

def p_endCondition(p):
   '''endCondition : RPAREN
                    | SEMICOLON'''
   semantics.createGoToF()
   pass

def p_condicionelse(p):
    '''condicionelse : else bloque
                     | epsilon''' 
    semantics.assignGoTo()
    pass

def p_else(p):
    '''else : ELSE'''
    semantics.assignGoTo(1)
    semantics.createGoTo()
    pass

def p_funcion(p):
    '''funcion : FUNCTION funcdef LPAREN argumentos RPAREN COLON tiposreturn bloque'''
    variables_control.scope_back()
    pass

def p_funcdef(p):
    '''funcdef : ID'''
    if(not variables_control.is_in_table(p[1])):
        declaring_variable.append(p[1])
    pass

def p_tiposreturn(p):
    '''tiposreturn : tipo
                    | VOID'''
    if(0<len(declaring_variable)):
        variables_control.add_func(declaring_variable.pop(), p[1])
      #  variables_control.print_table()
    pass

def p_argumentos(p):
    '''argumentos : args
                  | epsilon'''
    pass

def p_args(p):
    '''args : asignacion
            | args COMA args'''
    pass

def p_exp(p):
    '''exp : termino
           | termino signo exp'''
    semantics.checkCompare()
    pass

def p_signo(p):
    '''signo : PLUS
             | MINUS'''
 #   print("3", p[1])
    semantics.addOper(p[1])
    pass

def p_termino(p):
    '''termino : factor
               | factor operacion termino'''
 #   print("4", "checkTerm")
    semantics.checkTerm()
    pass

def p_operacion(p):
    '''operacion : TIMES
                 | DIVIDE
                 | DIFF
                 | EXP'''
  #  print("2", p[1])            
    semantics.addOper(p[1])
    pass

def p_factor(p):
    '''factor : paren expresion paren
               | varcte'''
#    print("5", "checkFact")
    semantics.checkFact()
    pass

def p_paren(p):
    '''paren : LPAREN
            | RPAREN'''
    if(p[1]=='('):
#      print("(")
      semantics.addOper(p[1])
    else:
#        print(")")
        semantics.checkFact()
        semantics.checkTerm()
        semantics.checkCompare()
        semantics.checkParen()
    pass

def p_epsilon(p):
    '''epsilon : '''
    pass

def p_varcte(p):
    '''varcte : ID 
              | int
              | float
              | bool
              | string'''
    if (p[1]):
        if variables_control.find_var(p[1]) == None:
            raise ValueError("Variable "+str(p[1])+" is not declared")
        else:
            semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

def p_int(p):
    '''int : INT'''
    variables_control.addConst(p[1], 'int')
    semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

def p_float(p):
    '''float : FLOAT'''
    variables_control.addConst(p[1], 'float')
    semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

def p_bool(p):
    '''bool : BOOL'''
    variables_control.addConst(p[1], 'bool')
    semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

def p_string(p):
    '''string : STRING'''
    variables_control.addConst(p[1], 'string')
    semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc(debug=True)

#fileName = input('Pystachio > ')
with open("test_while.pyst") as f:
    contents = f.read()
    result = parser.parse(contents)
    print("Errors:", result)

# while True:
#     try:
#         s = input('Pystachio > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
 