# Queue
class Queue:
     def __init__(self):
          self.queue = []
          
     def enqueue(self, data):
          self.queue.append(data)
     
     def dequeue(self):
          if not self.isEmpty():
               return self.queue.pop()
          return "Queue is empty"     
     
     def peek(self):
          if not self.isEmpty():
               return self.queue[0]
          return "Queue is empty"
          
     def isEmpty(self):
          return len(self.queue) == 0
          
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
"""Flow Samajho
Enqueue(10) → [10]

Enqueue(20) → [10, 20]

Enqueue(30) → [10, 20, 30]

Dequeue() → tumhare code me 30 niklega (last element)

Dequeue() → phir 20 niklega

👉 Matlab tumhari current logic = LIFO  
👉 Correct FIFO logic = pop(0) use karo"""
