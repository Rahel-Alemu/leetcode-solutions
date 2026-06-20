class Solution(object):
    def largestAltitude(self, gain):
        max_alt = 0
        curr_alt = 0
        for g in gain:
            curr_alt += g
            if curr_alt > max_alt:
                max_alt = curr_alt
        return max_alt