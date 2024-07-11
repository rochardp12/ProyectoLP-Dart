import ply.lex as lex
import os
from datetime import datetime

# List of token names.   This is always required
reserved = {
    #Roberto Encalada
    'main': 'MAIN',
    'map': 'MAP',
    'double':'DOUBLE',
    'if':'IF',
    'else':'ELSE',
    'return':'RETURN',
    'True':'TRUE',
    'False':'FALSE',
    #Richard Perez
    "String": "STRING",
    "int": "INT",
    "print": "PRINT",
    "Set": "SET",
    "switch": "SWITCH",
    "case": "CASE",
    #Katherine Tumbaco
    "void": "VOID",
    "for": "FOR",
    "var": "VAR",
    "break": "BREAK",
    "List": "LIST",
    "boolean": "BOOLEAN",
    "tuple": "TUPLE",
    }
tokens = (
    #Katherine Tumbaco
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LANGLE',
    'RANGLE',
    #Roberto Encalada
    'VARIABLE',
    'COMMA',
    'EQUALS',
    'NEQ',
    'DOT',
    'TWODOTS',
    'DOTCOMMA',
    'DOLLAR',
    'OR',
    'AND',
    'COMMENTLINE',
    'COMMENTBLOCK',
    'CHAINCHAR',
    #Richard Perez
    'ARROWFUNCTION',
) + tuple(reserved.values())

# Regular expression rules for simple tokens

#Katherine Tumbaco
t_NEQ = r'!='
t_DOT = r'\.'
t_TWODOTS = r':'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_DOTCOMMA = r';'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MINUS = r'-'
#Roberto Encalada
t_LANGLE = r'<'
t_RANGLE = r'>'
t_DOLLAR = r'\$'
t_OR = r'\|\|'
t_AND = r'&&'
t_COMMENTLINE = r'\/\/[^\n\t\r]*'
t_COMMENTBLOCK = r'/\*(.|\n)*?\*/'
t_CHAINCHAR = r'(\'[^\']*\'|\"[^\"]*\")'
#Richard Perez
t_COMMA   = r','
t_EQUALS  = r'='
t_ARROWFUNCTION = r'=>'
t_PLUS    = r'\+'


#Katherine Tumbaco
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
    
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
  error_msg = f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos} ಥ_ಥ¯\_(ツ)_/¯\n"
  with open("datos.txt", "a") as archivo:
      archivo.write(error_msg)
  print(error_msg)
  t.lexer.skip(1)





#Katherine Tumbaco
algoritmoKatherine = """
void main() {
  int num1 = 10;
  int num2 = 5;

  // Operación de suma
  int resultadoSuma = $num1 + $num2;
  
  // Operación de resta
  int resultadoResta = $num1 - $num2;

  // Verificación del resultado de la suma
  if ($resultadoSuma > 0) {
    print("La suma de $num1 y $num2 es positiva: $resultadoSuma");
  } else if ($resultadoSuma < 0) {
    print("La suma de $num1 y $num2 es negativa: $resultadoSuma");
  } else {
    print("La suma de $num1 y $num2 es cero.");
  }

  // Verificación del resultado de la resta
  if ($resultadoResta > 0) {
    print("La resta de $num1 y $num2 es positiva: $resultadoResta");
  } else if ($resultadoResta < 0) {
    print("La resta de $num1 y $num2 es negativa: $resultadoResta");
  } else {
    print("La resta de $num1 y $num2 es cero.");
  }
}

"""

algoritmoRichard = """
        void Pais() {
  String nombre = "Ecuador";
  boolean ganoMundial = True;
  int cantidad = 3;



  String cantidadMundiales() => print($cantidad);;
}


void main() {
  // Crear un conjunto de países
  Set<tuple> paises = {
    ('Brasil', True, 5),
    ('Argentina', True, 3),
    ('España', True, 1),
    ('Italia', True, 4),
    ('México', False, 0),
    ('Japón', False, 0),
  };

  // Recorrer el conjunto de países y aplicar el switch en ganoMundial
  for (int i = 0; i < $paises; $i++) {
    switch ($pais) {
      case True:
        print('GANÓ: ', $pais);
      case False:
        print('NO GANÓ:',  $pais);
    }
  }
}


        """
AlgoritmoRoberto = """
/* Block comment example
This is a test for the block comment token.
*/

// Line comment example
void main(){
    int number = 42;
    double decimalNumber = 3.14;
    boolean isValid = True;
    String CONSTANT_STRING = "Hello";
    List<int> myList = [1,3,2];
    map<String, int> myMap = {
        "hola": 1, 
        "adios": 2
        };

    void main() {
        var instance = "Hello, World!";
        instance.testMethod();
    }

    void testMethod() {
        int localVar = 10;
        double pi = 3.14;
        boolean flag = False;
        String greeting = "Hello, World!";
        String initial = "A";
        
        if ($localVar > 5 && $flag == False) {
            print("localVar is greater than 5");
        } else {
            print("localVar is less than or equal to 5");
        }

        for (int i = 0; $i < 10; $i++) {
            print($i);
        }

        switch ($localVar) {
            case 0:
                print("localVar is zero");
                break;
        }

    }

    void nullCheck() {
        int obj1 = 1;
        int obj2 = 2;
        if ($obj1 == $obj2) {
            print("var is obj");
        }
    }

    void thisCheck() {
        int obj1 = 1;
        int obj2 = 2;
        if ($obj1 == $obj2) {
            print("This object");
        }
    }

    @print() {
        String message = "Hello, World!";
        print($message);
    }
}
"""
algoritmos = [AlgoritmoRoberto]

# Build the lexer
lexer = lex.lex()

#Generate logs
"""log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

UsuariosGit = ["rocaenca"]
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")

for i in range(len(algoritmos)):
  log_filename = f"lexico-{UsuariosGit[i]}-{current_time}.txt"
  log_filepath = os.path.join(log_dir, log_filename)
  lexer.input(algoritmos[i])"""


# Tokenize
with  open("codigo.txt", "r") as archivo:
  codigo = archivo.read()
  lexer.input(codigo)

with open("datos.txt", "w") as error_file:
  while True:
      tok = lexer.token()
      if not tok: 
          break      # No more input
      print(tok)
      error_file.write(f"{tok}\n")
