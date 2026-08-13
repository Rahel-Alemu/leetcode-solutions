class Node:
    def __init__(self):
        self.lc = ''
        self.rc = ''
        self.pre = 0
        self.suf = 0
        self.best = 0
        self.length = 0

class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [Node() for _ in range(4 * n)]

        def pull(i):
            a = tree[i * 2]
            b = tree[i * 2 + 1]
            t = tree[i]

            t.length = a.length + b.length
            t.lc = a.lc
            t.rc = b.rc

            t.pre = a.pre
            if a.pre == a.length and a.rc == b.lc:
                t.pre += b.pre

            t.suf = b.suf
            if b.suf == b.length and a.rc == b.lc:
                t.suf += a.suf

            t.best = max(a.best, b.best)

            if a.rc == b.lc:
                t.best = max(t.best, a.suf + b.pre)

        def build(i, l, r):
            if l == r:
                tree[i].lc = s[l]
                tree[i].rc = s[l]
                tree[i].pre = 1
                tree[i].suf = 1
                tree[i].best = 1
                tree[i].length = 1
                return

            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            pull(i)

        def update(i, l, r, pos, ch):
            if l == r:
                tree[i].lc = ch
                tree[i].rc = ch
                tree[i].pre = 1
                tree[i].suf = 1
                tree[i].best = 1
                return

            m = (l + r) // 2

            if pos <= m:
                update(i * 2, l, m, pos, ch)
            else:
                update(i * 2 + 1, m + 1, r, pos, ch)

            pull(i)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1].best)

        return ans