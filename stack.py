from collections import deque

# stack = deque()

# print(dir(stack))

class Stack():
    def __init__(self):
        self.jar = deque()
    
    def push(self,val):
        self.jar.append(val)

    def pop(self):
        return self.jar.pop()
    
    def peek(self):
        return self.jar[-1]
    
    def is_empty(self):
        return len(self.jar == 0)
    
    def size(self):
        return len(self.jar)

    def reverse_string(self):
        if type(self.peek()) == str:
            return self.peek()[::-1]
        else:
            raise Exception("Invalid Input")


stack = Stack()
stack.push("hello")
stack.push(2)
stack.push("We will conquere COVID-19")
stack.push(5)

print(stack.reverse_string())


    

