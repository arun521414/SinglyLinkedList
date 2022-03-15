public class singlylinkedlist {
   
    private Node head = null;

    private class Node{

        Object data;
        Node next;

        Node(Object data){
            this.data = data;
            this.next = null;
        }
    }

    public void insertAtBeginning(Object data){

        Node newNode = new Node(data);

        if(head==null){
            head = newNode;
        }
        else{
            newNode.next = head;
            head         = newNode;
        }
    }

    public void insertAtEnd(Object data){

        if(head == null){
            insertAtBeginning(data);
            return;
        }

        Node newNode = new Node(data);

        Node temp = head;

        while(temp.next != null){
            temp = temp.next;
        }

        temp.next = newNode;

    }

    public void insertAtPosition(int index,Object data){

        if(index == 0){
            insertAtBeginning(data);
            return;
        }
        Node newNode = new Node(data);

        Node temp = head;

        for(int i = 1;i<index;i++){
            if(temp.next == null){
                throw new NullPointerException("invalid index : "+index);
            }
            temp = temp.next;
        }

        newNode.next = temp.next;
        temp.next = newNode;
    }

    public void deleteAtPosition(int index){

        if(index == 0){
            head = head.next;
            return;
        }

        Node curr = head;
        Node prev = null;

        for(int i = 1;i<=index;i++){
            prev = curr;
            curr = curr.next;
        }

        prev.next = curr.next;


    }

    public void updateAtPosition(int index,Object data){
        Node temp = head;
       for(int i = 1;i<=index;i++){
           temp = temp.next;
       }
       temp.data = data;
    }

    public void reverse(){

        Node prev = null;
        Node curr = head;
        Node next = head.next;

        while(curr != null){

            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;

        }

        head = prev;
    }

    public String toString(){

        Node temp = head;
        String string = "";

        while(temp!=null){
            string += temp.data+",";
            temp = temp.next;
        }

        if(string!=""){
            string = "[" + string.substring(0, string.length() - 1) + "]";
        }
        else{
            string = "[]";
        }
        return string;
    }

    public Boolean isEmpty(){
        if(head == null){
            return true;
        }
        return false;
    }

}

