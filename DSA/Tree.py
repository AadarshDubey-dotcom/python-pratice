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

     def search(self, root, key):
          if root is None or root.key == key:
               return root
          if key < root.key:
               return self.search(root.left, key)
          return self.search(root.right, key)  

     def inorder(self, root):
          if root:
               self.inorder(root.left)
               print(root.key, end=" ")
               self.inorder(root.right)

bst = BST()
root = None
root = bst.insertion(root, 50)
root = bst.insertion(root, 30)
root = bst.insertion(root, 20)     
root = bst.insertion(root, 40)
root = bst.insertion(root, 70)
root = bst.insertion(root, 60)     

print("Inorder traversal of the BST:")
bst.inorder(root)

