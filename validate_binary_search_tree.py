class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

def is_bst(root, min_value = float('-inf'), max_value = float('inf')):
    if not root:
        return True 
    if not min_value<root.val<max_value:
        return False
    return is_bst(root.left, min_value, root.val) and is_bst(root.right,  root.val, max_value)

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))