class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s=list(s)
        o=s.copy()
        for i in range(len(s)):
            o[indices[i]]=s[i]
        return "".join(o)