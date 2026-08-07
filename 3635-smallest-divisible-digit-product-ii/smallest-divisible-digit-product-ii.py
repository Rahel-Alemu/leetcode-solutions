class Solution:
    def smallestNumber(self, num, t):
        v = [0, 0, 0, 0]
        temp_t = t
        for i, p in enumerate([2, 3, 5, 7]):
            while temp_t % p == 0:
                v[i] += 1
                temp_t //= p
        if temp_t > 1: return "-1"
        
        m23 = [[0] * 50 for _ in range(70)]
        for i in range(70):
            for j in range(50):
                if i == 0 and j == 0: continue
                best = 1000
                if i > 0: best = min(best, m23[max(0, i - 1)][j])
                if i > 1: best = min(best, m23[max(0, i - 2)][j])
                if i > 2: best = min(best, m23[max(0, i - 3)][j])
                if j > 0: best = min(best, m23[i][max(0, j - 1)])
                if j > 1: best = min(best, m23[i][max(0, j - 2)])
                if i > 0 and j > 0: best = min(best, m23[max(0, i - 1)][max(0, j - 1)])
                m23[i][j] = 1 + best

        def check(rem, a, b, c, d):
            a, b, c, d = max(0, a), max(0, b), max(0, c), max(0, d)
            return rem >= (c + d + m23[min(69, a)][min(49, b)])

        def get_diff(dx):
            if dx == 2: return (1, 0, 0, 0)
            if dx == 3: return (0, 1, 0, 0)
            if dx == 4: return (2, 0, 0, 0)
            if dx == 5: return (0, 0, 1, 0)
            if dx == 6: return (1, 1, 0, 0)
            if dx == 7: return (0, 0, 0, 1)
            if dx == 8: return (3, 0, 0, 0)
            if dx == 9: return (0, 2, 0, 0)
            return (0, 0, 0, 0)

        n = len(num)
        p = [[0, 0, 0, 0] for _ in range(n + 1)]
        z = -1
        for i in range(n):
            d = int(num[i])
            if d == 0:
                z = i
                break
            diff = get_diff(d)
            p[i+1] = [p[i][j] + diff[j] for j in range(4)]
        
        if z == -1 and check(0, v[0]-p[n][0], v[1]-p[n][1], v[2]-p[n][2], v[3]-p[n][3]):
            return num
        
        def fill(rem, a, b, c, d):
            res = []
            for i in range(rem):
                for dx in range(1, 10):
                    da, db, dc, dd = get_diff(dx)
                    if check(rem - 1 - i, a - da, b - db, c - dc, d - dd):
                        res.append(str(dx))
                        a, b, c, d = a - da, b - db, c - dc, d - dd
                        break
            return "".join(res)

        limit = z if z != -1 else n - 1
        for i in range(limit, -1, -1):
            for dx in range(int(num[i]) + 1, 10):
                da, db, dc, dd = get_diff(dx)
                ra, rb, rc, rd = v[0]-p[i][0]-da, v[1]-p[i][1]-db, v[2]-p[i][2]-dc, v[3]-p[i][3]-dd
                if check(n - 1 - i, ra, rb, rc, rd):
                    return num[:i] + str(dx) + fill(n - 1 - i, ra, rb, rc, rd)
        
        ln = n + 1
        while not check(ln, v[0], v[1], v[2], v[3]): ln += 1
        return fill(ln, v[0], v[1], v[2], v[3])