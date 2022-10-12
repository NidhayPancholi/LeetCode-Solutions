class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[[1]*5]*n
        
        for i in range(1,n):
            for j in range(5):
                dp[i][j]=sum(dp[i-1][j:])
        
        return sum(dp[n-1])
        
        