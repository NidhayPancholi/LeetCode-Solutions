class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        i=1
        temp=pref[0]
        while i<n:
            pref[i]=temp^pref[i]
            temp=temp^pref[i]
            i+=1
        
        return pref
            
        