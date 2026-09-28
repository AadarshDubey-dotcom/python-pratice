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

