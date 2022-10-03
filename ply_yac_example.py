 # Yacc example
import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from ply_lex_example import tokens

def p_programa(p):
    '''programa : PROGRAM ID SEMICOLON vars bloque'''
    pass

def p_vars(p):
    '''vars : VAR var
            | vars vars
            | epsilon'''
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
            | FLOAT'''
    pass

def p_bloque(p):
    '''bloque : LCURLY estatuto RCURLY '''
    pass

def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion
                | escritura
                | epsilon'''
    pass

def p_asignacion(p):
    '''asignacion : ID EQUAL expresion SEMICOLON'''
    pass

def p_escritura(p):
    '''escritura : PRINT LPAREN escrito RPAREN SEMICOLON'''
    pass

def p_escrito(p):
    '''escrito : impr
               | impr COMA impr'''
    pass

def p_impr(p):
    '''impr : CTESTRING
            | expresion'''
    pass

def p_expresion(p): 
    #a => expresion -> exp-> termmino -> factor-> varcte -> ID
    #a<b => expresion -> exp expresion -> exp comparacion exp -> termimno comparacion termino -> factor comparacion factor
    #a+b => expresion -> exp expresion -> exp exp -> termino signo exp -> termino signo termino -> factor signo factor
    #a/b => expresion -> exp expresion -> exp exp -> termino termino -> factor operacion factor
    '''expresion : exp
                | comparacion exp
                | exp expresion'''
    pass  

def p_comparacion(p):
    '''comparacion : LESSTHAN
                   | MORETHAN
                   | NOTEQUAL'''
    pass

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque condicion
                | ELSE bloque condicion
                | SEMICOLON
                | epsilon'''
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
                 | DIVIDE exp'''
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
        s = input('littleDuck > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
 