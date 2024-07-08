
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ADMIRATION AND ARROWFUNCTION AS BOOLEAN BREAK CASE CATCH CHAINCHAR CLASS COMMA COMMENTBLOCK COMMENTLINE CONST DEF DEFAULT DIVIDE DOLLAR DOT DOTCOMMA DOUBLE DYNAMIC ELIF ELSE ENUM EQUALS EXTENDS FALSE FINAL FINALLY FLOAT FOR IF IN INT INTEGERDIVISION INTERFACE IS LANGLE LBRACE LBRACKET LIST LPAREN MAIN MAP METHOD MINUS MOD MODULE NEQ NEW NULL NUMBER OR PLUS PRINT PRIVATE PROTECTED PUBLIC RANGLE RBRACE RBRACKET RETURN RPAREN SET STATIC STRING SUPER SWITCH THIS TIMES TRUE TRY TWODOTS TYPEDEF VAR VARIABLE VOID WHILEprograma : cuerpo\n                | programa cuerpocuerpo : impresion\n              | declaracion\n              | operacion\n              | comentario\n              | estructuras_de_Control\n            estructuras_de_Control : sentencia_If\n                            | sentencia_Switch\n                            | ciclo_for\n                            | funcion_Anonima\n                            | diccionario\n                            | Conjunto\n                            | funcion_flecha\n                            | funcion_Void\n                            | funcion\n                            | funcion_Data\n                            | RETURN VARIABLE\n                            | estructura_List\n    comentario : COMMENTLINE\n                  | COMMENTBLOCKimpresion : PRINT LPAREN valores RPAREN DOTCOMMA\n                 | PRINT LPAREN operacion RPAREN DOTCOMMA\n                 | PRINT LPAREN RPAREN DOTCOMMA\n     sentencia_If : IF LPAREN condicion RPAREN LBRACE programa RBRACE else\n                        | IF LPAREN condicion RPAREN LBRACE programa RBRACE\n    \n    else : ELSE LBRACE programa RBRACE\n    \n    condicion : valor Comparador valor\n            |   condicion conector condicion\n    conector : AND\n                | OR\n    estructura_List : LIST LANGLE tipo RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMAfuncion_Void : VOID VARIABLE LPAREN valores RPAREN LBRACE programa RBRACE DOTCOMMAComparador : EQUALS EQUALS\n                    | LANGLE\n                    | RANGLE\n                    | LANGLE EQUALS\n                    | RANGLE EQUALS\n                    | NEQtupla : LPAREN valores RPARENvalores : valor\n               | valor COMMA valoresBool : TRUE\n        | FALSE \n    valor   : VARIABLE\n            | NUMBER\n            | FLOAT\n            | CHAINCHAR\n            | Bool\n            | tupla\n    tipo : MAP\n            | DOUBLE\n            | STRING\n            | INT\n            | SET\n            | LIST\n            | BOOLEAN\n            | FINAL\n            | CONST\n            | DYNAMIC\n    \n    declaracion : tipo VARIABLE EQUALS valor DOTCOMMA\n                | VAR VARIABLE EQUALS valor DOTCOMMA\n    operacion : valor operador expresionexpresion : LPAREN valor operador expresion RPAREN\n                    | valor funcion : VARIABLE LPAREN valores RPARENfuncion_Data : VARIABLE DOT VARIABLE LPAREN valores RPAREN DOTCOMMAsentencia_Switch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACEcaso : CASE valor TWODOTS programa BREAK DOTCOMMA caso \n            | CASE valor TWODOTS programa BREAK DOTCOMMA funcion_flecha : tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMAfuncion_flecha : tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMAConjunto : SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA\n                    | SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMAcuerpo_conjunto : LBRACE valores RBRACE\n                | LBRACE RBRACE operador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE \n    ciclo_for : FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa  RBRACE\n    contador : VARIABLE PLUS PLUS\n                | VARIABLE PLUS EQUALS valor\n                | VARIABLE MINUS MINUS\n                | VARIABLE MINUS EQUALS valor\n    funcion_Anonima : VAR VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA\n                    | tupla LBRACE programa RBRACE DOTCOMMA\n    diccionario : MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA\n    cuerpo_Diccionario : LBRACE duplas RBRACE\n                    | LBRACE RBRACE\n    duplas : dupla\n              | dupla COMMA duplas\n    dupla : valor TWODOTS valor\n    '
    
_lr_action_items = {'PRINT':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[8,8,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,8,-40,-65,-63,8,-24,-66,-22,-23,-61,8,-62,8,-73,-87,8,8,8,8,8,8,8,-72,-67,-64,-26,-68,8,-71,-86,-74,-25,8,8,8,8,8,-33,-88,-32,8,-81,-27,]),'VAR':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,72,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[13,13,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,13,101,-40,-65,-63,13,-24,-66,-22,-23,-61,13,-62,13,-73,-87,13,13,13,13,13,13,13,-72,-67,-64,-26,-68,13,-71,-86,-74,-25,13,13,13,13,13,-33,-88,-32,13,-81,-27,]),'COMMENTLINE':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[14,14,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,14,-40,-65,-63,14,-24,-66,-22,-23,-61,14,-62,14,-73,-87,14,14,14,14,14,14,14,-72,-67,-64,-26,-68,14,-71,-86,-74,-25,14,14,14,14,14,-33,-88,-32,14,-81,-27,]),'COMMENTBLOCK':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[15,15,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,15,-40,-65,-63,15,-24,-66,-22,-23,-61,15,-62,15,-73,-87,15,15,15,15,15,15,15,-72,-67,-64,-26,-68,15,-71,-86,-74,-25,15,15,15,15,15,-33,-88,-32,15,-81,-27,]),'RETURN':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[26,26,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,26,-40,-65,-63,26,-24,-66,-22,-23,-61,26,-62,26,-73,-87,26,26,26,26,26,26,26,-72,-67,-64,-26,-68,26,-71,-86,-74,-25,26,26,26,26,26,-33,-88,-32,26,-81,-27,]),'MAP':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[28,28,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,88,88,88,28,88,-40,-65,-63,28,-24,-66,88,-22,-23,-61,28,-62,28,-73,-87,28,28,28,28,28,28,28,-72,-67,-64,-26,-68,28,-71,-86,-74,-25,28,28,28,28,28,-33,-88,-32,28,-81,-27,]),'DOUBLE':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[29,29,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,29,29,29,29,29,-40,-65,-63,29,-24,-66,29,-22,-23,-61,29,-62,29,-73,-87,29,29,29,29,29,29,29,-72,-67,-64,-26,-68,29,-71,-86,-74,-25,29,29,29,29,29,-33,-88,-32,29,-81,-27,]),'STRING':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[30,30,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,30,30,30,30,30,-40,-65,-63,30,-24,-66,30,-22,-23,-61,30,-62,30,-73,-87,30,30,30,30,30,30,30,-72,-67,-64,-26,-68,30,-71,-86,-74,-25,30,30,30,30,30,-33,-88,-32,30,-81,-27,]),'INT':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[31,31,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,31,31,31,31,31,-40,-65,-63,31,-24,-66,31,-22,-23,-61,31,-62,31,-73,-87,31,31,31,31,31,31,31,-72,-67,-64,-26,-68,31,-71,-86,-74,-25,31,31,31,31,31,-33,-88,-32,31,-81,-27,]),'SET':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[32,32,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,90,90,90,32,90,-40,-65,-63,32,-24,-66,90,-22,-23,-61,32,-62,32,-73,-87,32,32,32,32,32,32,32,-72,-67,-64,-26,-68,32,-71,-86,-74,-25,32,32,32,32,32,-33,-88,-32,32,-81,-27,]),'LIST':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[33,33,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,91,91,91,33,91,-40,-65,-63,33,-24,-66,91,-22,-23,-61,33,-62,33,-73,-87,33,33,33,33,33,33,33,-72,-67,-64,-26,-68,33,-71,-86,-74,-25,33,33,33,33,33,-33,-88,-32,33,-81,-27,]),'BOOLEAN':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[34,34,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,34,34,34,34,34,-40,-65,-63,34,-24,-66,34,-22,-23,-61,34,-62,34,-73,-87,34,34,34,34,34,34,34,-72,-67,-64,-26,-68,34,-71,-86,-74,-25,34,34,34,34,34,-33,-88,-32,34,-81,-27,]),'FINAL':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[35,35,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,35,35,35,35,35,-40,-65,-63,35,-24,-66,35,-22,-23,-61,35,-62,35,-73,-87,35,35,35,35,35,35,35,-72,-67,-64,-26,-68,35,-71,-86,-74,-25,35,35,35,35,35,-33,-88,-32,35,-81,-27,]),'CONST':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[36,36,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,36,36,36,36,36,-40,-65,-63,36,-24,-66,36,-22,-23,-61,36,-62,36,-73,-87,36,36,36,36,36,36,36,-72,-67,-64,-26,-68,36,-71,-86,-74,-25,36,36,36,36,36,-33,-88,-32,36,-81,-27,]),'DYNAMIC':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,65,67,68,69,72,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[37,37,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,37,37,37,37,37,-40,-65,-63,37,-24,-66,37,-22,-23,-61,37,-62,37,-73,-87,37,37,37,37,37,37,37,-72,-67,-64,-26,-68,37,-71,-86,-74,-25,37,37,37,37,37,-33,-88,-32,37,-81,-27,]),'VARIABLE':([0,1,2,3,4,5,6,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,47,48,49,50,53,54,56,57,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,88,90,91,95,99,100,101,102,104,110,111,117,118,119,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,158,159,161,162,165,166,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[11,11,-1,-3,-4,-5,-6,-7,53,55,63,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,64,-19,-51,-52,-53,-54,66,-56,-57,-58,-59,-60,-46,-47,-48,-49,73,-43,-44,-2,53,-45,-50,53,83,53,-77,-78,-79,-80,-18,11,53,53,-40,53,53,53,-65,-63,53,53,-51,-55,-56,11,53,132,133,53,-24,-66,53,53,148,149,53,-30,-31,53,-35,-36,-39,-22,-23,-61,11,53,-62,11,-73,-87,11,-34,-37,-38,174,53,11,11,11,181,11,53,11,11,-72,-67,-64,53,-26,-68,11,-71,-86,-74,-25,11,11,53,53,53,11,11,11,-33,-88,-32,11,-81,53,53,-27,]),'NUMBER':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,56,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[38,38,-1,-3,-4,-5,-6,-7,38,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,38,-45,-50,38,38,-77,-78,-79,-80,-18,38,38,38,-40,38,38,38,-65,-63,38,38,38,38,38,-24,-66,38,38,38,-30,-31,38,-35,-36,-39,-22,-23,-61,38,38,-62,38,-73,-87,38,-34,-37,-38,38,38,38,38,38,38,38,38,-72,-67,-64,38,-26,-68,38,-71,-86,-74,-25,38,38,38,38,38,38,38,38,-33,-88,-32,38,-81,38,38,-27,]),'FLOAT':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,56,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[39,39,-1,-3,-4,-5,-6,-7,39,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,39,-45,-50,39,39,-77,-78,-79,-80,-18,39,39,39,-40,39,39,39,-65,-63,39,39,39,39,39,-24,-66,39,39,39,-30,-31,39,-35,-36,-39,-22,-23,-61,39,39,-62,39,-73,-87,39,-34,-37,-38,39,39,39,39,39,39,39,39,-72,-67,-64,39,-26,-68,39,-71,-86,-74,-25,39,39,39,39,39,39,39,39,-33,-88,-32,39,-81,39,39,-27,]),'CHAINCHAR':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,56,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[40,40,-1,-3,-4,-5,-6,-7,40,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,40,-45,-50,40,40,-77,-78,-79,-80,-18,40,40,40,-40,40,40,40,-65,-63,40,40,40,40,40,-24,-66,40,40,40,-30,-31,40,-35,-36,-39,-22,-23,-61,40,40,-62,40,-73,-87,40,-34,-37,-38,40,40,40,40,40,40,40,40,-72,-67,-64,40,-26,-68,40,-71,-86,-74,-25,40,40,40,40,40,40,40,40,-33,-88,-32,40,-81,40,40,-27,]),'IF':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[43,43,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,43,-40,-65,-63,43,-24,-66,-22,-23,-61,43,-62,43,-73,-87,43,43,43,43,43,43,43,-72,-67,-64,-26,-68,43,-71,-86,-74,-25,43,43,43,43,43,-33,-88,-32,43,-81,-27,]),'SWITCH':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[44,44,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,44,-40,-65,-63,44,-24,-66,-22,-23,-61,44,-62,44,-73,-87,44,44,44,44,44,44,44,-72,-67,-64,-26,-68,44,-71,-86,-74,-25,44,44,44,44,44,-33,-88,-32,44,-81,-27,]),'FOR':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[45,45,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,45,-40,-65,-63,45,-24,-66,-22,-23,-61,45,-62,45,-73,-87,45,45,45,45,45,45,45,-72,-67,-64,-26,-68,45,-71,-86,-74,-25,45,45,45,45,45,-33,-88,-32,45,-81,-27,]),'VOID':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,69,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[46,46,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,46,-40,-65,-63,46,-24,-66,-22,-23,-61,46,-62,46,-73,-87,46,46,46,46,46,46,46,-72,-67,-64,-26,-68,46,-71,-86,-74,-25,46,46,46,46,46,-33,-88,-32,46,-81,-27,]),'TRUE':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,56,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[47,47,-1,-3,-4,-5,-6,-7,47,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,47,-45,-50,47,47,-77,-78,-79,-80,-18,47,47,47,-40,47,47,47,-65,-63,47,47,47,47,47,-24,-66,47,47,47,-30,-31,47,-35,-36,-39,-22,-23,-61,47,47,-62,47,-73,-87,47,-34,-37,-38,47,47,47,47,47,47,47,47,-72,-67,-64,47,-26,-68,47,-71,-86,-74,-25,47,47,47,47,47,47,47,47,-33,-88,-32,47,-81,47,47,-27,]),'FALSE':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,56,58,59,60,61,62,64,69,70,71,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[48,48,-1,-3,-4,-5,-6,-7,48,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,48,-45,-50,48,48,-77,-78,-79,-80,-18,48,48,48,-40,48,48,48,-65,-63,48,48,48,48,48,-24,-66,48,48,48,-30,-31,48,-35,-36,-39,-22,-23,-61,48,48,-62,48,-73,-87,48,-34,-37,-38,48,48,48,48,48,48,48,48,-72,-67,-64,48,-26,-68,48,-71,-86,-74,-25,48,48,48,48,48,48,48,48,-33,-88,-32,48,-81,48,48,-27,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,11,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,43,44,45,47,48,49,50,53,54,55,56,58,59,60,61,62,64,69,70,71,73,78,79,80,81,83,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[9,9,-1,-3,-4,-5,-6,-7,50,9,56,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,70,71,72,-43,-44,-2,9,-45,-50,81,9,86,-77,-78,-79,-80,-18,9,9,9,102,-40,9,9,9,111,-65,-63,9,9,9,9,9,-24,-66,9,9,9,-30,-31,9,-35,-36,-39,-22,-23,-61,9,86,-62,9,-73,-87,9,-34,-37,-38,9,9,9,9,9,9,9,9,-72,-67,-64,9,-26,-68,9,-71,-86,-74,-25,9,9,9,9,9,9,9,9,-33,-88,-32,9,-81,9,9,-27,]),'$end':([1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,78,84,85,104,110,135,136,137,142,145,150,177,178,179,184,185,191,192,194,196,213,214,219,222,226,],[0,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,-40,-65,-63,-24,-66,-22,-23,-61,-62,-73,-87,-72,-67,-64,-26,-68,-71,-86,-74,-25,-33,-88,-32,-81,-27,]),'RBRACE':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,52,53,54,64,78,84,85,95,104,106,110,117,135,136,137,142,145,146,150,165,170,171,177,178,179,184,185,190,191,192,194,196,206,210,213,214,215,217,219,220,222,226,227,228,229,230,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-41,-45,-50,-18,-40,-65,-63,120,-24,-42,-66,147,-22,-23,-61,-62,-73,167,-87,180,184,185,-72,-67,-64,-26,-68,204,-71,-86,-74,-25,216,222,-33,-88,223,-91,-32,226,-81,-27,-70,-92,-93,-69,]),'DOTCOMMA':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,75,78,84,85,103,104,105,107,110,113,114,116,120,131,135,136,137,142,145,147,150,152,153,162,163,167,176,177,178,179,180,182,184,185,191,192,194,196,204,205,207,213,214,216,219,221,222,223,226,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,104,-40,-65,-63,135,-24,136,137,-66,142,-50,145,150,158,-22,-23,-61,-62,-73,-76,-87,-29,-28,177,178,-75,191,-72,-67,-64,192,194,-26,-68,-71,-86,-74,-25,213,214,219,-33,-88,-90,-32,227,-81,-89,-27,]),'BREAK':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,64,78,84,85,104,110,135,136,137,142,145,150,177,178,179,184,185,191,192,194,196,209,213,214,219,222,226,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-18,-40,-65,-63,-24,-66,-22,-23,-61,-62,-73,-87,-72,-67,-64,-26,-68,-71,-86,-74,-25,221,-33,-88,-32,-81,-27,]),'PLUS':([11,12,38,39,40,41,42,47,48,53,54,77,78,112,174,188,],[-45,59,-46,-47,-48,-49,-50,-43,-44,-45,-50,59,-40,59,188,200,]),'MINUS':([11,12,38,39,40,41,42,47,48,53,54,77,78,112,174,189,],[-45,60,-46,-47,-48,-49,-50,-43,-44,-45,-50,60,-40,60,189,202,]),'TIMES':([11,12,38,39,40,41,42,47,48,53,54,77,78,112,],[-45,61,-46,-47,-48,-49,-50,-43,-44,-45,-50,61,-40,61,]),'DIVIDE':([11,12,38,39,40,41,42,47,48,53,54,77,78,112,],[-45,62,-46,-47,-48,-49,-50,-43,-44,-45,-50,62,-40,62,]),'DOT':([11,],[57,]),'LANGLE':([28,32,33,38,39,40,41,47,48,53,54,78,97,],[65,67,68,-46,-47,-48,-49,-43,-44,-45,-50,-40,127,]),'COMMA':([29,30,31,34,35,36,37,38,39,40,41,47,48,52,53,54,77,78,88,89,90,91,112,217,229,],[-52,-53,-54,-57,-58,-59,-60,-46,-47,-48,-49,-43,-44,79,-45,-50,79,-40,-51,115,-55,-56,79,224,-93,]),'RANGLE':([29,30,31,34,35,36,37,38,39,40,41,47,48,53,54,78,88,90,91,93,94,97,144,],[-52,-53,-54,-57,-58,-59,-60,-46,-47,-48,-49,-43,-44,-45,-50,-40,-51,-55,-56,118,119,128,166,]),'RPAREN':([38,39,40,41,47,48,50,51,52,53,54,74,76,77,78,81,82,84,85,96,98,106,108,112,134,140,152,153,164,173,179,200,202,211,212,],[-46,-47,-48,-49,-43,-44,75,78,-41,-45,-50,103,105,-41,-40,109,110,-65,-63,121,130,-42,138,-41,160,163,-29,-28,179,187,-64,-82,-84,-83,-85,]),'EQUALS':([38,39,40,41,47,48,53,54,55,63,66,78,97,126,127,128,132,133,148,149,181,188,189,],[-46,-47,-48,-49,-43,-44,-45,-50,80,87,92,-40,126,154,155,156,80,159,168,169,193,201,203,]),'NEQ':([38,39,40,41,47,48,53,54,78,97,],[-46,-47,-48,-49,-43,-44,-45,-50,-40,129,]),'RBRACKET':([38,39,40,41,47,48,52,53,54,78,106,195,],[-46,-47,-48,-49,-43,-44,-41,-45,-50,-40,-42,207,]),'AND':([38,39,40,41,47,48,53,54,78,96,131,152,153,],[-46,-47,-48,-49,-43,-44,-45,-50,-40,123,123,123,-28,]),'OR':([38,39,40,41,47,48,53,54,78,96,131,152,153,],[-46,-47,-48,-49,-43,-44,-45,-50,-40,124,124,124,-28,]),'TWODOTS':([38,39,40,41,47,48,53,54,78,186,218,],[-46,-47,-48,-49,-43,-44,-45,-50,-40,198,225,]),'LBRACE':([42,78,92,114,121,130,160,168,187,193,197,],[69,-40,117,143,151,157,175,117,199,206,208,]),'ARROWFUNCTION':([109,138,],[139,161,]),'CASE':([157,227,],[172,172,]),'LBRACKET':([169,],[183,]),'ELSE':([184,],[197,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,69,139,143,151,161,175,198,199,208,],[1,95,162,165,170,176,190,209,210,220,]),'cuerpo':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[2,49,2,49,2,2,2,2,49,49,49,2,49,49,2,2,2,49,49,49,]),'impresion':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'declaracion':([0,1,69,72,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[4,4,4,99,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'operacion':([0,1,50,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[5,5,76,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'comentario':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'estructuras_de_Control':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'tipo':([0,1,65,67,68,69,72,95,115,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[10,10,89,93,94,10,100,10,144,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'valor':([0,1,9,50,56,58,69,70,71,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[12,12,52,77,52,84,12,97,98,52,107,52,112,113,12,97,52,52,52,97,153,12,84,12,12,113,12,12,12,12,186,12,12,52,12,12,12,211,212,218,12,12,12,12,218,229,]),'sentencia_If':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'sentencia_Switch':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ciclo_for':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'funcion_Anonima':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'diccionario':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Conjunto':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'funcion_flecha':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'funcion_Void':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'funcion':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'funcion_Data':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'estructura_List':([0,1,69,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'Bool':([0,1,9,50,56,58,69,70,71,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'tupla':([0,1,9,50,56,58,69,70,71,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[42,42,54,54,54,54,42,54,54,54,54,54,54,114,42,54,54,54,54,54,54,42,54,42,42,54,42,42,42,42,54,42,42,54,42,42,42,54,54,54,42,42,42,42,54,54,]),'valores':([9,50,56,79,81,86,102,111,117,183,],[51,74,82,106,108,51,134,140,146,195,]),'operador':([12,77,112,],[58,58,141,]),'expresion':([58,141,],[85,164,]),'condicion':([70,99,122,],[96,131,152,]),'cuerpo_conjunto':([92,168,],[116,182,]),'conector':([96,131,152,],[122,122,122,]),'Comparador':([97,],[125,]),'caso':([157,227,],[171,230,]),'contador':([158,],[173,]),'else':([184,],[196,]),'cuerpo_Diccionario':([193,],[205,]),'duplas':([206,224,],[215,228,]),'dupla':([206,224,],[217,217,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> cuerpo','programa',1,'p_programa','main.py',20),
  ('programa -> programa cuerpo','programa',2,'p_programa','main.py',21),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','main.py',25),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','main.py',26),
  ('cuerpo -> operacion','cuerpo',1,'p_cuerpo','main.py',27),
  ('cuerpo -> comentario','cuerpo',1,'p_cuerpo','main.py',28),
  ('cuerpo -> estructuras_de_Control','cuerpo',1,'p_cuerpo','main.py',29),
  ('estructuras_de_Control -> sentencia_If','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',33),
  ('estructuras_de_Control -> sentencia_Switch','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',34),
  ('estructuras_de_Control -> ciclo_for','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',35),
  ('estructuras_de_Control -> funcion_Anonima','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',36),
  ('estructuras_de_Control -> diccionario','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',37),
  ('estructuras_de_Control -> Conjunto','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',38),
  ('estructuras_de_Control -> funcion_flecha','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',39),
  ('estructuras_de_Control -> funcion_Void','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',40),
  ('estructuras_de_Control -> funcion','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',41),
  ('estructuras_de_Control -> funcion_Data','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',42),
  ('estructuras_de_Control -> RETURN VARIABLE','estructuras_de_Control',2,'p_estructuras_de_Control','main.py',43),
  ('estructuras_de_Control -> estructura_List','estructuras_de_Control',1,'p_estructuras_de_Control','main.py',44),
  ('comentario -> COMMENTLINE','comentario',1,'p_comentario','main.py',47),
  ('comentario -> COMMENTBLOCK','comentario',1,'p_comentario','main.py',48),
  ('impresion -> PRINT LPAREN valores RPAREN DOTCOMMA','impresion',5,'p_impresion','main.py',52),
  ('impresion -> PRINT LPAREN operacion RPAREN DOTCOMMA','impresion',5,'p_impresion','main.py',53),
  ('impresion -> PRINT LPAREN RPAREN DOTCOMMA','impresion',4,'p_impresion','main.py',54),
  ('sentencia_If -> IF LPAREN condicion RPAREN LBRACE programa RBRACE else','sentencia_If',8,'p_sentencia_If','main.py',59),
  ('sentencia_If -> IF LPAREN condicion RPAREN LBRACE programa RBRACE','sentencia_If',7,'p_sentencia_If','main.py',60),
  ('else -> ELSE LBRACE programa RBRACE','else',4,'p_else','main.py',64),
  ('condicion -> valor Comparador valor','condicion',3,'p_condicion','main.py',68),
  ('condicion -> condicion conector condicion','condicion',3,'p_condicion','main.py',69),
  ('conector -> AND','conector',1,'p_conector','main.py',73),
  ('conector -> OR','conector',1,'p_conector','main.py',74),
  ('estructura_List -> LIST LANGLE tipo RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMA','estructura_List',10,'p_estructura_List','main.py',80),
  ('funcion_Void -> VOID VARIABLE LPAREN valores RPAREN LBRACE programa RBRACE DOTCOMMA','funcion_Void',9,'p_funcion_Void','main.py',84),
  ('Comparador -> EQUALS EQUALS','Comparador',2,'p_Comparador','main.py',87),
  ('Comparador -> LANGLE','Comparador',1,'p_Comparador','main.py',88),
  ('Comparador -> RANGLE','Comparador',1,'p_Comparador','main.py',89),
  ('Comparador -> LANGLE EQUALS','Comparador',2,'p_Comparador','main.py',90),
  ('Comparador -> RANGLE EQUALS','Comparador',2,'p_Comparador','main.py',91),
  ('Comparador -> NEQ','Comparador',1,'p_Comparador','main.py',92),
  ('tupla -> LPAREN valores RPAREN','tupla',3,'p_tupla','main.py',95),
  ('valores -> valor','valores',1,'p_valores','main.py',98),
  ('valores -> valor COMMA valores','valores',3,'p_valores','main.py',99),
  ('Bool -> TRUE','Bool',1,'p_Bool','main.py',106),
  ('Bool -> FALSE','Bool',1,'p_Bool','main.py',107),
  ('valor -> VARIABLE','valor',1,'p_valor','main.py',112),
  ('valor -> NUMBER','valor',1,'p_valor','main.py',113),
  ('valor -> FLOAT','valor',1,'p_valor','main.py',114),
  ('valor -> CHAINCHAR','valor',1,'p_valor','main.py',115),
  ('valor -> Bool','valor',1,'p_valor','main.py',116),
  ('valor -> tupla','valor',1,'p_valor','main.py',117),
  ('tipo -> MAP','tipo',1,'p_tipo','main.py',122),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','main.py',123),
  ('tipo -> STRING','tipo',1,'p_tipo','main.py',124),
  ('tipo -> INT','tipo',1,'p_tipo','main.py',125),
  ('tipo -> SET','tipo',1,'p_tipo','main.py',126),
  ('tipo -> LIST','tipo',1,'p_tipo','main.py',127),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','main.py',128),
  ('tipo -> FINAL','tipo',1,'p_tipo','main.py',129),
  ('tipo -> CONST','tipo',1,'p_tipo','main.py',130),
  ('tipo -> DYNAMIC','tipo',1,'p_tipo','main.py',131),
  ('declaracion -> tipo VARIABLE EQUALS valor DOTCOMMA','declaracion',5,'p_declaracion','main.py',139),
  ('declaracion -> VAR VARIABLE EQUALS valor DOTCOMMA','declaracion',5,'p_declaracion','main.py',140),
  ('operacion -> valor operador expresion','operacion',3,'p_operacion','main.py',152),
  ('expresion -> LPAREN valor operador expresion RPAREN','expresion',5,'p_expresion','main.py',165),
  ('expresion -> valor','expresion',1,'p_expresion','main.py',166),
  ('funcion -> VARIABLE LPAREN valores RPAREN','funcion',4,'p_funcion','main.py',178),
  ('funcion_Data -> VARIABLE DOT VARIABLE LPAREN valores RPAREN DOTCOMMA','funcion_Data',7,'p_funcion_Data','main.py',181),
  ('sentencia_Switch -> SWITCH LPAREN valor RPAREN LBRACE caso RBRACE','sentencia_Switch',7,'p_sentencia_Switch','main.py',185),
  ('caso -> CASE valor TWODOTS programa BREAK DOTCOMMA caso','caso',7,'p_caso','main.py',188),
  ('caso -> CASE valor TWODOTS programa BREAK DOTCOMMA','caso',6,'p_caso','main.py',189),
  ('funcion_flecha -> tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMA','funcion_flecha',8,'p_funcion_flecha_param','main.py',195),
  ('funcion_flecha -> tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMA','funcion_flecha',7,'p_funcion_flecha_no_param','main.py',203),
  ('Conjunto -> SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA','Conjunto',5,'p_Conjunto','main.py',209),
  ('Conjunto -> SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMA','Conjunto',8,'p_Conjunto','main.py',210),
  ('cuerpo_conjunto -> LBRACE valores RBRACE','cuerpo_conjunto',3,'p_cuerpo_conjunto','main.py',213),
  ('cuerpo_conjunto -> LBRACE RBRACE','cuerpo_conjunto',2,'p_cuerpo_conjunto','main.py',214),
  ('operador -> PLUS','operador',1,'p_operador','main.py',218),
  ('operador -> MINUS','operador',1,'p_operador','main.py',219),
  ('operador -> TIMES','operador',1,'p_operador','main.py',220),
  ('operador -> DIVIDE','operador',1,'p_operador','main.py',221),
  ('ciclo_for -> FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa RBRACE','ciclo_for',10,'p_ciclo_for','main.py',228),
  ('contador -> VARIABLE PLUS PLUS','contador',3,'p_contador','main.py',233),
  ('contador -> VARIABLE PLUS EQUALS valor','contador',4,'p_contador','main.py',234),
  ('contador -> VARIABLE MINUS MINUS','contador',3,'p_contador','main.py',235),
  ('contador -> VARIABLE MINUS EQUALS valor','contador',4,'p_contador','main.py',236),
  ('funcion_Anonima -> VAR VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA','funcion_Anonima',8,'p_funcion_Anonima','main.py',242),
  ('funcion_Anonima -> tupla LBRACE programa RBRACE DOTCOMMA','funcion_Anonima',5,'p_funcion_Anonima','main.py',243),
  ('diccionario -> MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA','diccionario',10,'p_diccionario','main.py',248),
  ('cuerpo_Diccionario -> LBRACE duplas RBRACE','cuerpo_Diccionario',3,'p_cuerpo_Diccionario','main.py',252),
  ('cuerpo_Diccionario -> LBRACE RBRACE','cuerpo_Diccionario',2,'p_cuerpo_Diccionario','main.py',253),
  ('duplas -> dupla','duplas',1,'p_duplas','main.py',256),
  ('duplas -> dupla COMMA duplas','duplas',3,'p_duplas','main.py',257),
  ('dupla -> valor TWODOTS valor','dupla',3,'p_dupla','main.py',261),
]
