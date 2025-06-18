public class Dynamic_stack_own {
    int capacity = 2;
    int stack[] =new int[capacity];
    int top = 0;

    private void expand()
//  private makes it so only this class will have access on this function
    {
        int length = size();
        int newStack[] = new int[capacity*2];

        System.arraycopy(stack, 0, newStack, 0, length);
        stack = newStack;
        capacity = capacity * 2;
    }

    public void push(int data)
    {
        if (size() == capacity) {
            expand();
        }
        stack[top] = data;
        top++;


    }

    private void shrink()
    {
        int length = size();
        int newStack[] = new int[capacity/2];

        System.arraycopy(stack, 0, newStack, 0, length);
        stack = newStack;
        capacity = capacity/2;

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
            data = stack[top-1];
            stack[top-1] = 0;
            top--;

            if (size() <= (capacity/4))
//          if element takes 1/4 of the array size, then shrink
            {
                shrink();
            }

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
        {
            System.out.print(n + " ");
        }
        System.out.println();
    }


}
