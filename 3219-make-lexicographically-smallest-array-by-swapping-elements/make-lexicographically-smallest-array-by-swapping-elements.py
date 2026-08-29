class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        indexed = sorted(range(n), key=lambda i: nums[i])

        groups = []
        current_group = [indexed[0]]
        for k in range(1, n):
            prev_idx = indexed[k - 1]
            curr_idx = indexed[k]
            if nums[curr_idx] - nums[prev_idx] <= limit:
                current_group.append(curr_idx)
            else:
                groups.append(current_group)
                current_group = [curr_idx]
        groups.append(current_group)

        result = [0] * n
        for group in groups:
            sorted_indices = sorted(group)
            sorted_values = sorted(nums[i] for i in group)
            for idx, val in zip(sorted_indices, sorted_values):
                result[idx] = val

        return result