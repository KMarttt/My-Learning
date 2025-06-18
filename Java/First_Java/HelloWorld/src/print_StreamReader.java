import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class print_StreamReader {
    public static void main(String[] args) throws IOException
    {
        System.out.println("~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|\n");
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");
        System.out.println("~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|\n");

        InputStreamReader UserInput = new InputStreamReader(System.in);
        BufferedReader Buffer = new BufferedReader(UserInput);

        String str_n1, str_n2;
        int n1, n2, sum;

        System.out.print("Insert a number (a): ");
        //if there is a ln in the print, the user input will be placed in the next line
        str_n1 = Buffer.readLine();
        // this think will get an error if there is no IOThrowException
        n1 = Integer.parseInt(str_n1);

        System.out.print("Print a number(b): ");
        str_n2 = Buffer.readLine();
        n2 = Integer.parseInt(str_n2);

        sum = n1 + n2;

        System.out.print("Sum: " + sum);


    }
}
