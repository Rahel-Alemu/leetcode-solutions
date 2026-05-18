import collections

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
            
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        q = collections.deque([0])
        visited = {0}
        steps = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == n - 1:
                    return steps
                
                for nxt in (curr - 1, curr + 1):
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
                        
                for nxt in graph[arr[curr]]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
                        
                del graph[arr[curr]]
                
            steps += 1
            
        return 0