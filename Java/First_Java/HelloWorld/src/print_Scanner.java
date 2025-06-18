import java.util.Scanner;
import java.text.DecimalFormat;
// text for decimal format cuz it formats texts??

public class print_Scanner {
    public static void main (String [] args)
    {
        System.out.println("~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|\n");
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");
        System.out.println("~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|");

        Scanner Scan = new Scanner(System.in);
        DecimalFormat DF = new DecimalFormat("0.00");
        // you need to string the pattern (0.00)
        double num1, num2, sum;


        System.out.print("Enter a number (a): ");
        num1 = Scan.nextDouble();

        System.out.print("Enter a number (b): ");
        num2 = Scan.nextDouble();

        sum = num1 + num2;

        System.out.println("Sum: " + DF.format(sum));
    }
}
