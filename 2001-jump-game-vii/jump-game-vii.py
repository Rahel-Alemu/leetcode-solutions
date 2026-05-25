class Solution(object):
    def canReach(self, s, minJump, maxJump):
        if s[-1] == '1':
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        reachable_count = 0
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1
                
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[-1]