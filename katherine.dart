void sumaYMensaje(int a, int b) {
  int suma = a + b;
  
  if (suma > 10) {
    print("La suma es mayor que 10: $suma");
  } else {
    print("La suma es igual o menor que 10: $suma");
  }
}

void main() {
  int num1 = 5;
  int num2 = 7;
  sumaYMensaje(num1, num2);
}