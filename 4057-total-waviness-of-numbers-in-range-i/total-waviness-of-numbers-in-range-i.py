class Solution(object):
    def totalWaviness(self, num1, num2):
        def solve(S):
            memo = {}
            def dfs(idx, prev2, prev1, is_less, is_started):
                if idx == len(S):
                    return (1, 0)
                state = (idx, prev2, prev1, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(S[idx])
                tot_count = 0
                tot_wave = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            c, w = dfs(idx + 1, -1, -1, next_less, False)
                            tot_count += c
                            tot_wave += w
                        else:
                            c, w = dfs(idx + 1, -1, d, next_less, True)
                            tot_count += c
                            tot_wave += w
                    else:
                        c, w = dfs(idx + 1, prev1, d, next_less, True)
                        tot_count += c
                        tot_wave += w
                        
                        if prev2 != -1 and prev1 != -1:
                            if (prev2 < prev1 and prev1 > d) or (prev2 > prev1 and prev1 < d):
                                tot_wave += c
                                
                memo[state] = (tot_count, tot_wave)
                return memo[state]

            return dfs(0, -1, -1, False, False)[1]

        return solve(str(num2)) - solve(str(num1 - 1))