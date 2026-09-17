class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        best_end = [INF] * n 

        left = 0
        curr_sum = 0
        best_so_far = INF
        result = INF

        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == target:
                length = right - left + 1
                if left > 0 and best_end[left - 1] != INF:
                    result = min(result, length + best_end[left - 1])
                best_so_far = min(best_so_far, length)
            best_end[right] = best_so_far

        return result if result != INF else -1