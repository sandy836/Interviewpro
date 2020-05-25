class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val 

def preorder(root):
    if not root:
        return
    preorder(root.left)
    print(root.val, end=" ")
    preorder(root.right)

def largest_bst_subtree(root):
    if not root:
        return [True, float('-inf'), float('inf')]
    if not root.left and not root.right:
        return [True, root.val, root.val]
    left_subtree = largest_bst_subtree(root.left)
    right_subtree = largest_bst_subtree(root.right)
    global x
    if left_subtree[0] and right_subtree[0] and left_subtree[1]<root.val<right_subtree[2]:
        x = root
        return [True, max(root.val, left_subtree[1], right_subtree[1]),\
            min(root.val, left_subtree[2], right_subtree[2])] 
    return [False, 0, 0]


node = TreeNode(3)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
largest_bst_subtree(node)
preorder(x)