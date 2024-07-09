/* Block comment example
This is a test for the block comment token.
*/

// Line comment example
public class TestClass {
    private int number = 42;
    public double decimalNumber = 3.14;
    protected isValid = True;
    static final String CONSTANT_STRING = "Hello";
    private List<Integer> myList = new ArrayList<>();
    private Map<String, Integer> myMap = new HashMap<>();

    public static void main(String[] args) {
        TestClass instance = new TestClass();
        instance.testMethod();
    }

    public void testMethod() {
        int localVar = 10;
        double pi = 3.14;
        eanean flag = False;
        String greeting = "Hello, World!";
        char initial = 'A';
        
        if (localVar > 5 && flag == False) {
            print("localVar is greater than 5");
        } else {
            print("localVar is less than or equal to 5");
        }

        for (int i = 0; i < 10; i++) {
            myList.add(i);
        }

        while (localVar > 0) {
            localVar--;
        }

        switch (localVar) {
            case 0:
                print("localVar is zero");
                break;
            default:
                print("localVar is not zero");
                break;
        }

        try {
            int result = localVar / 0;
        } catch (ArithmeticException e) {
            print("Division by zero!");
        } finally {
            print("End of try-catch block");
        }

        number = (int) pi; // Casting
        myMap.put("Key", 123);

        // Check reserved words
        nullCheck(null);
        thisCheck(this);
        superCheck(super.toString());

        print(greeting + " " + initial + '!');
    }

    private void nullCheck(Object obj) {
        if (obj == null) {
            print("Object is null");
        }
    }

    private void thisCheck(TestClass obj) {
        if (obj == this) {
            print("This object");
        }
    }

    private void superCheck(String str) {
        if (str != null) {
            print("Super check passed");
        }
    }

    private void print(String message) {
        System.out.println(message);
    }
}