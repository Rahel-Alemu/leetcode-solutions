class Solution(object):
    def canReach(self, arr, start):
        stack = [start]
        visited = {start}
        
        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            
            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < len(arr) and nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
                    
        return False