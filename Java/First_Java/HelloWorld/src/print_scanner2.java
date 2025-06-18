import java.util.Scanner;
import java.text.DecimalFormat;


public class print_scanner2 {
    public static void main (String [] args){
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year and Section: BCS11\n");

        Scanner SCAN = new Scanner(System.in);
        DecimalFormat DF = new DecimalFormat("0.0000");

        System.out.print("What is your name? ");
        String name = SCAN.nextLine();

        System.out.print("What is your age? ");
        int age = SCAN.nextInt();

        if (age >= 18){
            System.out.println("Name: " + name +": Legal!\n");
        } else {
            System.out.println("Name: " + name +":Minor :(");
        }

        System.out.println("Now let's try some calculation\n");

        System.out.print("Insert 1st number (a): ");
        double a = SCAN.nextDouble();

        System.out.print("Inset 2nd number (b): ");
        double b = SCAN.nextDouble();

        double sum = a + b;
        double difference = a - b;
        double product = a * b;
        double quotient = a / b;

        System.out.println("\nSum: "+DF.format(sum));
        System.out.println("Difference: "+ DF.format(difference));
        System.out.println("Product: "+ DF.format(product));
        System.out.println("Quotient: "+ DF.format(quotient));




    }

}
