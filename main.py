import ply.yacc as yacc
from lexico import tokens

import os
from datetime import datetime

def p_cuerpo(p):
    '''cuerpo : switch
            | declaracion
            | flecha
            | NUMBER '''
    

def p_declaracion(p):
    'declaracion : tipoDato VARIABLE EQUALS valoresDatos'
    
def p_operacion(p):
  'operacion : valorNumerico operador valorNumerico'

def p_sentencia(p):
    '''sentencia : declaracion
                | operacion
                | RETURN VARIABLE 
                | funcion
                | funcionData '''
    
def p_funcion(p):
    'funcion : VARIABLE LPAREN parametros RPAREN'

def p_funcionData(p):
    'funcionData : VARIABLE DOT VARIABLE LPAREN parametros RPAREN'

#-----------------SWITCH-----------------------------------
def p_sentenciaSwitch(p):
    'switch : SWITCH LPAREN valoresDatos RPAREN LBRACE caso RBRACE'

def p_casos(p):
    '''caso : CASE valoresDatos TWODOTS sentencia BREAK caso 
            | CASE valoresDatos TWODOTS sentencia BREAK'''
#----------------------------------------------------------


#----------------FUNCION FLECHA-----------------------------
def p_funcionflecha(p):
    'flecha : tipoDato VARIABLE LPAREN parametros RPAREN ARROWFUNCTION sentencia'
#----------------------------------------------------------


#----------------CONJUNTOS---------------------------------
def p_crearConjunto(p):
    '''crearConjunto : SET VARIABLE EQUALS conjunto
                    | SET LANGLE tipoDato RANGLE VARIABLE EQUALS conjunto'''

def p_conjunto(p):
    '''conjunto : LBRACE parametros RBRACE
                | LBRACE RBRACE '''
#----------------------------------------------------------
    
def p_valorNumerico(p):
    '''valorNumerico : NUMBER
                    | FLOAT '''
    
def p_valorBooleano(p):
    '''valorBooleano : TRUE
                    | FALSE '''

def p_valoresDatos(p):
    '''valoresDatos : valorBooleano
                    | valorNumerico
                    | VARIABLE '''

def p_tipoDato(p):
   '''tipoDato : MAP
                | DOUBLE
                | STRING
                | INT
                | SET
                | LIST
                | BOOLEAN
                | VAR '''

def p_parametros(p):
    '''parametros : valoresDatos
                | valoresDatos COMMA parametros'''

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE '''



# Error rule for syntax errors
#def p_error(p):
   # print("Syntax error in input!")
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

current_time = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"sintactico-rochardp12-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

def p_error(p):
    print(f"Error sintactico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos}")
    with open(log_filepath, 'a') as f:
        f.write(f"Error sintactico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos}\n")


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