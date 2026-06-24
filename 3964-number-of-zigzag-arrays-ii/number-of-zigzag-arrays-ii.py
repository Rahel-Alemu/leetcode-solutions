class Solution(object):
    def zigZagArrays(self, n, l, r):
        m = r - l + 1
        MOD = 10**9 + 7
        
        def multiply(A, B):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                row_A = A[i]
                row_C = C[i]
                for k in range(m):
                    if row_A[k]:
                        aik = row_A[k]
                        row_B = B[k]
                        for j in range(m):
                            row_C[j] += aik * row_B[j]
                C[i] = [x % MOD for x in row_C]
            return C

        def power(A, p):
            res = [[0] * m for _ in range(m)]
            for i in range(m):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res
            
        T = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i + j >= m:
                    T[i][j] = 1
                    
        P = power(T, n - 2)
        
        U2 = list(range(m))
        
        ans = 0
        for i in range(m):
            val = 0
            for j in range(m):
                val += P[i][j] * U2[j]
            ans = (ans + val) % MOD
            
        return (ans * 2) % MOD