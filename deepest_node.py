class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
    def deepest(self, root):
        self.global_deep = 0
        self.ans = None 
        def helper(root, deep):
            if not root.left and not root.right:
                if self.global_deep<deep:
                    self.ans = root.val 
                    self.global_deep = deep
                return 
            if root.left:
                helper(root.left, deep+1)
            if root.right:
                helper(root.right, deep+1)
        helper(root, 0)
        return self.ans, self.global_deep+1

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')
print(Solution().deepest(root))