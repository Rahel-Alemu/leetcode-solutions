from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 1000000007
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([(1, 0)])
        vis = [False] * (n + 1)
        vis[1] = True
        mx = 0

        while q:
            u, d = q.popleft()
            mx = max(mx, d)
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append((v, d + 1))

        return pow(2, mx - 1, MOD)