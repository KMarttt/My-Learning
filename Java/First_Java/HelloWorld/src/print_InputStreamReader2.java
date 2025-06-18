import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.text.DecimalFormat;

public class print_InputStreamReader2 {
    public static void main (String [] args) throws IOException {
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");

        InputStreamReader INPUT = new InputStreamReader(System.in);
        BufferedReader BUFFER = new BufferedReader(INPUT);
        DecimalFormat DF = new DecimalFormat("0.0000");

        System.out.print("What's your name? ");
        String name = BUFFER.readLine();

        System.out.print("How old are you? ");
        String age_str = BUFFER.readLine();
        int age_int = Integer.parseInt(age_str);
        System.out.println("...");

        if (age_int >= 18) {
            System.out.println("Okay, " + name + ", your legal for our services!\n");
        } else {
            System.out.print("Minor :(\n");
        }

        System.out.println("Now, let's do some calculation\n");

        System.out.print("Insert first number (a): ");
        String num1 = BUFFER.readLine();
        double n1 = Double.parseDouble(num1);

        System.out.print("Insert second number (b): ");
        String num2 = BUFFER.readLine();
        double n2 = Double.parseDouble(num2);

        double sum = n1 + n2;
        double difference = n1 - n2;
        double product = n1 * n2;
        double quotient = n1 / n2;


        System.out.println("...\n");
        System.out.println("Sum: " + DF.format(sum));
        System.out.println("Difference: "+ DF.format(difference));
        System.out.println("Product: "+ DF.format(product));
        System.out.println("Quotient: "+ DF.format(quotient));

    }
}
