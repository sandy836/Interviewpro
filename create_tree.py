class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def pre_order(root):
    if not root:
        return
    print(root.val, end= " ")
    pre_order(root.left)
    pre_order(root.right)

def get_index(node_value, inorder):
    for i in range(len(inorder)):
        if node_value == inorder[i]:
            return i 
    
def reconstruct(preorder, inorder):
    if not inorder:
        return None 
    node_value = preorder.pop(0)
    root = Node(node_value)
    _index = get_index(node_value, inorder)
    root.left = reconstruct(preorder, inorder[0:_index])
    root.right = reconstruct(preorder, inorder[_index+1:])
    return root

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
pre_order(tree)