class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        n = len(vals)
        positions = []
        for i in range(1, n - 1):
            if (vals[i] > vals[i - 1] and vals[i] > vals[i + 1]) or (vals[i] < vals[i - 1] and vals[i] < vals[i + 1]):
                positions.append(i)

        if len(positions) < 2:
            return [-1, -1]

        max_distance = positions[-1] - positions[0]
        min_distance = min(positions[k + 1] - positions[k] for k in range(len(positions) - 1))

        return [min_distance, max_distance]