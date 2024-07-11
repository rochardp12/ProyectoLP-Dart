import ply.yacc as yacc
from lexico import tokens

#interfaz

import tkinter as tk

#---------------------------------------------- abrir archivo dart o txt --------------------------------------------------
def procesar_archivo():
    nombrecodigo = cajafiles.get("1.0",'end-1c')
    if nombrecodigo.endswith('.dart'):
        try:
            with open(nombrecodigo, 'r') as archivo:
                cajacodigo.delete("1.0", tk.END)  # Limpiar contenido anterior si es necesario
                for linea in archivo:
                    cajacodigo.insert(tk.END, linea)  # Insertar cada línea en la caja de texto
        except FileNotFoundError:
                cajacodigo.delete("1.0", tk.END)
                cajaconsole.insert(tk.END, f"No se encontró el archivo '{nombrecodigo}'")
    elif nombrecodigo.endswith('.txt'):
        try:
            with open(nombrecodigo, 'r') as archivo:
                cajacodigo.delete("1.0", tk.END)  # Limpiar contenido anterior si es necesario
                for linea in archivo:
                    cajacodigo.insert(tk.END, linea)  # Insertar cada línea en la caja de texto
        except FileNotFoundError:
                cajacodigo.delete("1.0", tk.END)
                cajaconsole.insert(tk.END, f"No se encontró el archivo '{nombrecodigo}'")
    else:
        cajaconsole.delete("1.0", tk.END)
        cajaconsole.insert(tk.END, "Error: El archivo debe tener extensión '.txt' o '.dart'")
def textoconsole():
    
    codigo = cajacodigo.get("1.0",'end-1c')
    with open("codigo.txt", "w") as archivo:
        archivo.write(codigo) 
        
    type_map = {
        'String': str,
        'int': int,
        'double': float,
        'boolean': bool,
        'List': list,
        'map': dict,
        'Set': set,
        'tuple': tuple,
        'var': type(None)
    }

    #Katherine Tumbaco
    sin_retorno= {}
    variables = {}

    def p_programa(p):
        '''programa : cuerpo
                    | programa cuerpo'''
        
        if len(p) == 2:
            p[0] = [p[1]] + [None]
        else:
            p[0] = p[1] + [p[2]]

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
                                | estructura_List
                                | estructura_tupla'''
        
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
        contenido = p[3]
        if contenido != None:
            for variable in contenido:
                if isinstance(variable, list) and variable[0] == '$':
                    var = variable[1]
                    if not existe_variable(var):
                        error_declaracion(var)
                    else:
                        pass
        else:
            pass

        
        
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
        if p[1] != None and p[3] != None:
            if not isinstance(p[1],list) and not isinstance(p[3],list):
                if type(p[1]) == type(p[3]):
                    pass
                else:
                    error_tipo(type(p[1]).__name__, p[3])
                    return
                p[0] = [p[1], p[2], p[3]]
            elif isinstance(p[1],list) and p[1][0] == '$' and not isinstance(p[3],list):
                var1 = p[1][1]
                if existe_variable(var1):
                    tipo_var1 = variables[var1][0]
                    if type(tipo_var1) == type(p[3]):
                        pass
                    else:
                        error_tipo(type(tipo_var1).__name__, p[3])
                        return
                else:
                    error_declaracion(var1)
                    return
                p[0] = [p[1], p[2], p[3]]
            elif not isinstance(p[1],list) and isinstance(p[3],list) and p[3][0] == '$':
                var2 = p[3][1]
                if existe_variable(var2):
                    tipo_var2 = variables[var2][0]
                    if type(p[1]) == type(tipo_var2):
                        pass
                    else:
                        error_tipo(p[1], tipo_var2)
                        return
                else:
                    error_declaracion(var2)
                    return
                p[0] = [p[1], p[2], p[3]]
            else:
                if(p[1][0] == '$' and p[3][0] == '$'):
                    var1 = p[1][1]
                    var2 = p[3][1]
                    if existe_variable(var2) and existe_variable(var1):
                        tipo_var1 = variables[var1][0]
                        tipo_var2 = variables[var2][0]
                        if type(tipo_var1) == type(tipo_var2):
                            pass
                        else:
                            error_tipo(type(tipo_var1).__name__, tipo_var2)
                            return
                    elif not existe_variable(var2) and existe_variable(var1):
                        error_declaracion(var2)
                        return
                    elif existe_variable(var2) and not existe_variable(var1):
                        error_declaracion(var1)
                        return
                    else:
                        error_declaracion(var1)
                        error_declaracion(var2)
                        return
                    p[0] = [p[1], p[2], p[3]]
                else:
                    if type(p[1]) == type(p[3]):
                        pass
                    else:
                        error_tipo(type(p[1]).__name__, p[3])
                        return
                p[0] = [p[1], p[2], p[3]]
        else:
            pass
        


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
        lista = p[7]
        for element in lista:
            if tipo_elemento == type(None):
                variables[p[5]] = [lista, f"LIST<{p[3]}>"]
            else:
                if isinstance(element, tipo_elemento):
                    pass
                else:
                    error_tipo(tipo_elemento.__name__, element)
                    return
        variables[p[5]] = [lista, f"LIST<{p[3]}>"]


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
        if len(p) == 9 and 'return' in p[7]:
            error_void(func_name)
        elif len(p) == 8 and 'return' in p[6]:
            error_void(func_name)
        else:
            pass

    
    def p_return(p):
        'return : RETURN valor DOTCOMMA'
        p[0] = p[1]
                

    def p_Comparador(p):
        '''Comparador : EQUALS EQUALS
                        | LANGLE
                        | RANGLE
                        | LANGLE EQUALS
                        | RANGLE EQUALS
                        | NEQ'''
        #Semantico - Katherine Tumbaco 
        if len(p) == 2:
            p[0] = p[1]  
        else:
            p[0] = (p[1], p[2])

    def p_estructura_tupla(p):
        'estructura_tupla : TUPLE LANGLE tipo RANGLE VARIABLE EQUALS tupla DOTCOMMA'
        tipo_elemento = type_map[p[3]]
        tupla = p[7]
        for element in tupla:
            if tipo_elemento == type(None):
                variables[p[5]] = [tupla, f"TUPLE<{p[3]}>"]
            else:
                if isinstance(element, tipo_elemento):
                    pass
                else:
                    error_tipo(tipo_elemento.__name__, element)
                    return
        variables[p[5]] = [tupla, f"TUPLE<{p[3]}>"]
        

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
            p[0] =  [p[1]] + p[3]

            
    def p_Bool(p):
        '''Bool : TRUE
            | FALSE '''
        p[0] = bool(p[1])


    def p_valor(p):
        '''
        valor   : variable
                | NUMBER
                | FLOAT
                | CHAINCHAR
                | Bool
                | tupla
                | lista
                | cuerpo_conjunto
                | cuerpo_Diccionario
        '''
        p[0] = p[1]

    def p_variables(p):
        '''variables : variable
                    | variable COMMA variables'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_variable(p):
        '''variable : DOLLAR VARIABLE
                    | tipo VARIABLE'''
        p[0] = [p[1],p[2]]


    def p_tipo(p):
        '''tipo : MAP
                | DOUBLE
                | STRING
                | INT
                | SET
                | LIST
                | BOOLEAN
                | TUPLE
                | VAR
        '''
        p[0] = p[1]

    #Richard

    def p_declaracion(p):
        """
        declaracion : tipo VARIABLE EQUALS valor DOTCOMMA
        """
        
        tipo_variable = type_map[p[1]]
        valor = p[4]
        if not isinstance(valor,list):
            if tipo_variable == type(None):
                variables[p[2]] = [valor, p[1]]
            else:
                if isinstance(valor, tipo_variable):
                    variables[p[2]] = [valor, p[1]]
                else:
                    error_tipo(tipo_variable.__name__, valor)
                    return
        else:
            var = valor[1]
            if not existe_variable(var):
                error_declaracion(var)
            else:
                tipo_var_declarada = variables[var][1]
                if tipo_variable.__name__ == tipo_var_declarada:
                    variables[p[2]] = variables[var]
                else:
                    error_tipo( tipo_variable.__name__, variables[var][0] )
                    return
        p[0] = [p[1], p[2], p[4]]
        

    def p_operacion(p):
        'operacion : valor operador expresion'

        if not isinstance(p[1],int) and not isinstance(p[1],float):
            error_valor()
            

    def p_expresion(p):
        '''expresion : LPAREN valor operador expresion RPAREN
                        | valor '''
        if len(p) == 2:
            p[0] = p[1]    
        else:
            if not isinstance(p[2], (int, float)):
                error_expresion()
            elif not isinstance(p[4], (int, float)):
                error_expresion()
            elif p[3] == '+' and isinstance(p[2], type(p[4])):
                p[0] = p[2] + p[4]
            elif p[3] == '-' and isinstance(p[2], type(p[4])):
                p[0] = p[2] - p[4]
            elif p[3] == '*' and isinstance(p[2], type(p[4])):
                p[0] = p[2] * p[4]
            elif p[3] == '/' and isinstance(p[2], type(p[4])):
                p[0] = p[2] / p[4]
            else:
                error_expresion()

    

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
        'funcion_flecha : tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION cuerpo DOTCOMMA'
        for valor in p[4]:
            var = valor[1]
            if not isinstance(var,str) or not var.isidentifier():
                error_parametro(var)

    

    def p_funcion_flecha_no_param(p):
        'funcion_flecha : tipo VARIABLE LPAREN RPAREN ARROWFUNCTION cuerpo DOTCOMMA'
    #----------------------------------------------------------


    #----------------CONJUNTOS---------------------------------
    def p_Conjunto(p):
        '''Conjunto : SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA
                        | SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMA'''
        if len(p) == 6:
            variables[p[2]] = [p[4], "SET"]
        else:
            tipo_elemento = type_map[p[3]]
            cuerpo_conjunto = p[7]
            
            for elemento in cuerpo_conjunto:
                if tipo_elemento == type(None):
                    if not isinstance(elemento, (int, float, str, tuple)):
                        error_tipo_mutable(elemento)
                        return
                else:
                    if isinstance(elemento, tipo_elemento):
                        pass
                    else:
                        error_tipo(tipo_elemento.__name__, elemento )
                        return
            
            variables[p[5]] = [cuerpo_conjunto, f"SET<{p[3]}>"]

    def p_cuerpo_conjunto(p):
        '''cuerpo_conjunto : LBRACE valores RBRACE
                    | LBRACE RBRACE '''
        
        if len(p) == 4:
                p[0] = set()
                for valor in p[2]:
                    try:
                        p[0].add(valor)
                    except TypeError:
                        error_tipo_mutable(valor)
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
        variable_control = p[3][1]
        # Obtenemos la condición de terminación
        condicion_terminacion = p[4]
        # Obtenemos el contador
        contador = p[6]
        # Verificamos que la variable de control exista
        if existe_variable(variable_control):
            valor_actual = variables[variable_control][0]
            # Determinamos el valor de terminación de la condición
            print(condicion_terminacion)
            if condicion_terminacion!= None:
                if not isinstance(condicion_terminacion[2], list):
                    if condicion_terminacion[1] == "<":
                        valor_terminacion = condicion_terminacion[2]
                        if valor_actual >= valor_terminacion:
                            error_ciclo(variable_control)
                            return
                        else:
                            if contador[1] == "-" and contador[2] == "-":
                                error_ciclo(variable_control)
                                return
                            else:
                                pass
                    elif condicion_terminacion[1] == ('<', '='):
                        valor_terminacion = condicion_terminacion[2]
                        if valor_actual > valor_terminacion:
                            error_ciclo(variable_control)
                            return
                        elif valor_actual == valor_terminacion:
                            pass
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
                    elif condicion_terminacion[1] == ('>', '='):
                        valor_terminacion = condicion_terminacion[2]
                        if valor_actual < valor_terminacion:
                            error_ciclo(variable_control)
                            return
                        elif valor_actual == valor_terminacion:
                            pass
                        else:
                            if contador[1] == "+" and contador[2] == "+":
                                error_ciclo(variable_control)
                                return
                else:
                    if not existe_variable(condicion_terminacion[2][1]):
                        error_declaracion(condicion_terminacion[2][1])
                        return
                    else:
                        if condicion_terminacion[1] == "<":
                            valor_terminacion = variables[condicion_terminacion[2][1]][0]
                            if valor_actual >= valor_terminacion:
                                error_ciclo(variable_control)
                                return
                            else:
                                if contador[1] == "-" and contador[2] == "-":
                                    error_ciclo(variable_control)
                                    return
                        elif condicion_terminacion[1] == ('<', '='):
                            valor_terminacion = variables[condicion_terminacion[2][1]][0]
                            if valor_actual > valor_terminacion:
                                error_ciclo(variable_control)
                                return
                            elif valor_actual == valor_terminacion:
                                pass
                            else:
                                if contador[1] == "-" and contador[2] == "-":
                                    error_ciclo(variable_control)
                                    return
                        elif condicion_terminacion[1] == ">":
                            valor_terminacion = variables[condicion_terminacion[2][1]][0]
                            if valor_actual <= valor_terminacion:
                                error_ciclo(variable_control)
                                return
                            else:
                                if contador[1] == "+" and contador[2] == "+":
                                    error_ciclo(variable_control)
                                    return
                        elif condicion_terminacion[1] == ('>', '='):
                            valor_terminacion = variables[condicion_terminacion[2][1]][0]
                            if valor_actual < valor_terminacion:
                                error_ciclo(variable_control)
                                return
                            elif valor_actual == valor_terminacion:
                                pass
                            else:
                                if contador[1] == "+" and contador[2] == "+":
                                    error_ciclo(variable_control)
                                    return
            else:
                pass
        else:
            error_declaracion(variable_control)


    

    def p_contador(p):
        '''contador : variable PLUS PLUS
                    | variable PLUS EQUALS valor
                    | variable MINUS MINUS
                    | variable MINUS EQUALS valor'''
        if existe_variable(p[1][1]):
            pass
        else:
            error_declaracion(p[1][1])
        p[0] = [p[1][1]] + [p[2], p[3]]
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
            if  tipo_clave != type(None) and tipo_valor == type(None):
                if not isinstance(clave, tipo_clave):
                    error_tipo(tipo_clave.__name__, clave)
                    return
            elif tipo_clave == type(None) and tipo_valor != type(None):
                if not isinstance(valor, tipo_valor):
                    error_tipo(tipo_valor.__name__, valor)
                    return
            elif tipo_clave == type(None) and tipo_valor == type(None):
                variables[p[7]] = [cuerpo_dic, f"MAP<{p[3]}, {p[5]}>"]
            else:
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
            agregar_dupla(p[0], p[1])
        else:
            p[0] = {}
            agregar_dupla(p[0], p[1])
            p[0].update(p[3])

    def p_dupla(p):
        '''dupla : valor TWODOTS valor
        '''
        p[0] = [p[1], p[3]]

    def agregar_dupla(diccionario, dupla):
        clave, valor = dupla
        try:
            diccionario[clave] = valor
        except TypeError:
            error_tipo_mutable(clave)
            return
        

    #---------------Funciones de Errores semánticos-------------------------------------------    
    def error_tipo_mutable(p):
        print(f"Error semántico: Tipo mutable '{p}' no es válido.")
        with open("datos.txt", "a") as archivo:
            archivo.write(f"Error semántico: Tipo mutable '{p}' no es válido. ಥ_ಥ¯\_(ツ)_/¯\n")
        
    def error_declaracion(p):
        print(f"Error semántico: La variable '{p}' no ha sido declarada.")
        with open("datos.txt", "a") as archivo:
            archivo.write(f"Error semántico: La variable '{p}' no ha sido declarada. ಥ_ಥ¯\_(ツ)_/¯\n")

    def existe_variable(p):
        return isinstance(p, str) and p in variables

    def error_tipo(p1, p2):
        print(f"Error semántico: Tipos incompatibles '{p1}' y '{type(p2).__name__}'.\n")
        with open("datos.txt", "a") as archivo:
            archivo.write(f"Error semántico: Tipos incompatibles '{p1}' y '{type(p2).__name__}'. ಥ_ಥ¯\_(ツ)_/¯\n")
    
    def error_ciclo(variable):
        print(f"Error semántico: El ciclo for con la variable de control '{variable}' jamás se ejecuta o se ejecuta infinitas veces.\n")
        with open("datos.txt", "a") as archivo:
            archivo.write(f"Error semántico: El ciclo for con la variable de control '{variable}' jamás se ejecuta o se ejecuta infinitas veces. ಥ_ಥ¯\_(ツ)_/¯\n")
    
    def error_expresion():
        print('Error semántico: Los valores en la expresion deben ser numérico\n')
        with open("datos.txt", "a") as archivo:
            archivo.write('Error semántico: Los valores en la expresion deben ser numérico ಥ_ಥ¯\_(ツ)_/¯\n')

    def error_valor():
        print('Error semántico: El valor en la operacion debe ser numérico\n')
        with open("datos.txt", "a") as archivo:
            archivo.write('Error semántico: El valor en la operacion debe ser numérico ಥ_ಥ¯\_(ツ)_/¯\n')

    def error_void(p):
        print(f"Error semántico: La función '{p}' declarada como 'void' no debe contener un retorno 'return'.")
        with open("datos.txt", "a") as archivo:
            archivo.write(f"Error semántico: La función '{p}' declarada como 'void' no debe contener un retorno 'return'. ಥ_ಥ¯\_(ツ)_/¯\n")

    def error_parametro(p):
        print(f'Error semantico: Parametro "{p}" incorrecto. Los parametros de la funcion flecha deben ser nombres de variables\n')
        with open("datos.txt", "a") as archivo:
            archivo.write(f'Error semantico: Parametro "{p}" incorrecto. Los parametros de la funcion flecha deben ser nombres de variables ಥ_ಥ¯\_(ツ)_/¯\n')
    #----------------------------------------------------------
    # Crear el directorio de logs si no existe
    #log_dir = "logs_semantico"
    #if not os.path.exists(log_dir):
    #    os.makedirs(log_dir)
        
    # Obtener la hora actual para los nombres de archivo de log
    #current_time = datetime.now().strftime("%d%m%Y-%Hh%M")
    #UsuariosGit = "rocaenca"

    # Nombre del archivo de log
    #log_filename = f"semantico-{UsuariosGit}-{current_time}.txt"
    #log_filepath = os.path.join(log_dir, log_filename)

    # Archivo de log para escribir
    #log_file = open(log_filepath, 'w')
    # Error rule for syntax errors
    def p_error(p):
        if p:
            error_msg = f"Error sintáctico en el token '{p.value}' en la linea {p.lineno}, posicion {p.lexpos} ಥ_ಥ¯\_(ツ)_/¯\n"
        else:
            error_msg = "Error sintáctico en el final del token ಥ_ಥ¯\_(ツ)_/¯\n"
        with open("datos.txt", "a") as archivo:
            archivo.write(error_msg)

    # Build the parser
    parser = yacc.yacc()
       
    # Limpieza del archivo de errores anterior
    with open("datos.txt", "w") as archivo:
        archivo.write('')

    def parse_input(input_string):
        result = parser.parse(input_string)
        return result

    with open('codigo.txt', 'r') as archiCodigo:
        codAnalizar = archiCodigo.read()

    result = parse_input(codAnalizar)

    with open('datos.txt', 'a') as archivo:
        print(result)
        if result and None not in result:
            archivo.write(f"{result}")

    with open('datos.txt', 'r') as archivo:
        contenido = archivo.read()
        cajaconsole.delete("1.0", tk.END)
        cajaconsole.insert(tk.END, contenido)
        ventana.update()

    archivo = open('datos.txt','r')
    if len(archivo.readlines()) == 0: 
      cajaconsole.delete("1.0", tk.END)
      cajaconsole.insert(tk.END,"Compile successfully (👉ﾟヮﾟ)👉💻💻🧑🏽‍💻🧑🏽‍💻")
    archivo.close()
#---------------------  INTERFAZ -------------------------------------
import tkinter as tk

# Función para lp >
def update_lp(event=None):
    line_prefixes = ''
    for i in range(1, int(cajacodigo.index('end').split('.')[0])):
        line_prefixes += 'lp >\n'
    linea_lp.config(state='normal')
    linea_lp.delete('1.0', tk.END)
    linea_lp.insert('1.0', line_prefixes)
    linea_lp.config(state='disabled')

# Crear ventana principal
ventana = tk.Tk()
ventana.title("DARTLSS")
ventana.geometry("875x575")
ventana.configure(bg='#000000')

# Crear widgets
titulo = tk.Label(ventana, text="DARTLSS\n Simple Dart Syntax Checker \n Elaborado por: Katherine Tumbaco - Richard Perez - Roberto Encalada",
                  font=("Courier", 12, "italic"), bg="black", fg="white", anchor="center")

textocod = tk.Label(ventana, text="Write your syntax here",
                    font=("Courier", 11), bg="black", fg="white")

textoconsola = tk.Label(ventana, text="Console",
                        font=("Courier", 12), bg="black", fg="white")

cajacodigo = tk.Text(ventana, width=85, height=15, bg='#515150', fg='white',
                     font=('monospace', 12), insertbackground='white', bd=0, highlightthickness=0)

linea_lp = tk.Text(ventana, width=4, height=15, bg='#515150', fg='white', 
                      font=('monospace', 12), state='disabled', bd=0, highlightthickness=0)

cajaconsole = tk.Text(ventana, width=50, height=15, bg='#293742', fg='white',
                      font=('monospace', 12), insertbackground='white', bd=0, highlightthickness=0)

cajafiles = tk.Text(ventana, width=15, height=2, bg='#ECEEF1', fg='black',
                    font=('monospace', 12))

btcheck = tk.Button(ventana, text="Check", width=15, height=2, font=('sans-serif', 12, 'bold'),
                    command=lambda: textoconsole(), bg='#27AE60', fg='white')

btfile = tk.Button(ventana, text="Open file", width=16, height=2, font=('sans-serif', 12, 'bold'),
                   command=procesar_archivo, bg='#27AE60', fg='white')

# Disposición de widgets
titulo.grid(row=0, column=0, columnspan=5, padx=(75,10), pady=20, sticky='nsew')

btfile.grid(row=1, column=0, columnspan=2, sticky='n', pady=10, padx=20, )
cajafiles.grid(row=1, column=2, columnspan=4, pady=10, padx=1, sticky='nsew')

textocod.grid(row=2, column=0, columnspan=2, pady=5, padx=(15,5), sticky='w')
btcheck.grid(row=2, column=2, columnspan=1, pady=5, padx=(0,1), sticky='w')

textoconsola.grid(row=2, column=3, pady=5, padx=(15,1),sticky='w')

linea_lp.grid(row=3, column=0, pady=10, sticky='nse')
cajacodigo.grid(row=3, column=1, columnspan=3, pady=10, sticky='nsew')
cajaconsole.grid(row=3, column=3, columnspan=4, padx=10, pady=10, sticky='nsew')

cajacodigo.bind('<KeyRelease>', update_lp)
update_lp()  

ventana.mainloop()
#----------------------------------------------------------