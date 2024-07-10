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