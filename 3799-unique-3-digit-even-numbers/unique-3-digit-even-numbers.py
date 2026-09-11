from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        results = set()
        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                num = perm[0] * 100 + perm[1] * 10 + perm[2]
                results.add(num)
        return len(results)