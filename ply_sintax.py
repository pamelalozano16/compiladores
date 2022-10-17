 # Yacc example
import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from ply_lex import tokens
from semantic_cube import SemanticCube
from variables_control import VariableControl

semantic_cube = SemanticCube()
variables_control = VariableControl()
declaring_variable = []
declaring_types = []

def p_programa(p):
    '''programa : START LPAREN RPAREN bloque'''
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
        print("Error: Variable "+p[1]+" is not declared")
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
                | comparacion exp
                | AND exp
                | OR exp
                | exp expresion
                | arreglo '''
        #       | expresion expresion '''
    pass  

def p_comparacion(p):
    '''comparacion : LESSTHAN
                   | MORETHAN
                   | ISEQUAL
                   | NOTEQUAL'''
    pass

def p_whileLoop(p):
   '''whileLoop : WHILE LPAREN expresion RPAREN bloque'''

def p_forLoop(p):
   '''forLoop : FOR LPAREN argumentos expresion SEMICOLON expresion RPAREN bloque'''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque condicionelse'''
    pass

def p_condicionelse(p):
    '''condicionelse : ELSE bloque
                     | epsilon'''
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
    '''args : ID COLON tipo
            | args COMA args'''
    pass

def p_exp(p):
    '''exp : termino
           | termino signo'''
    pass

def p_signo(p):
    '''signo : PLUS
             | MINUS'''
    pass

def p_termino(p):
    '''termino : factor
               | factor operacion'''
    pass

def p_operacion(p):
    '''operacion : TIMES exp
                 | DIVIDE exp
                 | DIFF exp
                 | EXP exp'''
    pass

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
               | varcte
               | signo varcte'''
    pass

def p_epsilon(p):
    '''epsilon : '''
    pass

def p_varcte(p):
    '''varcte : ID 
              | CTEL
              | CTEF'''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc(debug=True)

fileName = input('Pystachio > ')
with open(fileName) as f:
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
 