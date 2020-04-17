class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def _ceil(root, k):
    if not root:
        return -1
    if root.value == k:
        return k
    if root.value<k:
        return _ceil(root.right, k)
    value = _ceil(root.left, k)
    return value if value>=k else root.value

def _floor(root, k):
    if not root:
        return float('inf')
    if root.value == k:
        return k
    if root.value>k:
        return _floor(root.left, k)
    value = _floor(root.right, k)
    return value if value<=k else root.value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    _floor_val = _floor(root_node,k)
    _ceil_val = _ceil(root_node,k)
    if _floor_val == float('inf') or _ceil_val == -1:
        return None
    else:
        return _floor_val, _ceil_val

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 15))