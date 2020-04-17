class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print(self.value, end=" ")
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invertTree(root):
    if not root:
        return None
    right = invertTree(root.right)
    left = invertTree(root.left)
    root.left = right
    root.right = left
    return root

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
invertTree(root)
print("\n")
root.preorder()