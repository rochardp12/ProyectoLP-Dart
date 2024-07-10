/* Block comment example
This is a test for the block comment token.
*/

// Line comment example
void main {
    int number = 42;
    double decimalNumber = 3.14;
    boolean isValid = True;
    String CONSTANT_STRING = "Hello";
    List<int> myList = [1,3,2];
    map<String, int> myMap = {"hola": 1, "adios": 2};

    void main() {
        var instance = "Hello, World!";
        instance.testMethod();
    }

    void testMethod() {
        int localVar = 10;
        double pi = 3.14;
        boolean flag = false;
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

    void nullCheck($obj) {
        if (obj == obj) {
            print("var is obj");
        }
    }

    void thisCheck($obj) {
        if (obj == obj) {
            print("This object");
        }
    }

    void print($message) {
        print(message);
    }
}