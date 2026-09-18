class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for i in range(n):
            ch = s[i]
            if first[ch] != i:
                continue
            start = i
            end = last[ch]
            j = i
            valid = True
            while j <= end:
                c2 = s[j]
                if first[c2] < start:
                    valid = False
                    break
                if last[c2] > end:
                    end = last[c2]
                j += 1
            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result