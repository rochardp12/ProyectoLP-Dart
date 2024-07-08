import os
from datetime import datetime
import ply.yacc as yacc
from lexico import tokens


#Katherine Tumbaco
sin_retorno= {}
funciones = {}
variables = {}

def p_programa(p):
    '''programa : cuerpo
                | programa cuerpo'''
    
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_cuerpo(p):
    '''cuerpo : impresion
              | declaracion
              | operacion
              | comentario
              | estructuras_de_Control
              | RETURN 
              | RETURN valores'''
    p[0] = p[1]
       
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
                            | estructura_List'''
                            
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
    ''' sentencia_If : IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE 
                        | IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE else
    '''
  
            
def p_else(p):
    """
    else : ELSE LBRACE programa RBRACE
    """
def obtener_tipo(valor):
    if isinstance(valor, int):
        return 'int'
    elif isinstance(valor, float):
        return 'float'
    elif isinstance(valor, str):
        return 'string'
    elif isinstance(valor, bool):
        return 'bool'
    else:
        return 'unknown'
    
def p_condicion(p):
    '''
    condicion : valor Comparador valor
            |   condicion conector condicion
            |   Bool
    ''' 
    #Semantica - If tener una condición que evalúe a un valor booleano. Katherine Tumbaco 
    if len(p) == 4:
        tipo1 = obtener_tipo(p[1])
        tipo2 = obtener_tipo(p[3])
        if tipo1 != tipo2:
            print(f"Error semántico: Tipos incompatibles en la comparación: {tipo1} y {tipo2}")
        else:
            p[0] = True 
    elif len(p) == 3:
        p[0] = p[1] and p[3] if p[2] == 'AND' else p[1] or p[3]
    else:
        p[0] = p[1]
    
def p_conector(p):
    '''conector : AND
                | OR
    '''
    

# Estructura de datos - Arreglos - List - Katherine Tumbaco
def p_estructura_List(p):
    'estructura_List : LIST LANGLE tipo RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA'

# Tipo de funcion - Función sin retorno - Katherine Tumbaco
def p_funcion_Void(p):
    '''funcion_Void : VOID VARIABLE LPAREN valores RPAREN LBRACE programa RBRACE
                    | VOID VARIABLE LPAREN RPAREN LBRACE programa RBRACE
                    | VOID MAIN LPAREN RPAREN LBRACE programa RBRACE'''
    #Semantico- no retorna un valor deben ser declaradas con el tipo void - Katherine Tumbaco
    func_name = p[2]
    sin_retorno[func_name] = 'void'

    if any('return' in item for item in p[7]):
        print(f"Error semántico: La función '{func_name}' declarada como 'void' no debe contener un retorno 'return'.")
    elif any('return' in item for item in p[6]):
        print(f"Error semántico: La función '{func_name}' declarada como 'void' no debe contener un retorno 'return'.")
    else:
        print(f"Función sin retorno '{func_name}' declarada correctamente.")

def p_Comparador(p):
    '''Comparador : EQUALS EQUALS
                    | LANGLE
                    | RANGLE
                    | LANGLE EQUALS
                    | RANGLE EQUALS
                    | NEQ'''
    #Semantico - Katherine Tumbaco 
    p[0] = p[1] if len(p) == 2 else (p[1], p[2])

def p_tupla(p):
    'tupla : LPAREN valores RPAREN'

def p_valores(p):
    '''valores : valor
               | valor COMMA valores
               | tipo VARIABLE
               | tipo VARIABLE COMMA valores'''
               
    #Semantico - Katherine Tumbaco           
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = [p[1]] + p[3]
    elif len(p) == 4:
        p[0] = [p[1], p[3]]
    elif len(p) == 5:
        p[0] = [p[1], p[3]] + p[4]

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
    #Semantico - Katherine Tumbaco 
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
def p_funcion_flecha(p):
    'funcion_flecha : tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMA'
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
log_dir = "logs_semantico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    
# Obtener la hora actual para los nombres de archivo de log
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")

UsuariosGit = "katumbac"
# Nombre del archivo de log
log_filename = f"semantico-{UsuariosGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

# Archivo de log para escribir
log_file = open(log_filepath, 'w')
  
# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Error sintactico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos}")
        log_file.write(f"Syntax error at '{p.value}'\n")
    else:
        print("Error sintactico en el final del token")
        log_file.write("Syntax error at EOF\n")

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