class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        key = lambda x: (sum(int(d) for d in str(x)), x)
        target_pos = {v: i for i, v in enumerate(sorted(nums, key=key))}
        perm = [target_pos[v] for v in nums]
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = perm[j]
        return n - cycles