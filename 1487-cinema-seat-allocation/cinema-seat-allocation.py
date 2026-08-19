class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        row_masks = {}
        for row, seat in reservedSeats:
            row_masks[row] = row_masks.get(row, 0) | (1 << seat)

        blockA = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        blockB = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        blockC = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        ans = 2 * (n - len(row_masks))
        for mask in row_masks.values():
            if (mask & blockA) == 0 and (mask & blockC) == 0:
                ans += 2
            elif (mask & blockA) == 0 or (mask & blockB) == 0 or (mask & blockC) == 0:
                ans += 1
        return ans