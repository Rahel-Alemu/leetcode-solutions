class Solution(object):
    def __getattr__(self, name):
        def wrapper(nums):
            def get_gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            
            prefixGcd = []
            mxi = 0
            for num in nums:
                if num > mxi:
                    mxi = num
                prefixGcd.append(get_gcd(num, mxi))
            
            prefixGcd.sort()
            ans = 0
            i = 0
            j = len(prefixGcd) - 1
            while i < j:
                ans += get_gcd(prefixGcd[i], prefixGcd[j])
                i += 1
                j -= 1
            return ans
        return wrapper