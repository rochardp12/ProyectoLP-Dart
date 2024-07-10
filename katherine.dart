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