class Solution(object):
    def maxIceCream(self, costs, coins):
        max_val = max(costs)
        freq = [0] * (max_val + 1)
        for c in costs:
            freq[c] += 1
            
        res = 0
        for i in range(1, max_val + 1):
            if freq[i] > 0:
                take = min(freq[i], coins // i)
                res += take
                coins -= take * i
                if coins < i:
                    break
        return res

    def maxNumberOfBalloons(self, text):
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2
        o = text.count('o') // 2
        n = text.count('n')
        return min(b, a, l, o, n)