class Solution(object):
    def validSequence(self, word1, word2):
        n1 = len(word1)
        m = len(word2)

        e = [0] * (n1 + 1)
        j = m
        for i in range(n1 - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            e[i] = m - j

        s = [0] * (n1 + 1)
        for i in range(n1 - 1, -1, -1):
            se = s[i + 1]
            if se < m and word1[i] == word2[m - 1 - se]:
                opt1 = se + 1
            else:
                opt1 = se
            ee = e[i + 1]
            opt2 = ee + 1 if ee < m else ee
            s[i] = opt1 if opt1 > opt2 else opt2

        result = []
        i = 0
        jj = 0
        used = False
        while jj < m and i < n1:
            if used:
                if word1[i] == word2[jj]:
                    result.append(i)
                    jj += 1
                i += 1
            else:
                if word1[i] == word2[jj]:
                    if s[i + 1] >= m - jj - 1:
                        result.append(i)
                        jj += 1
                        i += 1
                    else:
                        i += 1
                else:
                    if e[i + 1] >= m - jj - 1:
                        result.append(i)
                        jj += 1
                        i += 1
                        used = True
                    else:
                        i += 1

        if jj < m:
            return []
        return result