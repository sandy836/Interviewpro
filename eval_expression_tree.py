class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "//"

def evaluate(root):
    if not root.left and not root.right:
        return root.val 
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)
    return eval(str(left_val)+root.val+str(right_val))


tree = Node(DIVIDE)
tree.left = Node(TIMES)
tree.left.left = Node(2)
tree.left.right = Node(PLUS)
tree.right = Node(4)
tree.left.right.left = Node(3)
tree.left.right.right = Node(DIVIDE)
tree.left.right.right.left = Node(6)
tree.left.right.right.right = Node(2)
print(evaluate(tree))
# 45