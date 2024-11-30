class stack():
    def __init__(self, item):
        self.items = [1,2,3,4,5,6,8,9,10]
        return
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        if self.is_empty():
            self.items.append(item)
        else:
            return IndexError
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Pop the last item
        else:
            raise IndexError("Pop from empty stack")  # Raise an exception

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)    
    
s = stack(None)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek())