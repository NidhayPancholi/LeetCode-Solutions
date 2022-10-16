class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        for x in range(num):
            if x+int(str(x)[::-1])==num:
                return True
        return False
                
        