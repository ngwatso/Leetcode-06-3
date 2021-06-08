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