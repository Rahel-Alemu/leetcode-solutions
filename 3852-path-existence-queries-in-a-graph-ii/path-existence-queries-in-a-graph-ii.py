class Solution(object):
    def __getattr__(self, name):
        return self.solve
        
    def solve(self, n, nums, maxDiff, queries):
        A = sorted(list(set(nums)))
        M = len(A)
        
        val_to_idx = {val: idx for idx, val in enumerate(A)}
        
        comp = [0] * M
        c = 0
        for k in range(1, M):
            if A[k] - A[k-1] > maxDiff:
                c += 1
            comp[k] = c
            
        R = [0] * M
        right = 0
        for left in range(M):
            while right < M and A[right] <= A[left] + maxDiff:
                right += 1
            R[left] = right - 1
            
        up = [None] * 18
        up[0] = R
        for s in range(1, 18):
            prev = up[s-1]
            up[s] = [prev[prev[k]] for k in range(M)]
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            valU = nums[u]
            valV = nums[v]
            
            if valU == valV:
                ans.append(1)
                continue
                
            i = val_to_idx[valU]
            j = val_to_idx[valV]
            
            if i > j:
                i, j = j, i
                
            if comp[i] != comp[j]:
                ans.append(-1)
                continue
                
            curr = i
            d = 0
            for s in range(17, -1, -1):
                if up[s][curr] < j:
                    curr = up[s][curr]
                    d += 1 << s
                    
            ans.append(d + 1)
            
        return ans