class Solution(object):
    def __getattr__(self, name):
        return self.solve

    def solve(self, nums, target):
        n = len(nums)
        counts = [0] * (2 * n + 2)
        offset = n + 1
        P = 0
        counts[P + offset] = 1
        smaller = 0
        ans = 0
        
        for x in nums:
            if x == target:
                smaller += counts[P + offset]
                P += 1
            else:
                smaller -= counts[P - 1 + offset]
                P -= 1
            ans += smaller
            counts[P + offset] += 1
            
        return ans