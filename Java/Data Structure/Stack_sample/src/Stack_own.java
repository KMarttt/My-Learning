public class Stack_own
{
    int stack[] =new int[5];
//  for this example we will be using only 5 size
//  you can make its size according to user input if you want
    int top = 0;
    public void push(int data)
    {
        if (top == 5)
        {
            System.out.println("StackOverflow");
        }
        else
        {
            stack[top] = data;
            top++;
//      move the top var up toward a vacant space
        }

    }

    public int pop()
    {
        int data = 0;

        if (top == 0)
        {
            System.out.println("StackUnderflow");
        }
        else
        {
//       simply makes it so you can select top with a value
            data = stack[top-1];
            stack[top-1] = 0;
            top--;

        }
        return data;
    }

    public int peek()
    {
        int data;

        data = stack[top-1];
        return data;


    }
    public int size()
    {
        return top;
    }

    public boolean isEmpty()
    {
        if (top == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public void show()
    {
        for (int n: stack)
//       this how you print the elements of a stack
        {
            System.out.print(n + " ");
        }
        System.out.println();
    }

}
