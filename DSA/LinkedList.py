"""Linked List ek linear data structure hai jisme elements (jinhe nodes kehte hain) contiguous 
memory (jaise array) mein nahi, balki pointers / references ke zariye ek-dusre se judey hote hain."""
"""Singly Linked List:

Har node sirf agle node (next) ka reference rakhta hai.

Traversal sirf one direction (head se tail tak) mein hota hai."""
class Node:
     def __init__(self, data):
          self.data = data
          self.next = None 
class SinglyLinkedList:
     def __init__(self):
               self.head = None   
     def insert_at_head(self, data):
               new_node = Node(data)
               new_node.next = self.head
               self.head = new_node     
     def print_list(self):
          curr = self.head
          while curr:
               print(curr.data, end=" => ")
               curr = curr.next
          print("None")                      
li = SinglyLinkedList()
li.insert_at_head(18)
li.insert_at_head(20)
li.insert_at_head(38)
li.print_list()          