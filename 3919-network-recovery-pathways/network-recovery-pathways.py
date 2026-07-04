class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                
        for u in range(n):
            adj[u].sort(key=lambda x: x[1], reverse=True)
            
        q = [i for i in range(n) if in_degree[i] == 0]
        topo = []
        while q:
            u = q.pop()
            topo.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        inf = 10**15
        
        def check(min_val):
            dist = [inf] * n
            dist[0] = 0
            for u in topo:
                d = dist[u]
                if d != inf:
                    for v, cost in adj[u]:
                        if cost < min_val:
                            break
                        if d + cost < dist[v]:
                            dist[v] = d + cost
            return dist[n - 1] <= k

        low = 0
        high = 10**9
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans