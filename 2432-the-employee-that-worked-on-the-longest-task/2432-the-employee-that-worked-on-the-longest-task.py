class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start=0
        m=0
        output=-1
        for t in logs:
            if m<=t[1]-start:
                if m==t[1]-start:
                    output=min(t[0],output)
                else:
                    m=t[1]-start
                    output=t[0]
            start=t[1]
        return output
            
            
        