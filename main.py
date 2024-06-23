import ply.yacc as yacc
from lexico import tokens

import os
from datetime import datetime

def p_cuerpo(p):
    '''cuerpo : switch
            | NUMBER '''


#-----------------SWITCH-----------------------------------
def p_sentenciaSwitch(p):
    '''switch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACE'''


def p_casos(p):
    '''caso : CASE valor TWODOTS cuerpo BREAK caso 
            | CASE valor TWODOTS cuerpo BREAK'''


def p_valor(p):
    '''valor : VARIABLE
            | NUMBER
            | FLOAT
            | TRUE
            | FALSE
    '''

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