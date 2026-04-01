class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        robots.sort()
        
        stack = []
        survivors = []
        
        for r in robots:
            if r[2] == 'R':
                stack.append(r)
            else:
                while stack and r[1] > 0:
                    if stack[-1][1] < r[1]:
                        stack.pop()
                        r[1] -= 1
                    elif stack[-1][1] > r[1]:
                        stack[-1][1] -= 1
                        r[1] = 0
                    else:
                        stack.pop()
                        r[1] = 0
                
                if r[1] > 0:
                    survivors.append(r)
        
        final_survivors = survivors + stack
        final_survivors.sort(key=lambda x: x[3])
        
        return [r[1] for r in final_survivors]