class Solution(object):
    def minScore(self, n, roads):
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        visited = [False] * (n + 1)
        visited[1] = True
        q = [1]
        ans = float('inf')
        
        while q:
            nxt = []
            for u in q:
                for v, w in adj[u]:
                    if w < ans:
                        ans = w
                    if not visited[v]:
                        visited[v] = True
                        nxt.append(v)
            q = nxt
            
        return ans