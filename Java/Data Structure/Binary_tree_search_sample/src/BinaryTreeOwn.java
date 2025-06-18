
class Node {
    int data;
    Node left;
    Node right;

    public Node(int data){
        this.data = data;
//        then left and right is automatically = null
    }
}

public class BinaryTreeOwn {

    Node root;
    public void insert(int data) {
        root = insertRec(root, data);
    }
    public Node insertRec( Node root, int data ) {
        if (root == null) {
            root = new Node(data);
//          this root is actualy a local root

//          if this condition is true, then new node is created with the data

//          if this condition passes, the root returns to the previous recursion
//          where root.right is equal to this root
//          and this will continue  to connect upwards till it connects to the main root
//           like root.right = (value)-root.right = (value)-root.right
        } else if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data){
            root.right = insertRec(root.right, data);
//           so I'm actually passing the root.right as root in this function
        }

        return root;
    }

    public void inorder(){
        inorderRec(root);
    }

    public void inorderRec(Node root){
        if(root != null){
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }
}


