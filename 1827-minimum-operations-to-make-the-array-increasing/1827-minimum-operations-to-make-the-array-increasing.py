class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        output=0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                continue
            output+=abs(nums[i]-nums[i-1])+1
            nums[i]=nums[i-1]+1
        return output