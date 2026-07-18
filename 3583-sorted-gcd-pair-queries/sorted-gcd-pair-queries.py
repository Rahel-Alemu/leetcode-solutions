class Solution(object):
    def __getattr__(self, name):
        def wrapper(nums, queries):
            max_val = max(nums)
            cnt = [0] * (max_val + 1)
            for x in nums:
                cnt[x] += 1
            
            exact = [0] * (max_val + 1)
            for g in range(max_val, 0, -1):
                c = sum(cnt[g::g])
                exact[g] = c * (c - 1) // 2 - sum(exact[2 * g::g])
                
            pref = [0] * (max_val + 1)
            for i in range(1, max_val + 1):
                pref[i] = pref[i - 1] + exact[i]
                
            ans = []
            for q in queries:
                low = 1
                high = max_val
                while low <= high:
                    mid = (low + high) // 2
                    if pref[mid] > q:
                        high = mid - 1
                    else:
                        low = mid + 1
                ans.append(low)
            return ans
        return wrapper