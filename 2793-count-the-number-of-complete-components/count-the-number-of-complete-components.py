class Solution(object):
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                v_count = 0
                e_count = 0
                
                while q:
                    u = q.pop()
                    v_count += 1
                    e_count += len(adj[u])
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                            
                if e_count == v_count * (v_count - 1):
                    ans += 1
                    
        return ans