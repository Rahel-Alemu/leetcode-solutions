from collections import deque

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = (n + 1).bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        parent = [0] * (n + 1)
        parent[1] = 1

        while q:
            u = q.popleft()
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        for i in range(1, n + 1):
            up[0][i] = parent[i]

        for k in range(1, LOG):
            for i in range(1, n + 1):
                up[k][i] = up[k - 1][up[k - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        ans = []
        for u, v in queries:
            w = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[w]
            ans.append(0 if d == 0 else pow(2, d - 1, MOD))

        return ans