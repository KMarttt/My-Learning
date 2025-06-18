import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class test {
    public static void main (String [] args) throws  IOException
    {
        System.out.println("= | == | == | == | == | == | == | == | == | =\n");
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");
        System.out.println("= | == | == | == | == | == | == | == | == | =\n");

        String num1, num2;
        int n1, n2, sum, difference, product , quotient;

        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(input);

        System.out.print("Enter first number (a): ");
        num1 = buffer.readLine();
        n1 = Integer.parseInt(num1);

        System.out.print("Enter second number (b): ");
        num2 = buffer.readLine();
        n2 = Integer.parseInt(num2);

        sum = n1 + n2;
        difference = n1 - n2;
        product = n1 * n2;
        quotient = n1/n2;

        System.out.println("\n{~~ | ^~^ | ~~  ~~ | ^~^ | ~~ ~~ | ^~^ | ~~ ~~ | ^~^ | ~~}\n");
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: "+ product);
        System.out.println("Quotient: "+ quotient);
        System.out.println("\n{~~ | ^~^ | ~~  ~~ | ^~^ | ~~ ~~ | ^~^ | ~~ ~~ | ^~^ | ~~}\n");







    }
}
