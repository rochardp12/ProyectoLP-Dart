import os
from datetime import datetime
import ply.yacc as yacc
from lexico import tokens


type_map = {
    'String': str,
    'int': int,
    'double': float,
    'boolean': bool,
    'List': list,
    'map': dict,
    'Set': set,
    'tuple': tuple,
}

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
        p[0] = [p[1]] + p[2]

def p_cuerpo(p):
    '''cuerpo : impresion
              | declaracion
              | operacion
              | comentario
              | estructuras_de_Control
              | return'''
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
                 | PRINT LPAREN CHAINCHAR RPAREN DOTCOMMA
                 | PRINT LPAREN operacion RPAREN DOTCOMMA
                 | PRINT LPAREN condiciones RPAREN DOTCOMMA
                 | PRINT LPAREN RPAREN DOTCOMMA
    '''
    if len(p) == 5:
        pass
    else:
        contenido = p[3]
        if isinstance(contenido, list): 
            for var in contenido:
                if not existe_variable(var):
                    error_declaracion(var)

    
    
# Estructura de control - If-else - Katherine Tumbaco
def p_sentencia_If(p):
    ''' sentencia_If : IF LPAREN condiciones RPAREN LBRACE programa RBRACE else
                        | IF LPAREN condiciones RPAREN LBRACE programa RBRACE '''

  
def p_else(p):
    """
    else : ELSE LBRACE programa RBRACE
    """
    
def p_condicion(p):
    'condicion : valor Comparador valor'
    if type(p[1][0]) == type(p[3]):
        pass
    else:
        error_tipo(p[1], p[3])

    p[0] = [p[1], p[2], p[3]]

def p_condiciones(p):
    '''condiciones : condicion
                    | condicion conector condiciones
                    | Bool
    '''               
    
    #Semantica - If tener una condición que evalúe a un valor booleano. Katherine Tumbaco 

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_conector(p):
    '''conector : AND
                | OR
    '''
    p[0] = p[1]
    

# Estructura de datos - Arreglos - List - Katherine Tumbaco
def p_estructura_List(p):
    'estructura_List : LIST LANGLE tipo RANGLE VARIABLE EQUALS lista DOTCOMMA'
    tipo_elemento = type_map[p[3]]
    lista_valores = []
    for element in p[7]:
        if isinstance(element, tipo_elemento):
            lista_valores.append(element)
        else:
            error_tipo(tipo_elemento.__name__, element)
            return
    
    variables[p[5]] = [lista_valores, f"LIST<{p[3]}>"]


def p_lista(p):
    'lista : LBRACKET valores RBRACKET'
    p[0] = list(p[2])


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

def p_return(p):
    'return : RETURN valor DOTCOMMA'
    p[0] = [p[1], p[2]]
            

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
    p[0] = tuple(p[2])

def p_valores(p):
    '''valores : valor
               | valor COMMA valores'''
               
    #Semantico - Katherine Tumbaco           
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

        
def p_Bool(p):
    '''Bool : TRUE
        | FALSE '''
    p[0] = bool(p[1])


def p_valor(p):
    '''
    valor   : VARIABLE
            | NUMBER
            | FLOAT
            | CHAINCHAR
            | Bool
            | tupla
            | lista
            | cuerpo_conjunto
            | cuerpo_Diccionario
    '''

    if existe_variable(p[1]):
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]


def p_tipo(p):
    '''tipo : MAP
            | DOUBLE
            | STRING
            | INT
            | SET
            | LIST
            | BOOLEAN
            | TUPLE
    '''
    p[0] = p[1]

#Richard

def p_declaracion(p):
    """
    declaracion : tipo VARIABLE EQUALS valor DOTCOMMA
                | VAR VARIABLE EQUALS valor DOTCOMMA
    """
    if p[1] == "var":
        variables[p[2]] = [p[4], "VAR"]
    else:
        tipo_variable = type_map[p[1]]
        valor = p[4]

        if isinstance(valor, tipo_variable):
            variables[p[2]] = [valor, p[1]]
        else:
            error_tipo(tipo_variable.__name__, valor)
            return
    p[0] = p[2]

def p_operacion(p):
    'operacion : valor operador expresion'

    if not isinstance(p[1],int) and not isinstance(p[1],float):
        mensaje = 'Error semantico: El valor en la operacion debe ser numerico\n'
        print(mensaje)
        

def p_expresion(p):
    '''expresion : LPAREN valor operador expresion RPAREN
                    | valor '''
    if len(p) == 2:
        p[0] = p[1]    
    else:
        if not isinstance(p[2], (int, float)):
            mensaje = "Error semantico: Los valores en la expresion deben ser numericos"
            print(mensaje)
        elif not isinstance(p[4], (int, float)):
            mensaje = "Error semantico: Los valores en la expresion deben ser numericos"
            print(mensaje)
        elif p[3] == '+' and isinstance(p[2], type(p[4])):
            p[0] = p[2] + p[4]
        elif p[3] == '-' and isinstance(p[2], type(p[4])):
            p[0] = p[2] - p[4]
        elif p[3] == '*' and isinstance(p[2], type(p[4])):
            p[0] = p[2] * p[4]
        elif p[3] == '/' and isinstance(p[2], type(p[4])):
            p[0] = p[2] / p[4]
        else:
            mensaje = "Error semantico: Los valores en la expresion deben ser numericos"
            print(mensaje)

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

def p_funcion_flecha_no_param(p):
    'funcion_flecha : tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMA'
#----------------------------------------------------------


#----------------CONJUNTOS---------------------------------
def p_Conjunto(p):
    '''Conjunto : SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA
                    | SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMA'''
    if len(p) == 6:
        conjunto = p[4]
        variables[p[2]] = [conjunto, "SET"]
    else:
        tipo_elemento = type_map[p[3]]
        cuerpo_conjunto = p[7]
        
        conjunto = set()
        for elemento in cuerpo_conjunto:
            if isinstance(elemento, tipo_elemento):
                conjunto.add(elemento)
            else:
                error_tipo(tipo_elemento.__name__, elemento )
                return
        
        variables[p[5]] = [conjunto, f"SET<{p[3]}>"]

def p_cuerpo_conjunto(p):
    '''cuerpo_conjunto : LBRACE valores RBRACE
                | LBRACE RBRACE '''
    if len(p) == 4:
        p[0] = set(p[2])
    else:
        p[0] = set()
#----------------------------------------------------------

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE '''
    p[0] = p[1]
#Roberto Encalada

#-----------------------FOR-----------------------------------
def p_ciclo_for(p):
    """
    ciclo_for : FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa RBRACE
    """
    # Obtenemos la variable de control
    variable_control = p[3]
    # Obtenemos la condición de terminación
    condicion_terminacion = p[4]
    # Obtenemos el contador
    contador = p[6]
    # Verificamos que la variable de control exista
    if existe_variable(variable_control):
        valor_actual = variables[variable_control][0]
        
        # Determinamos el valor de terminación de la condición
        if condicion_terminacion[1] == "<":
            valor_terminacion = condicion_terminacion[2]
            if valor_actual >= valor_terminacion:
                error_ciclo(variable_control)
                return
            else:
                if contador[1] == "-" and contador[2] == "-":
                    error_ciclo(variable_control)
                    return
        elif condicion_terminacion[1] == ">":
            valor_terminacion = condicion_terminacion[2]
            if valor_actual <= valor_terminacion:
                error_ciclo(variable_control)
                return
            else:
                if contador[1] == "+" and contador[2] == "+":
                    error_ciclo(variable_control)
                    return

    else:
        error_declaracion(variable_control)


def error_ciclo(variable):
    print(f"Error semántico: El ciclo for con la variable de control '{variable}' jamás se ejecuta o se ejecuta infinitas veces.")
    

def p_contador(p):
    '''contador : VARIABLE PLUS PLUS
                | VARIABLE PLUS EQUALS valor
                | VARIABLE MINUS MINUS
                | VARIABLE MINUS EQUALS valor'''
    if existe_variable(p[1]):
        if len(p) == 4:
            if p[2] == "+" and p[3] == "+":
                variables[p[1]][0] += 1
            else:
                variables[p[1]][0] -= 1
        else:
            variables[p[1]][0] += int(p[4])
    else:
        error_declaracion(p[1])
    p[0] = [p[1]] + [p[2], p[3]]
#----------------------------------------------------------
#-----------------------Función anónima-----------------------------------
def p_funcion_Anonima(p):
    """
    funcion_Anonima : tipo VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA
                    | tupla LBRACE programa RBRACE DOTCOMMA
    """
   

#----------------------------------------------------------
#-----------------------Diccionario-----------------------------------
def p_diccionario(p):
    'diccionario : MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA'
     # Obtenemos el cuerpo del diccionario
    cuerpo_dic = p[9]
    tipo_clave = type_map[p[3]]
    tipo_valor = type_map[p[5]]
    # Validamos las duplas
    for clave, valor in cuerpo_dic.items():
        if not isinstance(clave, tipo_clave):
            error_tipo(tipo_clave.__name__, clave)
            return
        if not isinstance(valor, tipo_valor):
            error_tipo(tipo_valor.__name__, valor)
            return
        # Si todo es correcto, almacenamos el diccionario
    variables[p[7]] = [cuerpo_dic, f"MAP<{p[3]}, {p[5]}>"]

def p_cuerpo_Diccionario(p):
    """
    cuerpo_Diccionario : LBRACE duplas RBRACE
                    | LBRACE RBRACE
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = {}

    
def p_duplas(p):
    '''duplas : dupla
              | dupla COMMA duplas
    '''
    if len(p) == 2:
        p[0] = {}
        p[0][p[1][0]] = p[1][1]
    else:
        p[0] = {}
        p[0][p[1][0]] = p[1][1]
        p[0].update(p[3])

def p_dupla(p):
    '''dupla : valor TWODOTS valor
    '''
    p[0] = [p[1],p[3]]

def error_declaracion(p):
    print(f"Error semántico: La variable '{p}' no ha sido declarada.")

def existe_variable(p):
    return isinstance(p, str) and p in variables

def error_tipo(p1, p2):
    print(f"Error semántico: Tipos incompatibles '{p1}' y '{type(p2).__name__}'.")
#----------------------------------------------------------

# Crear el directorio de logs si no existe

log_dir = "logs_semantico"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    
# Obtener la hora actual para los nombres de archivo de log
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")


UsuariosGit = "rocaenca"

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

