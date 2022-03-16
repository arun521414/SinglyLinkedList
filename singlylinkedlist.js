class List{

     head = null;

     Node = class{
         data = null
         next = null

         constructor(data) {
             this.data = data;
             this.next = null;
         }
         
     }

     insertAtBeginning  = (data)=>{
         var newNode = new this.Node(data);

         if(this.head == null){
             this.head = newNode
         }
         else{
             newNode.next = this.head;
             this.head = newNode;
         }
     }

     insertAtEnd = (data)=>{
         var newNode = new this.Node(data);

         if(this.head == null){

             this.head = newNode;
         }
         else{

             var temp = this.head;

             while(temp.next != null){
                 temp = temp.next;
             }

             temp.next = newNode;
         }
     }


     insertAtPosition = (index,data)=>{
         if(index == 0){
             this.insertAtBeginning(data);
             return NaN;
         }
         var newNode = new this.Node(data);
         var curr = this.head;
         var prev = null;
         for(var i = 1;i<=index;i++){

             prev = curr;
             curr = curr.next;
         }

         newNode.next = prev.next;
         prev.next = newNode;
     }

     deleteAtPosition = (index)=>{
         if(index == 0){
             this.head = this.head.next;
         }
         else{
             var curr  = this.head
             var prev = null;

             for(var i = 1;i<=index;i++){
                 prev = curr;
                 curr = curr.next;
             }
             prev.next = curr.next;
         }
     }

     reverse = ()=>{

         var prev = null;
         var curr = this.head;
         var next = this.head.next;

         while(curr != null){
             next = curr.next;
             curr.next = prev;
             prev = curr;
             curr = next;
         }

         this.head = prev;


     }

     display = ()=>{

         var temp = this.head;
         var string = "";

         while(temp!=null){
             string += temp.data + ",";
             temp = temp.next;
         }

         if(string!=""){

             
            string = "["+string.substring(0,string.length - 1) + "]"

         }
         else{
             string = "[]"
         }
         console.log(string);
     }
    
     isEmpty = ()=>{
         if(this.head==null){
             return true;
         }
         else{
             return false;
         }
     }
     
}

var list = new List();
list.insertAtBeginning("arun")
list.insertAtBeginning("elakiya")
list.display()



