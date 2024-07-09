void imprimirMensaje(String carrera) {
  if (carrera=="Computacion") {
    print("Es de la facultad de FIEC.");
  } else {
    print("No es de FIEC.");
  }
}

void main() {
  String carrera1 = "Computacion";
  String carrera2 = "Biologia";
  imprimirMensaje(carrera1); 
  imprimirMensaje(carrera2); 
}
