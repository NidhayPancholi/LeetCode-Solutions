class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        o=[]
        for i in nums:
            s+=i
            o.append(s)
        return o
            
            
        