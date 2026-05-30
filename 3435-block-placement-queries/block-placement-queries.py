import bisect

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] if self.tree[2 * i] > self.tree[2 * i + 1] else self.tree[2 * i + 1]
            
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2 == 1:
                if self.tree[l] > res: 
                    res = self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                if self.tree[r] > res: 
                    res = self.tree[r]
            l //= 2
            r //= 2
        return res

class Solution(object):
    def getResults(self, queries):
        m = max(q[1] for q in queries) + 1
        st = SegmentTree(m)
        obstacles = [0]
        res = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_right(obstacles, x)
                prev_x = obstacles[idx - 1]
                st.update(x, x - prev_x)
                if idx < len(obstacles):
                    next_x = obstacles[idx]
                    st.update(next_x, next_x - x)
                obstacles.insert(idx, x)
            else:
                x = q[1]
                sz = q[2]
                idx = bisect.bisect_right(obstacles, x)
                prev_x = obstacles[idx - 1]
                max_gap_before = st.query(0, prev_x + 1)
                res.append(max_gap_before >= sz or (x - prev_x) >= sz)
                
        return res