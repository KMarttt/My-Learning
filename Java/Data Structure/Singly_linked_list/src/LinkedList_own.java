public class LinkedList_own
{
    Node head;
//    by default, the value for head is null
//    so if there is no fist node, then you can set it as head

    public void insert(int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
//      to make it more readable you can me it equal to null

//        if this is the first node
        if (head == null)
        {
            head = node;
        }
        else
//      if this is not your first node
        {
            Node n = head;
//          so n is your selected node
//          and it'll first start at the head
            while(n.next!=null)
//          this will select all the node till it reach the end (null)
            {
                n = n.next;
            }
            n.next = node;
        }
    }

    public void insertAtStart(int data)
    {
//        Node next_node = head;
//
//        Node node = new Node();
//        node.data = data;
//        node.next = next_node;
//
//        head = node;


//       VIDEO VERSION
        Node node = new Node();
        node.data = data;
        node.next = null;

        node.next = head;
//      You're setting the link field of the new node to the head
        head = node;
//      Then set head to the current node
    }

    public void insertAt(int index, int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;

        Node n = head;

        if (index == 0)
        {
            insertAtStart(data);
        }
        else
        {
            for (int i = 0; i < index - 1; i++)
            {
                n = n.next;
            }
            node.next = n.next;
            n.next = node;
        }
    }

    public void deleteAt(int index)
    {
        Node n = head;
        Node n_delete = null;

        if (index==0)
        {
            head = head.next;
        }
        else
        {
            for (int i = 0; i < index - 1; i++) {
                n = n.next;
            }
            n_delete = n.next;
//          this points to the node to deleted

            n.next = n_delete.next;
//          this connects the preceding node to the succeeding node the of the deleted node
            System.out.println("Node deleted (node data: " + n_delete.data +" )" );
            n_delete = null;
//          will delete the node
        }

    }

    public void show()
    {
        Node n = head;

        while(n.next != null)
        {
            System.out.println(n.data);
            n = n.next;
        }
        System.out.println(n.data);
    }

}
