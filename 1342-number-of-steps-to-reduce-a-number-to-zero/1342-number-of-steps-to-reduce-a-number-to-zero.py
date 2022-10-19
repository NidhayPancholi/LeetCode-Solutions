class Solution:
    def numberOfSteps(self, num: int) -> int:
        s=0
        while num>0:
            s+=1
            if num%2==0:
                num//=2
            else:
                num-=1
            
        return s