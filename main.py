import ply.yacc as yacc
from lexico import tokens

def p_cuerpo(p):
    '''cuerpo : expresion
             | impresion 
             | tupla
             | declaracion
             | sentencia'''

def p_expresion(p):
  'expresion : valor operador valor'

def p_sentenciaIfElse(p):
    'sentencia : IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE ELSE LBRACE cuerpo RBRACE'

def p_condicion(p):
    'condicion : valor operadorComp valor'

def p_operadorComp(p):
    '''operadorComp : LESSTHAN
                | MORETHAN'''

def p_declaracion(p):
    '''declaracion : VARIABLE ASSIGN valor
                   | VARIABLE ASSIGN tupla'''

def p_operador(p):
    '''operador : PLUS
                | MINUS
            | TIMES
            | DIVIDE
    '''

def p_impresion(p):
    'impresion : PRINT LPAREN valores RPAREN'

def p_impresion_vacia(p):
    'impresion : PRINT LPAREN RPAREN'

def p_tupla(p):
    'tupla : LPAREN valores RPAREN'

def p_valores(p):
    '''valores : valor
            | valor COMMA valores'''

def p_valor(p):
    '''valor : VARIABLE
            | INT
            | FLOAT
            | expresion
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)