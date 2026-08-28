from collections import Counter

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]
        if n % 2 == 0:
            if len(odd_chars) != 0:
                return ""
            mid = ""
        else:
            if len(odd_chars) != 1:
                return ""
            mid = odd_chars[0]

        half_len = n // 2
        half_counts = [0] * 26
        for c, f in cnt.items():
            half_counts[ord(c) - 97] = f // 2

        # Try exact match construction
        exact_counts = half_counts[:]
        feasible = True
        for i in range(half_len):
            idx = ord(target[i]) - 97
            exact_counts[idx] -= 1
            if exact_counts[idx] < 0:
                feasible = False
                break

        if feasible:
            half = target[:half_len]
            full = half + mid + half[::-1]
            if full > target:
                return full

        # Pivot search within the half
        avail = half_counts[:]
        neg_count = [0]

        def adjust(idx, delta):
            old_neg = avail[idx] < 0
            avail[idx] += delta
            new_neg = avail[idx] < 0
            if old_neg and not new_neg:
                neg_count[0] -= 1
            elif not old_neg and new_neg:
                neg_count[0] += 1

        for i in range(half_len):
            adjust(ord(target[i]) - 97, -1)

        for p in range(half_len - 1, -1, -1):
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
                    half = target[:p] + chr(candidate + 97) + ''.join(remaining)
                    full = half + mid + half[::-1]
                    return full

        return ""