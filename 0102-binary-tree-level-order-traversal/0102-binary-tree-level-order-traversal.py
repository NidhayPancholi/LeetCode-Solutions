# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        o=[]
        def rec(queue):
            temp=[]
            new=[]
            for x in queue:
                if x:
                    temp.append(x.val)
                    new.append(x.left)
                    new.append(x.right)
            if not temp:
                return 
            o.append(temp)
            return rec(new)
        
        rec([root])
        return o
        
        