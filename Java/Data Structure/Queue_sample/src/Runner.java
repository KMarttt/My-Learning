public class Runner {
    public static void main (String[] args)
    {
        Queue_own q = new Queue_own();

        System.out.println("Queue is empty: " + q.isEmpty());
        q.enQueue(5);
        q.enQueue(2);
        q.enQueue(7);
        q.enQueue(3);

        q.deQueue();
        q.deQueue();

        q.enQueue(9);
        q.enQueue(1);

        q.enQueue(19);
        System.out.println("Queue is full: " + q.isFull());


        q.enQueue(15);

        System.out.println("Size: " + q.getSize());

        q.show();
    }
}
