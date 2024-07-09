class Pais {
  String nombre;
  bool ganoMundial;
  int cantidad;

  Pais(this.nombre, this.ganoMundial, this.cantidad);

  public String cantidadMundiales() => print(this.cantidad)
}


void main() {
  // Crear un conjunto de países
  Set<Pais> paises = {
    Pais('Brasil', true, 5),
    Pais('Argentina', true, 3),
    Pais('España', true, 1),
    Pais('Italia', true, 4),
    Pais('México', false, 0),
    Pais('Japón', false, 0),
  };

  // Recorrer el conjunto de países y aplicar el switch en ganoMundial
  for (Pais pais in paises) {
    switch (pais.ganoMundial) {
      case true:
        print('GANÓ:  ${pais.nombre}');
        pais.cantidadMundiales();
        break;
      case false:
        print('NO GANÓ:  ${pais.nombre}');
        break;
      case default:
        print('Sin Informacion');
    }
  }
}

