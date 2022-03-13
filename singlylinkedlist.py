class List:
    
    __head = None
    
    class __Node:
        
        data = None
        next = None
        
        #constrcutor initialize the new Node data
        
        def __init__(self,data):
            
            self.data = data
            self.next = None
    
    #insert methods start
    
    def insertAtBeginning(self,data):
        
        newNode = self.__Node(data) #new Node
        
        if( self.__head == None ):
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head    = newNode
    
    def insertAtEnd(self,data):
        
        newNode = self.__Node(data)
        temp    = self.__head
        
        if( self.__head == None ):
            self.__head = newNode
        else:
            while( temp.next != None ):
                temp = temp.next
            temp.next = newNode
    
    def insertAtPosition(self,index,data):
        
        if( index == 0):
            self.insertAtBeginning(data)
            return None
        
        newNode = self.__Node(data)
        temp = self.__head
        
        index = index - 1
        
        for i in range(index):
            if( temp.next == None ):
                self.insertAtEnd(data)
                return None
            temp = temp.next
        
        newNode.next = temp.next
        temp.next    = newNode
        
        
    
    #insert methods end
    
    #delete methods start
    #delete  node using data
    
    def delete(self,data):
        
        temp = self.__head
        prev = None
        
        if( self.__head.data == data ):
            self.__head = self.__head.next
            return None
        
        while( temp!=None ):
            if(temp.data==data):
                prev.next = temp.next
            prev = temp
            temp = temp.next
        

        #delete node using index 
        
    def deleteAt(self,index):
        
        temp = self.__head
        prev = None
        
        if(index==0):
            self.__head = self.__head.next
            return None
        
        for i in range(index):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        
    #delete method end
    
    #reverse method   
    
    def reverse(self):
        
        prev = None
        temp = self.__head
        next = self.__head.next
        
        while(temp!= None):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        self.__head = prev
        
    
        
        
    
    #string method invoke when object print eg :- print(obj)
    
    def __str__(self):
        
        string = ""
        temp = self.__head
        
        while( temp != None ):
            string += temp.data+","
            temp    = temp.next
            
        if( string != None ):
            string = "[" + string[0:len(string)-1] + "]"
        else:
            string = "[]"
        
        return string
    
    def isEmpty(self):
        if(self.__head == None):
            return True
        else:
            return False
        
list = List()
list.insertAtBeginning("arun")
list.insertAtEnd("abi")

list.insertAtPosition(2, "elakiya")
list.reverse()
print(list)



            

        
        
        