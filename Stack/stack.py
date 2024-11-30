class stack():
    def __init__(self, item):  # Corrected __int__ to __init__
        self.items = [0,1,2,3,4,5,6,7,8,9,10]
        return 
    
    def is_empty(self):  # Fixed self.item to self.items
        return len(self.items) == 0 # Corrected return statement
    
    def push(self, item):
        if self.is_empty():  # Added parentheses to call the method
            self.items.append(item)
        else:
            return "Stack is not Empty"  # Fixed typo in message

    def pop(self):
        if not self.is_empty():  # Added parentheses to call the method
            return self.items.pop(5)  # Removed extra comma
        else:
            return IndexError("pop from empty stack")

    def peek(self): 
        if not self.is_empty():  # Added parentheses to call the method
            return self.items[-1]
        else:
            return IndexError("Peek from empty stack")
    
    def size(self):
        return len(self.items)
    
s = stack(None)  # Pass an initial item or change constructor to not require it
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())
        
