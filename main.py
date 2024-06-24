import os
from datetime import datetime
import ply.yacc as yacc
from lexico import tokens

# Crear el directorio de logs si no existe
log_dir = "logs_sintactico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    
# Obtener la hora actual para los nombres de archivo de log
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")

UsuariosGit = "katumbac"
# Nombre del archivo de log
log_filename = f"sintactico-{UsuariosGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

# Archivo de log para escribir
log_file = open(log_filepath, 'w')
  
#Katherine Tumbaco

def p_cuerpo(p):
    '''cuerpo : expresion
              | impresion 
              | tupla
              | declaracion
              | sentenciaIfElse
              | estructuraList
              | funcionVoid'''

def p_expresion(p):
    'expresion : valor operador valor'

def p_declaracion(p):
    '''declaracion : VARIABLE EQUALS valor
                   | VARIABLE EQUALS tupla'''

def p_impresion(p):
    '''impresion : PRINT LPAREN valores RPAREN DOTCOMMA
                 | PRINT LPAREN expresion RPAREN DOTCOMMA
    '''

# Estructura de control - If-else - Katherine Tumbaco
def p_sentenciaIfElse(p):
    ''' sentenciaIfElse : IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE ELSE LBRACE cuerpo RBRACE DOTCOMMA
                        | IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE DOTCOMMA
    '''
# Estructura de datos - Arreglos - List - Katherine Tumbaco
def p_estructuraList(p):
    'estructuraList : LIST LANGLE type RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA'

# Tipo de funcion - Función sin retorno - Katherine Tumbaco
def p_funcionVoid(p):
    'funcionVoid : VOID VARIABLE LPAREN valores RPAREN LBRACE cuerpo RBRACE DOTCOMMA'

def p_condicion(p):
    'condicion : valor operadorComp valor'

def p_operadorComp(p):
    '''operadorComp : EQUALS 
                    | LANGLE
                    | RANGLE
                    | NEQ'''

def p_tupla(p):
    'tupla : LPAREN valores RPAREN'

def p_impresion_vacia(p):
    '''impresion : PRINT LPAREN RPAREN DOTCOMMA
    '''
def p_impresion_varias(p):
    'impresion : '

def p_valores(p):
    '''valores : valor
               | valor COMMA valores'''
               
def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
    '''

def p_valor(p):
    '''valor : VARIABLE
             | INT
             | FLOAT
             | BOOL
             | expresion
             | NUMBER
    '''
def p_type(p):
    '''type : INT
             | STRING
             | BOOL
    '''
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    log_file.write(f"Syntax error at '{p.value}'\n")

# Build the parser
parser = yacc.yacc()

def parse_input(input_string):
    result = parser.parse(input_string)
    log_file.write(f"Input: {input_string}\nResult: {result}\n\n")
    return result

#while True:
#   try:
#       s = input('lp > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)

if __name__ == '__main__':
    while True:
        try:
            s = input('lp > ')
        except EOFError:
            break
        if not s:
            continue
        result = parse_input(s)
        print(result)

log_file.close()