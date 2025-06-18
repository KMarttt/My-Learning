public class RecursionTutorial {
    public static void main (String[] args){
        sayHi(3);
    }

    private static void sayHi(int count){
        System.out.println("Hi");

        if (count <= 1) {
            return;
//          will return to the preceding recursion that called it
//          and since it completed successfully, the call stack will remove that function
//          same with the previous recursions
        }
        sayHi( count - 1);
//        you have to have an exit condition to avoid recurion overflow
    }
}
