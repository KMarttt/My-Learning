import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class experiment {
    public static void main (String[] args) throws IOException
    {
        System.out.println("= | = = | == | == | == | == | == | == | =\n");
        System.out.println("Name: Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");
        System.out.println("= | = = | == | == | == | == | == | == | =\n");

        String name, sure, lowered_sure, age;
        boolean naming;

        InputStreamReader INPUT = new InputStreamReader(System.in);
        BufferedReader BUFFER = new BufferedReader(INPUT);

        naming = true;

        while (naming = true){
            System.out.print("What is your name? ");
            name = BUFFER.readLine();

            System.out.println("So your name is "+ name + " , am I correct?\n");

            System.out.print("Are you sure? ");
            sure = BUFFER.readLine();
            lowered_sure = sure.toLowerCase();
            System.out.print(" ");

            if (lowered_sure == "yes") {
                System.out.println("Okay, got it.\nI won't doubt you anymore");
                naming = false;
            }
        }




        System.out.println("Okay, got it.\nI won't doubt you anymore");

        System.out.println("So moving on, what is your age?\n You know just to be sure, we want to keep FBI away.");









    }
}
