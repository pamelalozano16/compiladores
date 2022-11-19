# Yacc example
import ply.yacc as yacc
import sys
 
 # Get the token map from the lexer.  This is required.
from ply_lex import tokens
from variables_control import VariableControl
from semantics import Semantics
from maquina_virtual import MaquinaVirtual

variables_control = VariableControl()
maquina_virtual = MaquinaVirtual()
semantics = Semantics(variables_control)
declaring_variable = [] #Which variable am I declaring
declaring_types = [] #Which variable type am I declaring
declaring_array = []
opers = []

def p_programa(p):
    '''programa : START LPAREN RPAREN bloque'''
    semantics.endProgram()
    semantics.endStatus()
    maquina_virtual.run()
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
    '''var : vardef COLON tipo SEMICOLON
           | declaracionArr SEMICOLON
           | declaracionMatrix SEMICOLON'''
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
        variables_control.add_var(declaring_variable.pop(), p[1], 0<len(declaring_array))
     #   variables_control.print_table()
    pass

def p_bloque(p):
    '''bloque : LCURLY declaracion estatutoExp RCURLY'''
    pass

def p_bloqueReturn(p):
    '''bloqueReturn : LCURLY declaracion estatutoExp returnexp RCURLY'''
    pass

def p_estatutoExp(p):
    '''estatutoExp : estatuto SEMICOLON
                    | estatutoExp estatutoExp'''
    pass

def p_estatuto(p):
    '''estatuto : asignacion
                | asignacionArr
                | condicion
                | whileLoop
                | doWhile
                | forLoop
                | escritura
                | funcion
                | functionCall
                | break
                | input'''
    pass

def p_break(p): #For returns before end of func
    '''break : BREAK expresion'''
    semantics.returnExpression()
    semantics.addAssign()
    semantics.checkAssign()
    semantics.addReturnQuad()
    #Check return type
    #Assign exp to temp
    pass
                    
def p_returnexp(p): #Exclusive for end of func
    '''returnexp : RETURN expresion SEMICOLON'''
    semantics.returnExpression()
    semantics.addAssign()
    semantics.checkAssign()
    semantics.addReturnQuad()
    #Check return type
    #Assign exp to temp
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
    semantics.checkPrint()
    pass

def p_escrito(p):
    '''escrito : impr
               | impr COMA escrito'''
    pass

def p_impr(p):
    '''impr : expresion'''
    semantics.addOper("PRINT")
    pass

def p_expresion(p): 
    #a => expresion -> exp-> termino -> factor-> varcte -> ID
    #a<b => expresion -> exp expresion -> exp comparacion exp -> termimno comparacion termino -> factor comparacion factor
    #a+b => expresion -> exp expresion -> exp exp -> termino signo exp -> termino signo termino -> factor signo factor
    #a/b => expresion -> exp expresion -> exp exp -> termino termino -> factor operacion factor
    '''expresion : exp
                | condition
                | functionCall
                | arr'''
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
    '''funcion : FUNCTION funcdef LPAREN declaracion addArgs RPAREN COLON tiposreturn'''
    semantics.resetArgumentCount()
    semantics.endFunc()
    variables_control.scope_back()
    semantics.resetCounter()
    pass

def p_addArgs(p):
    '''addArgs : epsilon'''
    variables_control.addFuncInitialAddress(semantics.getCounter())
    variables_control.addArgs()
    pass

def p_funcdef(p):
    '''funcdef : ID'''
    if(not variables_control.is_in_table(p[1])):
        variables_control.add_func(p[1])
    else:
        raise ValueError(f'Function {p[1]} is declared twice.')
    pass

def p_tiposreturn(p):
    '''tiposreturn : tiposFuncion bloqueReturn
                    | VOID bloque'''
    if(p[1]):
        variables_control.add_return(p[1])
      #  variables_control.print_table()
    pass

def p_tiposFuncion(p):
    '''tiposFuncion : INT
                    | FLOAT
                    | BOOL
                    | STRING'''
    variables_control.add_return(p[1])
     #   variables_control.print_table()
    pass

def p_functionCall(p):
    '''functionCall : funCall lparen funcArgs rparen'''
    semantics.addFuncGoSub()
    semantics.checkReturnValue()
    pass

def p_funCall(p):
    '''funCall : ID'''
    if(variables_control.is_in_table(p[1]) == None):
        raise ValueError(f'Function not declared {p[1]}')
    semantics.addFuncEra(p[1])
    pass

def p_funcArgs(p):
    '''funcArgs : checkArgs
                  | funcArgs COMA funcArgs
                  | epsilon'''
    pass

def p_checkArgs(p):
    '''checkArgs : expresion'''
    semantics.addFuncArguments()
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
    '''factor : varcte
               | lparen expresion rparen
               | functionCall '''
#    print("5", "checkFact")
    semantics.checkFact()
    pass

def p_lparen(p):
    '''lparen : LPAREN'''
    semantics.addOper(p[1])
    pass

def p_rparen(p):
    '''rparen : RPAREN'''
    semantics.checkFact()
    semantics.checkTerm()
    semantics.checkCompare()
    semantics.checkParen()
    pass

def p_epsilon(p):
    '''epsilon : '''
    pass

def p_arrDef(p):
    '''arrDef : ID'''
    if(variables_control.find_var(p[1]) == None):
        declaring_variable.append(p[1])
        declaring_array.append(p[1])
    else:
        print('Variable is already declared')
    pass 

def p_declaracionArr(p):
    '''declaracionArr : arrDef LBRACKET INT RBRACKET COLON tipo'''
    if(0<len(declaring_array)):
        variables_control.declareArray(declaring_array.pop(), p[3])
    pass

def p_declaracionMatrix(p):
    '''declaracionMatrix : arrDef LBRACKET INT RBRACKET LBRACKET INT RBRACKET COLON tipo'''
    if(0<len(declaring_array)):
        variables_control.declareArray(declaring_array.pop(), p[3], p[6])
    pass
    pass

def p_asignacionArr(p):
    '''asignacionArr : arr arrayEqual expresion'''
    semantics.addAssign()
    semantics.checkAssign()
    pass

def p_arrayEqual(p):
    '''arrayEqual : EQUAL'''
    semantics.arrayAssign()
    pass

def p_arr(p):
    '''arr : callArr openBracket expresion abracket matrix
            | callArr openBracket expresion abracket epsilon'''
    # Checar espacio
    pass  

def p_callArr(p):
    '''callArr : ID'''
    if (p[1]):
        if variables_control.find_var(p[1]) == None:
            raise ValueError("Variable "+str(p[1])+" is not declared")
    declaring_array.append(p[1])
    pass  

def p_matrix(p):
    '''matrix : openBracket expresion mbracket'''
    if (p[1]):
        if variables_control.find_var(p[1]) == None:
            raise ValueError("Variable "+str(p[1])+" is not declared")
    #Checar espacio
    pass

def p_openBracket(p):
    '''openBracket : LBRACKET'''
    semantics.addOper('(')
    pass

def p_closeBracket(p):
    '''closeBracket : RBRACKET'''
#        print(")")
    semantics.checkFact()
    semantics.checkTerm()
    semantics.checkCompare()
    semantics.checkParen()
    pass

def p_abracket(p):
    '''abracket : closeBracket'''
    semantics.findArrAddress(declaring_array.pop())
    pass

def p_mbracket(p):
    '''mbracket : closeBracket'''
    semantics.findMatrixAddress()
    pass

def p_input(p):
    '''input : INPUT LPAREN ID RPAREN'''
    s = input('Pystachio > ')
    semantics.addInput(s, p[3])
    pass   

def p_varcte(p):
    '''varcte : ID 
              | int
              | float
              | bool
              | string
              | matrix
              | arr'''
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
    semantics.insertId(p[1], 'float')
    pass

def p_bool(p):
    '''bool : BOOL'''
    variables_control.addConst(p[1], 'bool')
    semantics.insertId(p[1], variables_control.find_vars_type(p[1]))
    pass

def p_string(p):
    '''string : STRING'''
    name, varType = p[1]
    variables_control.addConst(name.replace('\"',''), varType)
    semantics.insertId(name.replace('\"',''), varType)
    pass

# Error rule for syntax errors
def p_error(p):
    raise EOFError("Syntax error in input!", p)

# Build the parser
parser = yacc.yacc(debug=True)

# while True:
#     try:
#         s = input('Pystachio > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
 