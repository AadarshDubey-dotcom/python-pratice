#BST
class Node:
     def __init__(self, key):
          self.key = key
          self.left = None
          self.right = None

class BST:
     def __init__(self):
          self.root = None

     def insertion(self, root, key):
          if root is None:
               return Node(key)
          if key < root.key:
               root.left = self.insertion(root.left, key)
          elif key > root.key:
               root.right = self.insertion(root.right, key)
          return  