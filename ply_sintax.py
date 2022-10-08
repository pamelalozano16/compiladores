 # Yacc example
import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from ply_lex_example import tokens

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
    '''vardef : ID
              | vardef COMA vardef'''
    pass

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | BOOL
            | STRING'''
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
   '''forLoop : FOR LPAREN vars expresion SEMICOLON expresion RPAREN bloque'''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque condicionelse'''
    pass

def p_condicionelse(p):
    '''condicionelse : ELSE bloque
                     | epsilon'''
    pass

def p_tiposreturn(p):
    '''tiposreturn : tipo
                    | VOID'''
    pass

def p_funcion(p):
    '''funcion : FUNCTION ID LPAREN argumentos RPAREN COLON tiposreturn bloque'''
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

while True:
    try:
        s = input('Pystachio > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
 