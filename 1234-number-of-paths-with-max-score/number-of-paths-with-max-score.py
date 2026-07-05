class Solution(object):
    def pathsWithMaxScore(self, board):
        N = len(board)
        MOD = 10**9 + 7
        max_sum = [[-1] * N for _ in range(N)]
        paths = [[0] * N for _ in range(N)]
        
        max_sum[N - 1][N - 1] = 0
        paths[N - 1][N - 1] = 1
        
        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if board[r][c] == 'X' or (r == N - 1 and c == N - 1):
                    continue
                
                best = -1
                ways = 0
                
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    pr, pc = r + dr, c + dc
                    if pr < N and pc < N and paths[pr][pc] > 0:
                        if max_sum[pr][pc] > best:
                            best = max_sum[pr][pc]
                            ways = paths[pr][pc]
                        elif max_sum[pr][pc] == best:
                            ways = (ways + paths[pr][pc]) % MOD
                            
                if ways > 0:
                    paths[r][c] = ways
                    if board[r][c].isdigit():
                        max_sum[r][c] = best + int(board[r][c])
                    else:
                        max_sum[r][c] = best
                        
        if paths[0][0] == 0:
            return [0, 0]
        return [max_sum[0][0], paths[0][0]]