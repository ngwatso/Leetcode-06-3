# In-order traversal using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        
        if root != None:
            self.inorderTraversalHelper(root, res)      
        return res
    
    def inorderTraversalHelper(self, root, res):
        
        if root == None:
            return
        # go to left subtree first
        if root.left != None:
            self.inorderTraversalHelper(root.left, res)
        # process current node
        res.append(root.val)
        # got to right subtree next
        if root.right != None:
            self.inorderTraversalHelper(root.right, res)
        
'''

U:

[1, null, 2, 3]

output = [1, 3, 2]

[1, 2, null, null, 3, 4, 5]

output = [2, 1, 4, 3, 5]

P:

Use recursion to go to the left subtree first, then process the current node, then use recursion again to go to the right subtree next

'''

# ===============

# Pre-order traversal using recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        
        if root != None:
            self.preorderTraversalHelper(root, res)      
        return res
    
    def preorderTraversalHelper(self, root, res):
        
        if root == None:
            return
                
        res.append(root.val)
        
        if root.left != None:
            self.preorderTraversalHelper(root.left, res)

        if root.right != None:
            self.preorderTraversalHelper(root.right, res)

# ===============

# Pre-order traversal using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        
        if root != None:
            self.postorderTraversalHelper(root, res)      
        return res
    
    def postorderTraversalHelper(self, root, res):
        
        if root == None:
            return
        
        if root.left != None:
            self.postorderTraversalHelper(root.left, res)

        if root.right != None:
            self.postorderTraversalHelper(root.right, res)
            
        res.append(root.val)

# ===============

# level order traversal

from collections import deque

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')
d = BinaryTreeNode('d')
e = BinaryTreeNode('e')

a.left = b
a.right = c
b.left = d
b.right = e

def levelOrderTraversal(root):
    
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        curr = queue.popleft()
        print(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
            
levelOrderTraversal(a)

# ===============