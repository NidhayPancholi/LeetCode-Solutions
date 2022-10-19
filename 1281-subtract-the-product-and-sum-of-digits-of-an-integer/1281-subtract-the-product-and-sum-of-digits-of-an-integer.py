class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n>0:
            j=n%10
            s+=j
            p*=j
            n=n//10
        return p-s
        