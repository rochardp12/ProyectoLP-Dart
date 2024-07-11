void Pais() {
  String nombre = "Ecuador";
  boolean ganoMundial = True;
  int cantidad = 3



  String cantidadMundiales() => print($cantidad);;
}


void main() {

  Set<tuple> paises = {
    ('Brasil', True, 5),
    ('Argentina', True, 3),
    ('España', True, 1),
    ('Italia', True, 4),
    ('México', False, 0),
    ('Japón', False, 0)
  };
  for (int i = 0; $i < $cantidad; $i++) {
    String pais = "Argentina";
    switch ($pais) {
      case True:
        print('GANÓ: ', $pais);
        break;
      case False:
        print('NO GANÓ:',  $pais);
        break;
    }
  }
}