class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        cnt = [0] * k
        for num in nums:
            r = num % k
            new_cnt = [0] * k
            for x in range(k):
                if cnt[x]:
                    new_cnt[(x * r) % k] += cnt[x]
            new_cnt[r] += 1
            cnt = new_cnt
            for y in range(k):
                result[y] += cnt[y]
        return result