public class Runner {
    public static void main (String[] args)
    {
        Dynamic_stack_own nums = new Dynamic_stack_own();

        System.out.println("Stack is empty: " + nums.isEmpty());

        nums.push(15);
        nums.show();
        nums.push(8);
        nums.show();
        nums.push(10);
        nums.show();
        nums.push(10);
        nums.show();
        nums.push(10);
        nums.show();

        nums.pop();
        nums.show();
        nums.pop();
        nums.show();
        nums.pop();
        nums.show();
        nums.pop();
        nums.show();
    }
}
