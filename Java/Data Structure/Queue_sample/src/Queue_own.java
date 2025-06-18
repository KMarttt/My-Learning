public class Queue_own
{
    int queue[] = new int[5];
    int size = 0;
    int front = 0;
    int rear = 0;

    public void enQueue(int data)
    {
        if (!isFull())
        {
            queue[rear] = data;
            rear = (rear + 1)%5;
//          this makes circular array, where rear can return to 0 and override it once rear exceed the array size of 5
            size++;
        }
        else
        {
            System.out.println("Queue is full");
        }

    }

    public int deQueue()
    {
//      this is lazy way of doing it, he didn't delete the said value on the array
//      if it were me, I would loop the whole array, to move the value down an index
        int data = queue[front];

        if (!isEmpty())
        {
            front = (front + 1)%5;
//          will return to 0 once front exceed array size of 5
            size--;
        }
        else
        {
            System.out.println("Queue is empty");
        }

        return data;
    }

    public int getSize()
    {
        return size;
    }

    public boolean isEmpty()
    {
        return getSize()==0;
//      this will return true if size == 0
    }

    public boolean isFull()
    {
        return getSize()==5;
    }


    public void show()
    {
        System.out.print("Elements: ");
        for (int i = 0; i<size; i++)
        {
            System.out.print(queue[(front + i)%5] + " ");
        }
    }

}
