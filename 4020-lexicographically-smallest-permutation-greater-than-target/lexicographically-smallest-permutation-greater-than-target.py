class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        avail = [0] * 26
        for ch in s:
            avail[ord(ch) - 97] += 1

        neg_count = [0]

        def adjust(idx, delta):
            old_neg = avail[idx] < 0
            avail[idx] += delta
            new_neg = avail[idx] < 0
            if old_neg and not new_neg:
                neg_count[0] -= 1
            elif not old_neg and new_neg:
                neg_count[0] += 1

        for ch in target:
            adjust(ord(ch) - 97, -1)

        for p in range(n - 1, -1, -1):
            idx_p = ord(target[p]) - 97
            adjust(idx_p, 1)

            if neg_count[0] == 0:
                candidate = None
                for c in range(idx_p + 1, 26):
                    if avail[c] > 0:
                        candidate = c
                        break
                if candidate is not None:
                    adjust(candidate, -1)
                    remaining = []
                    for c in range(26):
                        remaining.append(chr(c + 97) * avail[c])
                    return target[:p] + chr(candidate + 97) + ''.join(remaining)

        return ""