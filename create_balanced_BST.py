from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)+" "
      nodes.append(node.left)
      nodes.append(node.right)
    return answer


def createBalancedBST(nums):
    if not nums:
        return None 
    mid = len(nums)//2
    root = Node(nums[mid])
    root.left = createBalancedBST(nums[0:mid])
    root.right = createBalancedBST(nums[mid+1:])
    return root

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))