package learning;

public class Main {

    public static void main(String[] args) {
        // Main data types
        int helloWorld = 5; // Integer type
        char name = 'P'; // Character type
        float pi = 3.14f; // Float type
        double _pi = 3.14d; // Double type
        String name_ = "Pedro"; // String type

        System.out.println(pi);
        System.out.println(name);
        System.out.println(_pi);
        System.out.println(helloWorld);
        System.out.println(name_);


        // Declaring many variables in one line (same data type only)
        int a = 1, b = 2, c = 3;

        System.out.println(a + b + c);


        /* A floating point number can also be a scientific numbers with an 'e' to indicate
        the power of 10
         */
        float f1 = 35e3f;
        double d1 = 12E4d;

        System.out.println(f1);
        System.out.println(d1);


        // Type Casting
        int myInt = 9;
        myInt += 1;
        double myDouble = myInt; // automatically casting the type from a smaller size to a bigger size type

        System.out.println(myDouble);

        double myDouble2 = 9.29d;
        int myInt2 = (int) myDouble2; // changing a value from a bigger to a smaller type, the type must be placed in
        // parentheses

        System.out.println(myDouble2);


        // Operators
        /*
        Arithmetic Operators:
        + -> Addition
        - -> Subtraction
        * -> Multiplication
        / -> Division
        % -> Modulus
        ++ -> Increment
        -- -> Decrement
         */
        int x = 15;
        int y = 5;
        System.out.println(x + y);
        System.out.println(x - y);
        System.out.println(x * y);
        System.out.println(x / y);
        System.out.println(x % (y + 1));
        System.out.println(x++);
        System.out.println(x--);
        System.out.println(++x);
        System.out.println(--x);

        System.out.println("Assignment Operators");
        System.out.println(x);
        x = 5;
        System.out.println(x);
        x += 3;
        System.out.println(x);
        x -= 3;
        System.out.println(x);
        x *= 3;
        System.out.println(x);
        x /= 3;
        System.out.println(x);
        x %= 3;
        System.out.println(x);
        x &= 3;
        System.out.println(x);
        x |= 3;
        System.out.println(x);
        x ^= 3;
        System.out.println(x);
        x >>= 4;
        System.out.println(x);
        x <<= 3;
        System.out.println(x);


        /*
        Comparison Operators

        return a boolean value

        == -> Equals to
        != -> Not equal
        > -> Greater than
        < -> Less than
        >= -> Greater than or equal to
        <= -> Less than or equal to


        && -> Logical and
        || -> Logical or
        ! -> Logical not
         */

    }
}
