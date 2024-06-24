import os
from datetime import datetime
import ply.yacc as yacc
from lexico import tokens

#Katherine Tumbaco

def p_cuerpo(p):
    '''cuerpo : impresion
              | tupla
              | declaracion
              | sentenciaIf
              | estructuraList
              | funcionVoid
              | switch
              | operacion
              | flecha
              | RETURN VARIABLE 
              | funcion
              | funcionData 
              | crearConjunto
            '''

def p_impresion(p):
    '''impresion : PRINT LPAREN valores RPAREN DOTCOMMA
                 | PRINT LPAREN operacion RPAREN DOTCOMMA
    '''

# Estructura de control - If-else - Katherine Tumbaco
def p_sentenciaIf(p):
    ''' sentenciaIf : IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE else
                        | IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE DOTCOMMA
    '''
def p_condicion(p):
    'condicion : valor operadorComp valor' 
    
def p_else(p):
    """
    else : ELSE LBRACE cuerpo RBRACE DOTCOMMA
    """
# Estructura de datos - Arreglos - List - Katherine Tumbaco
def p_estructuraList(p):
    'estructuraList : LIST LANGLE type RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA'

# Tipo de funcion - Función sin retorno - Katherine Tumbaco
def p_funcionVoid(p):
    'funcionVoid : VOID VARIABLE LPAREN valores RPAREN LBRACE cuerpo RBRACE DOTCOMMA'

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

def p_Bool(p):
    '''Bool : TRUE
        | FALSE '''

def p_valor(p):
    '''valor : VARIABLE
             | FLOAT
             | Bool
             | operacion
             | NUMBER
             | CHAINCHAR
    '''
def p_type(p):
    '''type : MAP
            | DOUBLE
            | STRING
            | INT
            | SET
            | LIST
            | BOOLEAN
    '''

#Richard

def p_tipoVariable(p):
    '''tipoVariable : type  
                    | FINAL
                    | CONST
                    | VAR
                    | DYNAMIC '''


def p_declaracion(p):
    'declaracion : tipoVariable VARIABLE EQUALS valor'
    
def p_operacion(p):
  'operacion : valor operador numeroSiguiente'

def p_numeroSiguiente(p):
    '''numeroSiguiente : LPAREN valor operador numeroSiguiente RPAREN
                    | valor '''
    
def p_funcion(p):
    'funcion : VARIABLE LPAREN valores RPAREN'

def p_funcionData(p):
    'funcionData : VARIABLE DOT VARIABLE LPAREN valores RPAREN'

#-----------------SWITCH-----------------------------------
def p_sentenciaSwitch(p):
    'switch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACE'

def p_casos(p):
    '''caso : CASE valor TWODOTS cuerpo BREAK caso 
            | CASE valor TWODOTS cuerpo BREAK'''
#----------------------------------------------------------


#----------------FUNCION FLECHA-----------------------------
def p_funcionflecha(p):
    'flecha : type VARIABLE LPAREN valores RPAREN ARROWFUNCTION cuerpo'
#----------------------------------------------------------


#----------------CONJUNTOS---------------------------------
def p_crearConjunto(p):
    '''crearConjunto : SET VARIABLE EQUALS conjunto
                    | SET LANGLE type RANGLE VARIABLE EQUALS conjunto'''

def p_conjunto(p):
    '''conjunto : LBRACE valores RBRACE
                | LBRACE RBRACE '''
#----------------------------------------------------------

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE '''

#Roberto Encalada


# Crear el directorio de logs si no existe
log_dir = "logs_sintactico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    
# Obtener la hora actual para los nombres de archivo de log
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")

UsuariosGit = "rocaenca"
# Nombre del archivo de log
log_filename = f"sintactico-{UsuariosGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

# Archivo de log para escribir
log_file = open(log_filepath, 'w')
  
# Error rule for syntax errors
def p_error(p):
    print(f"Error sintactico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos}")
    log_file.write(f"Syntax error at '{p.value}'\n")

# Build the parser
parser = yacc.yacc()

def parse_input(input_string):
    result = parser.parse(input_string)
    log_file.write(f"Input: {input_string}\nResult: {result}\n\n")
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