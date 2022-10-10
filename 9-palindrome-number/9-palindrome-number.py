class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        n=len(s)
        for x in range(n):
            if s[x]!=s[n-x-1]:
                return False
        return True
        
        