class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        sz = 1
        while sz < n:
            sz *= 2

        # Generate unrolled leaf() and comb() specialized for this k
        leaf_body = []
        for a in range(k):
            for b in range(k):
                leaf_body.append("(1 if (%d*v)%%k==%d else 0)" % (a, b))
        leaf_src = (
            "def leaf(v):\n"
            "    v %= k\n"
            "    return v, (" + ",".join(leaf_body) + ",)\n"
        )

        comb_terms = []
        for a in range(k):
            for b in range(k):
                comb_terms.append("lM[%d]+rM[cc[%d]+%d]" % (a * k + b, a, b))
        cc_lines = "    cc = [%s]\n" % ",".join("((%d*lt)%%k)*k" % a for a in range(k))
        comb_src = (
            "def comb(lt, lM, rt, rM):\n"
            "    t = (lt*rt) % k\n"
            + cc_lines +
            "    return t, (" + ",".join(comb_terms) + ",)\n"
        )

        ns = {"k": k}
        exec(leaf_src, ns)
        exec(comb_src, ns)
        leaf = ns["leaf"]
        comb = ns["comb"]

        T = [1 % k] * (2 * sz)
        M = [None] * (2 * sz)

        idT, idM = 1 % k, tuple(0 for _ in range(k * k))

        for i, v in enumerate(nums):
            T[sz + i], M[sz + i] = leaf(v)
        for i in range(n, sz):
            T[sz + i], M[sz + i] = idT, idM
        for i in range(sz - 1, 0, -1):
            T[i], M[i] = comb(T[2*i], M[2*i], T[2*i+1], M[2*i+1])

        def update(idx, val):
            p = sz + idx
            T[p], M[p] = leaf(val)
            p //= 2
            while p:
                T[p], M[p] = comb(T[2*p], M[2*p], T[2*p+1], M[2*p+1])
                p //= 2

        def query(l, r):
            l, r = l + sz, r + sz + 1
            lt, lM, rt, rM = idT, idM, idT, idM
            while l < r:
                if l & 1:
                    lt, lM = comb(lt, lM, T[l], M[l])
                    l += 1
                if r & 1:
                    r -= 1
                    rt, rM = comb(T[r], M[r], rt, rM)
                l >>= 1
                r >>= 1
            return comb(lt, lM, rt, rM)

        a0 = 1 % k
        res = []
        for i, v, s, x in queries:
            update(i, v)
            res.append(query(s, n - 1)[1][a0 * k + x])
        return res