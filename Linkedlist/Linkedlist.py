class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        
# - Inserting the Head

    def insert_head(self , data):
        new_node = Node(data)
        if self.head is None: # Check if the list is empty
            self.head = new_node      # Set the new node as the head
        else: 
        # ho yeh raha he k agar head he to 1 new node lagao or usko head bana do
            new_node.next = self.head  # Add the new node before the Head 
            self.head = new_node       # Call it / use it as a Head
          
       
# - Delete the Ending Node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:  # Check if the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the new node at the end



# - Delete By Value

    def deletion_byvalue(self, value):
        if not hasattr(self, 'head'):  # Check if the list is -Empty
           return  # - Nothing to Delete
        
        current = self.head
        previous = None

        while current:
            # This line checks if the value stored in the current node (accessed with current.Node) is equal to the value we want to delete. If It is, we will delete this Node.
            if current.data == value:
                # This line checks if previous is not None. If previous is not None, it means that current is not the first node ( head ) of the list.
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                # - After Deleting the node, This line tells the method to stop running. We don’t need to check any more nodes since we’ve already completed the deletion.
                return

            previous = current 
            # Previous --> Cuurent 
            current = current.next
            # Cuurent --> Next           

# - Delete By Positon

    def del_bypos(self, position):

        if not hasattr(self, 'head'):
            return

        current = self.head

        if position == 0:
            self.head = current.next
            return

        previous = None
        count = 0


        while current and count < position:
                previous = current
                current = current.next
                count +=1

    
        if current and count == position:
            previous.next = current.next
            return       
        

    def printlist(self):
        current = self.head

        while current:
            print(current.data, end= " --> ")
            current = current.next
        print("None")


l = linkedlist()
l.insert_head(11) 
l.printlist()

l.insert_head(12) 
l.printlist()

l.insert_end(10)
l.printlist()

l.deletion_byvalue(11)
l.printlist()

l.del_bypos(1)
l.printlist()













        # Link list with insert , insert head , insert end , deletion by value and position