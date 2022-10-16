class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d={}
        output=0
        for x in nums:
            
            if abs(x) in d:
                if (d[abs(x)]==-1 and x>0) or (d[abs(x)]==1 and x<0):
                    output=max(abs(x),output)
            else:
                if x<0:
                    d[abs(x)]=-1
                elif x>0:
                    d[abs(x)]=1
        if output==0:
            return -1
        return output
                    
                    
        