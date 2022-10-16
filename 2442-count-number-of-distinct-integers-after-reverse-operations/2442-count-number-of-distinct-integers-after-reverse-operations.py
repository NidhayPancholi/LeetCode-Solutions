class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        t=[]
        for x in nums:
            x=int(str(x)[::-1])
            t.append(x)
        nums.extend(t)
        return len(set(nums))