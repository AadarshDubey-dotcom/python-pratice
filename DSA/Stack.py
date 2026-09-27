#Stack 
class Stack:
     def __init__(self):
          self.stack = []
          
     def push(self, data):
          self.stack.append(data)
     
     def pop(self):
          if not self.isEmpty():
               return self.stack.pop()
          return "Stack is empty"     
     
     def peek(self):
          if not self.isEmpty():
               return self.stack[-1]
          return "Stack is empty"     
          
     def isEmpty(self):
          return len(self.stack) == 0
          
     def display(self):
          print(self.stack)
          
s = Stack()    
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())
print(s.peek())
