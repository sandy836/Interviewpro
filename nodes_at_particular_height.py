class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    if not root:
        return 
    if height == 1:
        print(root.value, end=' ')
    valuesAtHeight(root.left, height-1)
    valuesAtHeight(root.right, height-1)

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
valuesAtHeight(a, 3)