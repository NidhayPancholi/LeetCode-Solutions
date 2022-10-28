"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        o=[]
        def rec(root):
            o.append(root.val)
            if root.children:
                for x in root.children:
                    rec(x)
        rec(root)
        
        return o