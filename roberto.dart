/* Block comment example
This is a test for the block comment token.
*/

//comment line example
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
        print($instance);
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

    void impresion() {
        String message = "Hello, World!";
        print($message);
    }
}