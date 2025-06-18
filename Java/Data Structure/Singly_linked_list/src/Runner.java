//will be our main method
import java.util.LinkedList;

public class Runner {
    public static void main (String[] args){
        /*This is the internal implementation of the Linked List it has its own methods*/

//        LinkedList list = new LinkedList();
//
//        list.add(5);
//        list.add(4, 12);

        LinkedList_own list = new LinkedList_own();
        list.insert(18);
        list.insert(45);
        list.insert(12);

        list.insertAtStart(25);
        list.insertAt(0, 55);

        list.deleteAt(3);

        list.show();


    }


}
