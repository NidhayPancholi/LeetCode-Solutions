class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c=Counter(s)
        t=0
        o=0
        for x in c:
            if c[x]%2==0:
                o+=c[x]
            else:
                o+=c[x]-1
                if not t:
                    t=1
                
        return o+t
        