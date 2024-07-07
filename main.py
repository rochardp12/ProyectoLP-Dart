import os
from datetime import datetime
import ply.yacc as yacc
from lexico import tokens

log_dir = "logs_semantico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

current_time = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"semantico-rochardp12-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

def escribir_log(mensaje):
    with open(log_filepath, 'a') as f:
        f.write(mensaje)

#Katherine Tumbaco
def p_programa(p):
    '''programa : cuerpo
                | programa cuerpo'''


def p_cuerpo(p):
    '''cuerpo : impresion
              | declaracion
              | operacion
              | comentario
              | estructuras_de_Control
            '''
    
def p_estructuras_de_Control(p):
    '''estructuras_de_Control : sentencia_If
                            | sentencia_Switch
                            | ciclo_for
                            | funcion_Anonima
                            | diccionario
                            | Conjunto
                            | funcion_flecha
                            | funcion_Void
                            | funcion
                            | funcion_Data
                            | RETURN VARIABLE
                            | estructura_List
    '''
def p_comentario(p):
    '''comentario : COMMENTLINE
                  | COMMENTBLOCK'''


def p_impresion(p):
    '''impresion : PRINT LPAREN valores RPAREN DOTCOMMA
                 | PRINT LPAREN operacion RPAREN DOTCOMMA
                 | PRINT LPAREN RPAREN DOTCOMMA
    '''

# Estructura de control - If-else - Katherine Tumbaco
def p_sentencia_If(p):
    ''' sentencia_If : IF LPAREN condicion RPAREN LBRACE programa RBRACE else
                        | IF LPAREN condicion RPAREN LBRACE programa RBRACE
    '''
def p_else(p):
    """
    else : ELSE LBRACE programa RBRACE
    """
def p_condicion(p):
    '''
    condicion : valor Comparador valor
            |   condicion conector condicion
    ''' 

def p_conector(p):
    '''conector : AND
                | OR
    '''
    

# Estructura de datos - Arreglos - List - Katherine Tumbaco
def p_estructura_List(p):
    'estructura_List : LIST LANGLE tipo RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA'

# Tipo de funcion - Función sin retorno - Katherine Tumbaco
def p_funcion_Void(p):
    'funcion_Void : VOID VARIABLE LPAREN valores RPAREN LBRACE programa RBRACE DOTCOMMA'

def p_Comparador(p):
    '''Comparador : EQUALS EQUALS
                    | LANGLE
                    | RANGLE
                    | LANGLE EQUALS
                    | RANGLE EQUALS
                    | NEQ'''

def p_tupla(p):
    'tupla : LPAREN valores RPAREN'

def p_valores(p):
    '''valores : valor
               | valor COMMA valores'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_Bool(p):
    '''Bool : TRUE
        | FALSE '''


def p_valor(p):
    '''
    valor   : VARIABLE
            | NUMBER
            | FLOAT
            | CHAINCHAR
            | Bool
            | operacion
            | tupla
    '''
    p[0] = p[1]

def p_tipo(p):
    '''tipo : MAP
            | DOUBLE
            | STRING
            | INT
            | SET
            | LIST
            | BOOLEAN
            | FINAL
            | CONST
            | DYNAMIC
    '''
    p[0] = p[1]

#Richard

def p_declaracion(p):
    """
    declaracion : tipo VARIABLE EQUALS valor DOTCOMMA
                | VAR VARIABLE EQUALS valor DOTCOMMA
    """
    
def p_operacion(p):
  'operacion : valor operador expresion'

def p_expresion(p):
    '''expresion : LPAREN valor operador expresion RPAREN
                    | valor '''
    
def p_funcion(p):
    'funcion : VARIABLE LPAREN valores RPAREN'

def p_funcion_Data(p):
    'funcion_Data : VARIABLE DOT VARIABLE LPAREN valores RPAREN DOTCOMMA'

#-----------------SWITCH-----------------------------------
def p_sentencia_Switch(p):
    'sentencia_Switch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACE'

def p_caso(p):
    '''caso : CASE valor TWODOTS programa BREAK DOTCOMMA caso 
            | CASE valor TWODOTS programa BREAK DOTCOMMA '''
#----------------------------------------------------------


#----------------FUNCION FLECHA-----------------------------
def p_funcion_flecha_param(p):
    'funcion_flecha : tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMA'
    for valor in p[4]:
        if not isinstance(valor,str) or not valor.isidentifier():
            mensaje = f'Error semantico: Parametro "{valor}" incorrecto. Los parametros de la funcion flecha deben ser nombres de variables\n'
            print(mensaje)
            escribir_log(mensaje)

def p_funcion_flecha_no_param(p):
    'funcion_flecha : tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMA'
#----------------------------------------------------------


#----------------CONJUNTOS---------------------------------
def p_Conjunto(p):
    '''Conjunto : SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA
                    | SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMA'''

def p_cuerpo_conjunto(p):
    '''cuerpo_conjunto : LBRACE valores RBRACE
                | LBRACE RBRACE '''
#----------------------------------------------------------

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE '''
    
#Roberto Encalada

#-----------------------FOR-----------------------------------
def p_ciclo_for(p):
    """
    ciclo_for : FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa  RBRACE
    """


def p_contador(p):
    '''contador : VARIABLE PLUS PLUS
                | VARIABLE PLUS EQUALS valor
                | VARIABLE MINUS MINUS
                | VARIABLE MINUS EQUALS valor'''

#----------------------------------------------------------
#-----------------------Función anónima-----------------------------------
def p_funcion_Anonima(p):
    """
    funcion_Anonima : VAR VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA
                    | tupla LBRACE programa RBRACE DOTCOMMA
    """
#----------------------------------------------------------
#-----------------------Diccionario-----------------------------------
def p_diccionario(p):
    'diccionario : MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA'

def p_cuerpo_Diccionario(p):
    """
    cuerpo_Diccionario : LBRACE duplas RBRACE
                    | LBRACE RBRACE
    """
def p_duplas(p):
    '''duplas : dupla
              | dupla COMMA duplas
    '''

def p_dupla(p):
    '''dupla : valor TWODOTS valor
    '''
#----------------------------------------------------------
# Crear el directorio de logs si no existe
'''
log_dir = "logs_semantico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    
# Obtener la hora actual para los nombres de archivo de log
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")

UsuariosGit = "rochardp12"
# Nombre del archivo de log
log_filename = f"semantico-{UsuariosGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

# Archivo de log para escribir
log_file = open(log_filepath, 'w')'''
  
# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Error sintactico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos}")
        #log_file.write(f"Syntax error at '{p.value}'\n")
    else:
        print("Error sintactico en el final del token")
        #log_file.write("Syntax error at EOF\n")

# Build the parser
parser = yacc.yacc()

def parse_input(input_string):
    result = parser.parse(input_string)
    #log_file.write(f"Input: {input_string}\nResult: {result}\n\n")
    return result

while True:
  try:
      s = input('lp > ')
  except EOFError:
      break
  if not s: continue
  result = parse_input(s)
  print(result)

log_file.close()