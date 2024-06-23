import ply.yacc as yacc
from lexico import tokens

import os
from datetime import datetime

def p_cuerpo(p):
    '''cuerpo : switch
            | flecha
            | crearConjunto
            | NUMBER '''


#-----------------SWITCH-----------------------------------
def p_sentenciaSwitch(p):
    'switch : SWITCH LPAREN valoresTotales RPAREN LBRACE caso RBRACE'

def p_casos(p):
    '''caso : CASE valoresTotales TWODOTS cuerpo BREAK caso 
            | CASE valoresTotales TWODOTS cuerpo BREAK'''
#----------------------------------------------------------

#----------------FUNCION FLECHA-----------------------------
def p_funcionflecha(p):
    'flecha : tipoDato valorVariable LPAREN parametros RPAREN ARROWFUNCTION cuerpo'
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
    
def p_valorVariable(p):
    'valorVariable : VARIABLE'

def p_valorBooleano(p):
    '''valorBooleano : TRUE
                    | FALSE '''

def p_valoresTotales(p):
    '''valoresTotales : valorBooleano
                    | valorNumerico
                    | valorVariable '''

def p_tipoDato(p):
   '''tipoDato : MAP
                | DOUBLE
                | STRING
                | INT
                | SET
                | LIST
                | BOOLEAN
                | NEWDATATYPE '''

def p_parametros(p):
    '''parametros : valoresTotales
                | valoresTotales COMMA parametros'''
    
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