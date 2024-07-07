
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ADMIRATION AND ARROWFUNCTION AS BOOLEAN BREAK CASE CATCH CHAINCHAR CLASS COMMA COMMENTBLOCK COMMENTLINE CONST DEF DEFAULT DIVIDE DOLLAR DOT DOTCOMMA DOUBLE DYNAMIC ELIF ELSE ENUM EQUALS EXTENDS FALSE FINAL FINALLY FLOAT FOR IF IN INT INTEGERDIVISION INTERFACE IS LANGLE LBRACE LBRACKET LIST LPAREN MAIN MAP METHOD MINUS MOD MODULE NEQ NEW NULL NUMBER OR PLUS PRINT PRIVATE PROTECTED PUBLIC RANGLE RBRACE RBRACKET RETURN RPAREN SET STATIC STRING SUPER SWITCH THIS TIMES TRUE TRY TWODOTS TYPEDEF VAR VARIABLE VOID WHILEprograma : cuerpo\n                | programa cuerpocuerpo : impresion\n              | declaracion\n              | operacion\n              | comentario\n              | estructuras_de_Control\n            estructuras_de_Control : sentencia_If\n                            | sentencia_Switch\n                            | ciclo_for\n                            | funcion_Anonima\n                            | diccionario\n                            | Conjunto\n                            | funcion_flecha\n                            | funcion_Void\n                            | funcion\n                            | funcion_Data\n                            | RETURN VARIABLE\n                            | estructura_List\n    comentario : COMMENTLINE\n                  | COMMENTBLOCKimpresion : PRINT LPAREN valores RPAREN DOTCOMMA\n                 | PRINT LPAREN operacion RPAREN DOTCOMMA\n                 | PRINT LPAREN RPAREN DOTCOMMA\n     sentencia_If : IF LPAREN condicion RPAREN LBRACE programa RBRACE else\n                        | IF LPAREN condicion RPAREN LBRACE programa RBRACE\n    \n    else : ELSE LBRACE programa RBRACE\n    \n    condicion : valor Comparador valor\n            |   condicion conector condicion\n    conector : AND\n                | OR\n    estructura_List : LIST LANGLE tipo RANGLE VARIABLE EQUALS LBRACKET valores RBRACKET DOTCOMMAfuncion_Void : VOID VARIABLE LPAREN valores RPAREN LBRACE programa RBRACE DOTCOMMAComparador : EQUALS EQUALS\n                    | LANGLE\n                    | RANGLE\n                    | LANGLE EQUALS\n                    | RANGLE EQUALS\n                    | NEQtupla : LPAREN valores RPARENvalores : valor\n               | valor COMMA valoresBool : TRUE\n        | FALSE \n    valor   : VARIABLE\n            | NUMBER\n            | FLOAT\n            | CHAINCHAR\n            | Bool\n            | operacion\n            | tupla\n    tipo : MAP\n            | DOUBLE\n            | STRING\n            | INT\n            | SET\n            | LIST\n            | BOOLEAN\n            | FINAL\n            | CONST\n            | DYNAMIC\n    \n    declaracion : tipo VARIABLE EQUALS valor DOTCOMMA\n                | VAR VARIABLE EQUALS valor DOTCOMMA\n    operacion : valor operador expresionexpresion : LPAREN valor operador expresion RPAREN\n                    | valor funcion : VARIABLE LPAREN valores RPARENfuncion_Data : VARIABLE DOT VARIABLE LPAREN valores RPAREN DOTCOMMAsentencia_Switch : SWITCH LPAREN valor RPAREN LBRACE caso RBRACEcaso : CASE valor TWODOTS programa BREAK DOTCOMMA caso \n            | CASE valor TWODOTS programa BREAK DOTCOMMA funcion_flecha : tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMAfuncion_flecha : tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMAConjunto : SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA\n                    | SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMAcuerpo_conjunto : LBRACE valores RBRACE\n                | LBRACE RBRACE operador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE \n    ciclo_for : FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa  RBRACE\n    contador : VARIABLE PLUS PLUS\n                | VARIABLE PLUS EQUALS valor\n                | VARIABLE MINUS MINUS\n                | VARIABLE MINUS EQUALS valor\n    funcion_Anonima : VAR VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA\n                    | tupla LBRACE programa RBRACE DOTCOMMA\n    diccionario : MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA\n    cuerpo_Diccionario : LBRACE duplas RBRACE\n                    | LBRACE RBRACE\n    duplas : dupla\n              | dupla COMMA duplas\n    dupla : valor TWODOTS valor\n    '
    
_lr_action_items = {'PRINT':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[8,8,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,8,-40,-66,-64,8,-24,-67,-22,-23,-62,8,-63,8,-74,-88,8,8,8,8,8,8,8,-73,-68,-65,-26,-69,8,-72,-87,-75,-25,8,8,8,8,8,-33,-89,-32,8,-82,-27,]),'VAR':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,73,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[13,13,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,13,101,-40,-66,-64,13,-24,-67,-22,-23,-62,13,-63,13,-74,-88,13,13,13,13,13,13,13,-73,-68,-65,-26,-69,13,-72,-87,-75,-25,13,13,13,13,13,-33,-89,-32,13,-82,-27,]),'COMMENTLINE':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[14,14,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,14,-40,-66,-64,14,-24,-67,-22,-23,-62,14,-63,14,-74,-88,14,14,14,14,14,14,14,-73,-68,-65,-26,-69,14,-72,-87,-75,-25,14,14,14,14,14,-33,-89,-32,14,-82,-27,]),'COMMENTBLOCK':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[15,15,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,15,-40,-66,-64,15,-24,-67,-22,-23,-62,15,-63,15,-74,-88,15,15,15,15,15,15,15,-73,-68,-65,-26,-69,15,-72,-87,-75,-25,15,15,15,15,15,-33,-89,-32,15,-82,-27,]),'RETURN':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[26,26,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,26,-40,-66,-64,26,-24,-67,-22,-23,-62,26,-63,26,-74,-88,26,26,26,26,26,26,26,-73,-68,-65,-26,-69,26,-72,-87,-75,-25,26,26,26,26,26,-33,-89,-32,26,-82,-27,]),'MAP':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[28,28,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,88,88,88,28,88,-40,-66,-64,28,-24,-67,88,-22,-23,-62,28,-63,28,-74,-88,28,28,28,28,28,28,28,-73,-68,-65,-26,-69,28,-72,-87,-75,-25,28,28,28,28,28,-33,-89,-32,28,-82,-27,]),'DOUBLE':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[29,29,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,29,29,29,29,29,-40,-66,-64,29,-24,-67,29,-22,-23,-62,29,-63,29,-74,-88,29,29,29,29,29,29,29,-73,-68,-65,-26,-69,29,-72,-87,-75,-25,29,29,29,29,29,-33,-89,-32,29,-82,-27,]),'STRING':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[30,30,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,30,30,30,30,30,-40,-66,-64,30,-24,-67,30,-22,-23,-62,30,-63,30,-74,-88,30,30,30,30,30,30,30,-73,-68,-65,-26,-69,30,-72,-87,-75,-25,30,30,30,30,30,-33,-89,-32,30,-82,-27,]),'INT':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[31,31,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,31,31,31,31,31,-40,-66,-64,31,-24,-67,31,-22,-23,-62,31,-63,31,-74,-88,31,31,31,31,31,31,31,-73,-68,-65,-26,-69,31,-72,-87,-75,-25,31,31,31,31,31,-33,-89,-32,31,-82,-27,]),'SET':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[32,32,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,90,90,90,32,90,-40,-66,-64,32,-24,-67,90,-22,-23,-62,32,-63,32,-74,-88,32,32,32,32,32,32,32,-73,-68,-65,-26,-69,32,-72,-87,-75,-25,32,32,32,32,32,-33,-89,-32,32,-82,-27,]),'LIST':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[33,33,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,91,91,91,33,91,-40,-66,-64,33,-24,-67,91,-22,-23,-62,33,-63,33,-74,-88,33,33,33,33,33,33,33,-73,-68,-65,-26,-69,33,-72,-87,-75,-25,33,33,33,33,33,-33,-89,-32,33,-82,-27,]),'BOOLEAN':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[34,34,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,34,34,34,34,34,-40,-66,-64,34,-24,-67,34,-22,-23,-62,34,-63,34,-74,-88,34,34,34,34,34,34,34,-73,-68,-65,-26,-69,34,-72,-87,-75,-25,34,34,34,34,34,-33,-89,-32,34,-82,-27,]),'FINAL':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[35,35,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,35,35,35,35,35,-40,-66,-64,35,-24,-67,35,-22,-23,-62,35,-63,35,-74,-88,35,35,35,35,35,35,35,-73,-68,-65,-26,-69,35,-72,-87,-75,-25,35,35,35,35,35,-33,-89,-32,35,-82,-27,]),'CONST':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[36,36,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,36,36,36,36,36,-40,-66,-64,36,-24,-67,36,-22,-23,-62,36,-63,36,-74,-88,36,36,36,36,36,36,36,-73,-68,-65,-26,-69,36,-72,-87,-75,-25,36,36,36,36,36,-33,-89,-32,36,-82,-27,]),'DYNAMIC':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,66,68,69,70,73,78,84,85,95,104,110,115,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[37,37,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,37,37,37,37,37,-40,-66,-64,37,-24,-67,37,-22,-23,-62,37,-63,37,-74,-88,37,37,37,37,37,37,37,-73,-68,-65,-26,-69,37,-72,-87,-75,-25,37,37,37,37,37,-33,-89,-32,37,-82,-27,]),'VARIABLE':([0,1,2,3,4,5,6,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,47,48,49,50,53,54,55,57,58,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,88,90,91,95,99,100,101,102,104,110,111,117,118,119,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,158,159,161,162,165,166,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[11,11,-1,-3,-4,-5,-6,-7,53,56,64,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,65,-19,-52,-53,-54,-55,67,-57,-58,-59,-60,-61,-46,-47,-48,-49,74,-43,-44,-2,53,-45,-50,-51,53,83,53,-78,-79,-80,-81,-18,11,53,53,-40,53,53,53,-66,-64,53,53,-52,-56,-57,11,53,132,133,53,-24,-67,53,53,148,149,53,-30,-31,53,-35,-36,-39,-22,-23,-62,11,53,-63,11,-74,-88,11,-34,-37,-38,174,53,11,11,11,181,11,53,11,11,-73,-68,-65,53,-26,-69,11,-72,-87,-75,-25,11,11,53,53,53,11,11,11,-33,-89,-32,11,-82,53,53,-27,]),'NUMBER':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,55,57,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[38,38,-1,-3,-4,-5,-6,-7,38,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,38,-45,-50,-51,38,38,-78,-79,-80,-81,-18,38,38,38,-40,38,38,38,-66,-64,38,38,38,38,38,-24,-67,38,38,38,-30,-31,38,-35,-36,-39,-22,-23,-62,38,38,-63,38,-74,-88,38,-34,-37,-38,38,38,38,38,38,38,38,38,-73,-68,-65,38,-26,-69,38,-72,-87,-75,-25,38,38,38,38,38,38,38,38,-33,-89,-32,38,-82,38,38,-27,]),'FLOAT':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,55,57,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[39,39,-1,-3,-4,-5,-6,-7,39,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,39,-45,-50,-51,39,39,-78,-79,-80,-81,-18,39,39,39,-40,39,39,39,-66,-64,39,39,39,39,39,-24,-67,39,39,39,-30,-31,39,-35,-36,-39,-22,-23,-62,39,39,-63,39,-74,-88,39,-34,-37,-38,39,39,39,39,39,39,39,39,-73,-68,-65,39,-26,-69,39,-72,-87,-75,-25,39,39,39,39,39,39,39,39,-33,-89,-32,39,-82,39,39,-27,]),'CHAINCHAR':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,55,57,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[40,40,-1,-3,-4,-5,-6,-7,40,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,40,-45,-50,-51,40,40,-78,-79,-80,-81,-18,40,40,40,-40,40,40,40,-66,-64,40,40,40,40,40,-24,-67,40,40,40,-30,-31,40,-35,-36,-39,-22,-23,-62,40,40,-63,40,-74,-88,40,-34,-37,-38,40,40,40,40,40,40,40,40,-73,-68,-65,40,-26,-69,40,-72,-87,-75,-25,40,40,40,40,40,40,40,40,-33,-89,-32,40,-82,40,40,-27,]),'IF':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[43,43,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,43,-40,-66,-64,43,-24,-67,-22,-23,-62,43,-63,43,-74,-88,43,43,43,43,43,43,43,-73,-68,-65,-26,-69,43,-72,-87,-75,-25,43,43,43,43,43,-33,-89,-32,43,-82,-27,]),'SWITCH':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[44,44,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,44,-40,-66,-64,44,-24,-67,-22,-23,-62,44,-63,44,-74,-88,44,44,44,44,44,44,44,-73,-68,-65,-26,-69,44,-72,-87,-75,-25,44,44,44,44,44,-33,-89,-32,44,-82,-27,]),'FOR':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[45,45,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,45,-40,-66,-64,45,-24,-67,-22,-23,-62,45,-63,45,-74,-88,45,45,45,45,45,45,45,-73,-68,-65,-26,-69,45,-72,-87,-75,-25,45,45,45,45,45,-33,-89,-32,45,-82,-27,]),'VOID':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,70,78,84,85,95,104,110,135,136,137,139,142,143,145,150,151,161,162,165,170,175,176,177,178,179,184,185,190,191,192,194,196,198,199,208,209,210,213,214,219,220,222,226,],[46,46,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,46,-40,-66,-64,46,-24,-67,-22,-23,-62,46,-63,46,-74,-88,46,46,46,46,46,46,46,-73,-68,-65,-26,-69,46,-72,-87,-75,-25,46,46,46,46,46,-33,-89,-32,46,-82,-27,]),'TRUE':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,55,57,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[47,47,-1,-3,-4,-5,-6,-7,47,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,47,-45,-50,-51,47,47,-78,-79,-80,-81,-18,47,47,47,-40,47,47,47,-66,-64,47,47,47,47,47,-24,-67,47,47,47,-30,-31,47,-35,-36,-39,-22,-23,-62,47,47,-63,47,-74,-88,47,-34,-37,-38,47,47,47,47,47,47,47,47,-73,-68,-65,47,-26,-69,47,-72,-87,-75,-25,47,47,47,47,47,47,47,47,-33,-89,-32,47,-82,47,47,-27,]),'FALSE':([0,1,2,3,4,5,6,7,9,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,50,53,54,55,57,59,60,61,62,63,65,70,71,72,78,79,80,81,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[48,48,-1,-3,-4,-5,-6,-7,48,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,48,-45,-50,-51,48,48,-78,-79,-80,-81,-18,48,48,48,-40,48,48,48,-66,-64,48,48,48,48,48,-24,-67,48,48,48,-30,-31,48,-35,-36,-39,-22,-23,-62,48,48,-63,48,-74,-88,48,-34,-37,-38,48,48,48,48,48,48,48,48,-73,-68,-65,48,-26,-69,48,-72,-87,-75,-25,48,48,48,48,48,48,48,48,-33,-89,-32,48,-82,48,48,-27,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,11,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,43,44,45,47,48,49,50,53,54,55,56,57,59,60,61,62,63,65,70,71,72,74,78,79,80,81,83,84,85,86,87,95,99,102,104,110,111,117,122,123,124,125,127,128,129,135,136,137,139,141,142,143,145,150,151,154,155,156,159,161,162,165,170,172,175,176,177,178,179,183,184,185,190,191,192,194,196,198,199,201,203,206,208,209,210,213,214,219,220,222,224,225,226,],[9,9,-1,-3,-4,-5,-6,-7,50,9,57,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,71,72,73,-43,-44,-2,9,-45,-50,-51,81,9,86,-78,-79,-80,-81,-18,9,9,9,102,-40,9,9,9,111,-66,-64,9,9,9,9,9,-24,-67,9,9,9,-30,-31,9,-35,-36,-39,-22,-23,-62,9,86,-63,9,-74,-88,9,-34,-37,-38,9,9,9,9,9,9,9,9,-73,-68,-65,9,-26,-69,9,-72,-87,-75,-25,9,9,9,9,9,9,9,9,-33,-89,-32,9,-82,9,9,-27,]),'$end':([1,2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,78,84,85,104,110,135,136,137,142,145,150,177,178,179,184,185,191,192,194,196,213,214,219,222,226,],[0,-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,-40,-66,-64,-24,-67,-22,-23,-62,-63,-74,-88,-73,-68,-65,-26,-69,-72,-87,-75,-25,-33,-89,-32,-82,-27,]),'RBRACE':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,52,53,54,55,65,78,84,85,95,104,106,110,117,135,136,137,142,145,146,150,165,170,171,177,178,179,184,185,190,191,192,194,196,206,210,213,214,215,217,219,220,222,226,227,228,229,230,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-41,-45,-50,-51,-18,-40,-66,-64,120,-24,-42,-67,147,-22,-23,-62,-63,-74,167,-88,180,184,185,-73,-68,-65,-26,-69,204,-72,-87,-75,-25,216,222,-33,-89,223,-92,-32,226,-82,-27,-71,-93,-94,-70,]),'DOTCOMMA':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,76,78,84,85,103,104,105,107,110,113,114,116,120,131,135,136,137,142,145,147,150,152,153,162,163,167,176,177,178,179,180,182,184,185,191,192,194,196,204,205,207,213,214,216,219,221,222,223,226,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,104,-40,-66,-64,135,-24,136,137,-67,142,-51,145,150,158,-22,-23,-62,-63,-74,-77,-88,-29,-28,177,178,-76,191,-73,-68,-65,192,194,-26,-69,-72,-87,-75,-25,213,214,219,-33,-89,-91,-32,227,-82,-90,-27,]),'BREAK':([2,3,4,5,6,7,14,15,16,17,18,19,20,21,22,23,24,25,27,38,39,40,41,47,48,49,53,54,55,65,78,84,85,104,110,135,136,137,142,145,150,177,178,179,184,185,191,192,194,196,209,213,214,219,222,226,],[-1,-3,-4,-5,-6,-7,-20,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-46,-47,-48,-49,-43,-44,-2,-45,-50,-51,-18,-40,-66,-64,-24,-67,-22,-23,-62,-63,-74,-88,-73,-68,-65,-26,-69,-72,-87,-75,-25,221,-33,-89,-32,-82,-27,]),'PLUS':([5,11,12,38,39,40,41,42,47,48,52,53,54,55,77,78,84,85,97,98,107,112,113,114,153,164,174,179,186,188,211,212,218,229,],[-50,-45,60,-46,-47,-48,-49,-51,-43,-44,60,-45,-50,-51,-50,-40,60,-64,60,60,60,60,60,-51,60,-64,188,-65,60,200,60,60,60,60,]),'MINUS':([5,11,12,38,39,40,41,42,47,48,52,53,54,55,77,78,84,85,97,98,107,112,113,114,153,164,174,179,186,189,211,212,218,229,],[-50,-45,61,-46,-47,-48,-49,-51,-43,-44,61,-45,-50,-51,-50,-40,61,-64,61,61,61,61,61,-51,61,-64,189,-65,61,202,61,61,61,61,]),'TIMES':([5,11,12,38,39,40,41,42,47,48,52,53,54,55,77,78,84,85,97,98,107,112,113,114,153,164,179,186,211,212,218,229,],[-50,-45,62,-46,-47,-48,-49,-51,-43,-44,62,-45,-50,-51,-50,-40,62,-64,62,62,62,62,62,-51,62,-64,-65,62,62,62,62,62,]),'DIVIDE':([5,11,12,38,39,40,41,42,47,48,52,53,54,55,77,78,84,85,97,98,107,112,113,114,153,164,179,186,211,212,218,229,],[-50,-45,63,-46,-47,-48,-49,-51,-43,-44,63,-45,-50,-51,-50,-40,63,-64,63,63,63,63,63,-51,63,-64,-65,63,63,63,63,63,]),'DOT':([11,],[58,]),'LANGLE':([28,32,33,38,39,40,41,47,48,53,54,55,78,84,85,97,179,],[66,68,69,-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,127,-65,]),'COMMA':([29,30,31,34,35,36,37,38,39,40,41,47,48,52,53,54,55,77,78,84,85,88,89,90,91,112,164,179,217,229,],[-53,-54,-55,-58,-59,-60,-61,-46,-47,-48,-49,-43,-44,79,-45,-50,-51,-50,-40,-66,-64,-52,115,-56,-57,79,-64,-65,224,-94,]),'RANGLE':([29,30,31,34,35,36,37,38,39,40,41,47,48,53,54,55,78,84,85,88,90,91,93,94,97,144,179,],[-53,-54,-55,-58,-59,-60,-61,-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,-52,-56,-57,118,119,128,166,-65,]),'RPAREN':([38,39,40,41,47,48,50,51,52,53,54,55,75,77,78,81,82,84,85,96,98,106,108,112,134,140,152,153,164,173,179,200,202,211,212,],[-46,-47,-48,-49,-43,-44,76,78,-41,-45,-50,-51,103,105,-40,109,110,-66,-64,121,130,-42,138,-41,160,163,-29,-28,179,187,-65,-83,-85,-84,-86,]),'EQUALS':([38,39,40,41,47,48,53,54,55,56,64,67,78,84,85,97,126,127,128,132,133,148,149,179,181,188,189,],[-46,-47,-48,-49,-43,-44,-45,-50,-51,80,87,92,-40,-66,-64,126,154,155,156,80,159,168,169,-65,193,201,203,]),'NEQ':([38,39,40,41,47,48,53,54,55,78,84,85,97,179,],[-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,129,-65,]),'RBRACKET':([38,39,40,41,47,48,52,53,54,55,78,84,85,106,179,195,],[-46,-47,-48,-49,-43,-44,-41,-45,-50,-51,-40,-66,-64,-42,-65,207,]),'AND':([38,39,40,41,47,48,53,54,55,78,84,85,96,131,152,153,179,],[-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,123,123,123,-28,-65,]),'OR':([38,39,40,41,47,48,53,54,55,78,84,85,96,131,152,153,179,],[-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,124,124,124,-28,-65,]),'TWODOTS':([38,39,40,41,47,48,53,54,55,78,84,85,179,186,218,],[-46,-47,-48,-49,-43,-44,-45,-50,-51,-40,-66,-64,-65,198,225,]),'LBRACE':([42,78,92,114,121,130,160,168,187,193,197,],[70,-40,117,143,151,157,175,117,199,206,208,]),'ARROWFUNCTION':([109,138,],[139,161,]),'CASE':([157,227,],[172,172,]),'LBRACKET':([169,],[183,]),'ELSE':([184,],[197,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,70,139,143,151,161,175,198,199,208,],[1,95,162,165,170,176,190,209,210,220,]),'cuerpo':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[2,49,2,49,2,2,2,2,49,49,49,2,49,49,2,2,2,49,49,49,]),'impresion':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'declaracion':([0,1,70,73,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[4,4,4,99,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'operacion':([0,1,9,50,57,59,70,71,72,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[5,5,54,77,54,54,5,54,54,54,54,54,54,54,5,54,54,54,54,54,54,5,54,5,5,54,5,5,5,5,54,5,5,54,5,5,5,54,54,54,5,5,5,5,54,54,]),'comentario':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'estructuras_de_Control':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'tipo':([0,1,66,68,69,70,73,95,115,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[10,10,89,93,94,10,100,10,144,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'valor':([0,1,9,50,57,59,70,71,72,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[12,12,52,52,52,84,12,97,98,52,107,52,112,113,12,97,52,52,52,97,153,12,84,12,12,113,12,12,12,12,186,12,12,52,12,12,12,211,212,218,12,12,12,12,218,229,]),'sentencia_If':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'sentencia_Switch':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ciclo_for':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'funcion_Anonima':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'diccionario':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Conjunto':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'funcion_flecha':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'funcion_Void':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'funcion':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'funcion_Data':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'estructura_List':([0,1,70,95,139,143,151,161,162,165,170,175,176,190,198,199,208,209,210,220,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'Bool':([0,1,9,50,57,59,70,71,72,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'tupla':([0,1,9,50,57,59,70,71,72,79,80,81,86,87,95,99,102,111,117,122,125,139,141,143,151,159,161,162,165,170,172,175,176,183,190,198,199,201,203,206,208,209,210,220,224,225,],[42,42,55,55,55,55,42,55,55,55,55,55,55,114,42,55,55,55,55,55,55,42,55,42,42,55,42,42,42,42,55,42,42,55,42,42,42,55,55,55,42,42,42,42,55,55,]),'valores':([9,50,57,79,81,86,102,111,117,183,],[51,75,82,106,108,51,134,140,146,195,]),'operador':([12,52,84,97,98,107,112,113,153,186,211,212,218,229,],[59,59,59,59,59,59,141,59,59,59,59,59,59,59,]),'expresion':([59,141,],[85,164,]),'condicion':([71,99,122,],[96,131,152,]),'cuerpo_conjunto':([92,168,],[116,182,]),'conector':([96,131,152,],[122,122,122,]),'Comparador':([97,],[125,]),'caso':([157,227,],[171,230,]),'contador':([158,],[173,]),'else':([184,],[196,]),'cuerpo_Diccionario':([193,],[205,]),'duplas':([206,224,],[215,228,]),'dupla':([206,224,],[217,217,]),}

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
  ('valor -> operacion','valor',1,'p_valor','main.py',117),
  ('valor -> tupla','valor',1,'p_valor','main.py',118),
  ('tipo -> MAP','tipo',1,'p_tipo','main.py',123),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','main.py',124),
  ('tipo -> STRING','tipo',1,'p_tipo','main.py',125),
  ('tipo -> INT','tipo',1,'p_tipo','main.py',126),
  ('tipo -> SET','tipo',1,'p_tipo','main.py',127),
  ('tipo -> LIST','tipo',1,'p_tipo','main.py',128),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','main.py',129),
  ('tipo -> FINAL','tipo',1,'p_tipo','main.py',130),
  ('tipo -> CONST','tipo',1,'p_tipo','main.py',131),
  ('tipo -> DYNAMIC','tipo',1,'p_tipo','main.py',132),
  ('declaracion -> tipo VARIABLE EQUALS valor DOTCOMMA','declaracion',5,'p_declaracion','main.py',140),
  ('declaracion -> VAR VARIABLE EQUALS valor DOTCOMMA','declaracion',5,'p_declaracion','main.py',141),
  ('operacion -> valor operador expresion','operacion',3,'p_operacion','main.py',145),
  ('expresion -> LPAREN valor operador expresion RPAREN','expresion',5,'p_expresion','main.py',148),
  ('expresion -> valor','expresion',1,'p_expresion','main.py',149),
  ('funcion -> VARIABLE LPAREN valores RPAREN','funcion',4,'p_funcion','main.py',152),
  ('funcion_Data -> VARIABLE DOT VARIABLE LPAREN valores RPAREN DOTCOMMA','funcion_Data',7,'p_funcion_Data','main.py',155),
  ('sentencia_Switch -> SWITCH LPAREN valor RPAREN LBRACE caso RBRACE','sentencia_Switch',7,'p_sentencia_Switch','main.py',159),
  ('caso -> CASE valor TWODOTS programa BREAK DOTCOMMA caso','caso',7,'p_caso','main.py',162),
  ('caso -> CASE valor TWODOTS programa BREAK DOTCOMMA','caso',6,'p_caso','main.py',163),
  ('funcion_flecha -> tipo VARIABLE LPAREN valores RPAREN ARROWFUNCTION programa DOTCOMMA','funcion_flecha',8,'p_funcion_flecha_param','main.py',169),
  ('funcion_flecha -> tipo VARIABLE LPAREN RPAREN ARROWFUNCTION programa DOTCOMMA','funcion_flecha',7,'p_funcion_flecha_no_param','main.py',177),
  ('Conjunto -> SET VARIABLE EQUALS cuerpo_conjunto DOTCOMMA','Conjunto',5,'p_Conjunto','main.py',183),
  ('Conjunto -> SET LANGLE tipo RANGLE VARIABLE EQUALS cuerpo_conjunto DOTCOMMA','Conjunto',8,'p_Conjunto','main.py',184),
  ('cuerpo_conjunto -> LBRACE valores RBRACE','cuerpo_conjunto',3,'p_cuerpo_conjunto','main.py',187),
  ('cuerpo_conjunto -> LBRACE RBRACE','cuerpo_conjunto',2,'p_cuerpo_conjunto','main.py',188),
  ('operador -> PLUS','operador',1,'p_operador','main.py',192),
  ('operador -> MINUS','operador',1,'p_operador','main.py',193),
  ('operador -> TIMES','operador',1,'p_operador','main.py',194),
  ('operador -> DIVIDE','operador',1,'p_operador','main.py',195),
  ('ciclo_for -> FOR LPAREN declaracion condicion DOTCOMMA contador RPAREN LBRACE programa RBRACE','ciclo_for',10,'p_ciclo_for','main.py',202),
  ('contador -> VARIABLE PLUS PLUS','contador',3,'p_contador','main.py',207),
  ('contador -> VARIABLE PLUS EQUALS valor','contador',4,'p_contador','main.py',208),
  ('contador -> VARIABLE MINUS MINUS','contador',3,'p_contador','main.py',209),
  ('contador -> VARIABLE MINUS EQUALS valor','contador',4,'p_contador','main.py',210),
  ('funcion_Anonima -> VAR VARIABLE EQUALS tupla LBRACE programa RBRACE DOTCOMMA','funcion_Anonima',8,'p_funcion_Anonima','main.py',216),
  ('funcion_Anonima -> tupla LBRACE programa RBRACE DOTCOMMA','funcion_Anonima',5,'p_funcion_Anonima','main.py',217),
  ('diccionario -> MAP LANGLE tipo COMMA tipo RANGLE VARIABLE EQUALS cuerpo_Diccionario DOTCOMMA','diccionario',10,'p_diccionario','main.py',222),
  ('cuerpo_Diccionario -> LBRACE duplas RBRACE','cuerpo_Diccionario',3,'p_cuerpo_Diccionario','main.py',226),
  ('cuerpo_Diccionario -> LBRACE RBRACE','cuerpo_Diccionario',2,'p_cuerpo_Diccionario','main.py',227),
  ('duplas -> dupla','duplas',1,'p_duplas','main.py',230),
  ('duplas -> dupla COMMA duplas','duplas',3,'p_duplas','main.py',231),
  ('dupla -> valor TWODOTS valor','dupla',3,'p_dupla','main.py',235),
]
