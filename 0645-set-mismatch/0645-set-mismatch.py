class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        o=[0]*n
        output=[0,0]
        for i in nums:
            if o[i-1]==1:
                output[0]=i
            
            o[i-1]+=1
        
        output[1]=list(set([i for i in range(1,n+1)])-set(nums))[0]
        
        return output
        
        