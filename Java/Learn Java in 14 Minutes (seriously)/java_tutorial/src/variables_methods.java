import java.util.ArrayList;

public class variables_methods {
    public static void main (String[] args) {
        // whatever is in the main method, will run when hit play

        //This is a primitive type (built into java)
        int a = 5; // number variable
        char b = 'i'; // character variable
        long c = 400; //
        double d = 3.2; // decimal variable

        //Non-primitive type
        String name = "Susan"; // this is object (signified by the white color)
//        System.out.println(name.toUpperCase()); ; // to upercase
        System.out.println(name.toLowerCase()); // to lowercase

        // things with (), are 99% of the time are methods


        // to use the method that you made:
        addExclamationPoint("star light");

        // for your return method
        String exclaim = addExclamationPoint2("hot dogs");
        System.out.println(exclaim);

        // for your method in a class you made
        Animals_toBeImported animal = new Animals_toBeImported();
        // everytime you make an object, this is the format
        String dog = animal.iAmDog();
        // this is saved in a variable cause you used return in the method you made
        System.out.println(dog);


//        // Example of commonly used object
//        // hover over ArrayList in order to import it
//        ArrayList<Integer> a = new ArrayList<Integer>();
//        a.add()

//        // each object has its own methods (oop)
//        // each class represent an object which has its own method

    }

    // so to start a method:
    public static void addExclamationPoint (String s) { // s is the name of the string
    // this code will edit and print out the text
    // which is why system out

        System.out.println(s+"!");

    }


    public static String addExclamationPoint2 (String s) {
    // void is changed to String because this is a type of code
    // that returns something
            // so you can pretty much edit something and let it be stored in a variable
            // which is why it uses return

        return s + "!";

    }

    public static void doStuff() {
//       //if Statement
//
//        int a = 5;
//        if (a == 0) { // if (condition)
//            // then run this code
//        } else if (a == 1) {
//
//        } else {
//
//        }



//        // for loops
//        for (int i = 0; i <5; i++) {
//        // based on my understanding (int i = starting point; condition/end;
//        // increment of i (to avoid infinity)
//            // you can add for loops inside a for loop
//        // code here will be repeated 5 times
//        }



//        // while Loops: will work until the condition is not met
//        int a = 5;
//        while (a < 50) { // while (condition)
//            System.out.println("hi"); // will work if true
//            a++; // increment
//        }



//        try and catch
//
//        try {
//        //    if this is error
//        } catch (Exception e) {
//        //    then this line of code will run
//        }


        // API are long list of methods that are made from someone else
        // ex. Google, YouTube, Instagram, Twitter, etc.
        // to do this, go to someone's website and download jar file
    }
}
