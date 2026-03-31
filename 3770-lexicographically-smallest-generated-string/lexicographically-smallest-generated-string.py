class Solution:
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        word = ['?'] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                        fixed[i + j] = True
                    else:
                        return ""

        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                if match:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            for c in "abcdefghijklmnopqrstuvwxyz":
                                if c != str2[j]:
                                    word[pos] = c
                                    changed = True
                                    break
                            if changed:
                                break
                    if not changed:
                        return ""

        return "".join(word)