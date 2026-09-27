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
"""Workflow of Your Stack Code
1. Initialization
s = Stack()  
👉 Ek empty stack ban gaya: []

2. Push Operations
s.push(10) → stack = [10]

s.push(20) → stack = [10, 20]

s.push(30) → stack = [10, 20, 30]

👉 Har push me element end me add hota hai (top of stack).

3. Display
s.display() → prints [10, 20, 30]  
👉 Ye tumhe current stack list dikhata hai.

4. Pop Operation
s.pop() → removes last element (30)

Returns 30

Now stack = [10, 20]

👉 LIFO principle: Last In (30) → First Out.

5. Peek Operation
s.peek() → shows last element (20)

Stack remains [10, 20] (no removal)

👉 Peek sirf top element ko dekhne ke liye hota hai."""
