#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip3 install ply


# In[2]:


import ply.lex as lex
import re


# In[3]:


reserved_keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT',
    'ctestring': 'CTESTRING',
    'if': 'IF',
    'else': 'ELSE',
    'ctel': 'CTEL',
    'ctef': 'CTEF',
}


# In[4]:


tokens = [
    'ID',
    'NUMBER',
    'LCURLY',
    'RCURLY',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COLON',
    'COMA',
    'EQUAL',
    'MORETHAN',
    'LESSTHAN',
    'NOTEQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
] + list(reserved_keywords.values())


# In[5]:


t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMA = r'\,'
t_EQUAL = r'\='
t_MORETHAN = r'>'
t_LESSTHAN = r'<'
t_NOTEQUAL = r'<>'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'


# In[6]:


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved_keywords.get(t.value, 'ID')
    return t

def t_NUMBER(t):
     r'\d+ (\. \d+)? (E [+-]? \d+)?'
     t.value = float(t.value)    
     return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()

# Test it out
# data = '''
#  (3 + 4) > 10
#   { + <> 2.3E-5 * 2.33 }
#    ABC_123 
#  '''
 
#  # Give the lexer some input
# lexer.input(data)
 
#  # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok.type, tok.value)


# In[ ]:




