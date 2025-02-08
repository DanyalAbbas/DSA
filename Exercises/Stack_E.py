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

def reverse_string(string):
    stack = Stack()
    reverse = ''
    for i in range(len(string)):
        stack.push(string[i])
    
    i = stack.size()
    while i != 0:
        reverse += stack.pop()
        i -= 1
    return reverse


print(reverse_string("hehe"))


def is_balanced(string : str) -> bool:
    parenthesis = {"}" : "{", "]" : "[", ")" : "("}
    stack = Stack()
    for i in string:
        if i in parenthesis.values():
            stack.push(i)
        elif i in parenthesis.keys():
            if stack.size() == 0:
                return False
            if parenthesis.get(i) == stack.peek():
                stack.pop()
            else:
                return False
    return True

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{") )  
print(is_balanced("((a+b))") )    
print(is_balanced("))") )         
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    



    

