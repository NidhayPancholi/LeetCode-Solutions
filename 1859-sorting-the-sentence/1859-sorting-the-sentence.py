class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        o=s.copy()
        
        for i in s:
            if i!="":
                
                o[int(i[-1])-1]=i[:-1]
        return " ".join(o)
        