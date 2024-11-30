class queue:
    def __init__(self):
        self.items = []
        return
    
    def is_empty(self):
        return len (self.items) == 0
    
    def Enqueue(self, item):
        # if self.is_empty():
             self.items.append(item)
        # else:
        #     return IndentationError
       
    def Deque(self):
        if not self.is_empty():
            return "First item: "+ str(self.items.pop(0))  # str() use tp convert an object into string
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return "Peak item: " + str(self.items[0])  # str() use tp convert an object into string
        else:
            return IndentationError
        
    def size(self):
        return "Size of the queue is: " + str(len(self.items))  # str() use tp convert an object into string

q = queue()
q.Enqueue(3)
q.Enqueue(2)
q.Enqueue(1)
print(q.Deque())
print(q.peek())
print(q.size())


# I have to understand more about Abstract and Polymorphism and Its important!!
