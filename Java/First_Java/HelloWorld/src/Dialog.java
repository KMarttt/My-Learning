import javax.swing.JOptionPane;
import javax.swing.JDialog;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;

public class Dialog {
    public static void main (String [] args){
        System.out.println("Marti Kier V. Trance");
        System.out.println("Year & Section: BCS11\n");

        JOptionPane pane = new JOptionPane(System.in);
        JDialog.setDefaultLookAndFeelDecorated(true);
        JOptionPane.showMessageDialog(null, "Hi", "Greetings", JOptionPane.PLAIN_MESSAGE);
        JOptionPane.showMessageDialog(null, "Hello!", "Greetings", JOptionPane.WARNING_MESSAGE);
        JOptionPane.showMessageDialog(null, "Yo!!", "Greetings", JOptionPane.ERROR_MESSAGE);
        JOptionPane.showMessageDialog(null, "Sup.", "Greetings", JOptionPane.INFORMATION_MESSAGE);
        JOptionPane.showMessageDialog(null, "Pre?", "Greetings", JOptionPane.QUESTION_MESSAGE);

        String name_str = JOptionPane.showInputDialog(null, "What is your name? ", "Name", JOptionPane.QUESTION_MESSAGE);
        String age_str = JOptionPane.showInputDialog(null, "What is your age?", "Age", JOptionPane.QUESTION_MESSAGE);
        int age = Integer.parseInt(age_str);

        if (age >= 18){
            JOptionPane.showMessageDialog(null, ("Name: " + name_str + " --> LEGAL!"), "Status", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, ("Name: "+ name_str + " --> MINOR :("), "Status", JOptionPane.INFORMATION_MESSAGE);
        }


        JOptionPane.showMessageDialog(null,"Lets do some calculation!", "Calculation", JOptionPane.INFORMATION_MESSAGE);

        String a_str = JOptionPane.showInputDialog(null, "Insert 1st number (a): ", "a", JOptionPane.QUESTION_MESSAGE);
        int a_int = Integer.parseInt(a_str);

        String b_str = JOptionPane.showInputDialog(null, "Insert 2nd number (b): ", "b", JOptionPane.QUESTION_MESSAGE);
        int b_int = Integer.parseInt(b_str);

        int sum = a_int + b_int;
        int difference = a_int - b_int;
        int product = a_int * b_int;
        int quotient = a_int / b_int;

        JTextArea TEXTAREA = new JTextArea(5, 10);
        JScrollPane SCROLL = new JScrollPane(TEXTAREA);

        TEXTAREA.append("Really long word, like looooooooong word, suppppper loooong");
        TEXTAREA.append("\nSum: " + sum);
        TEXTAREA.append("\nDifference: " + difference);
        TEXTAREA.append("\nProduct: " + product);
        TEXTAREA.append("\nQuotient: "+ quotient);
        TEXTAREA.append("\na");
        TEXTAREA.append("\nb");
        TEXTAREA.append("\nc");

        JOptionPane.showMessageDialog(null, SCROLL);




    }
}
