# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def rec(l,r):
            if l and r:
                if l.val==r.val:
                    return rec(l.left,r.right) and rec(l.right,r.left)
            if not l and not r:
                return True
            return False
        return rec(root.left,root.right)