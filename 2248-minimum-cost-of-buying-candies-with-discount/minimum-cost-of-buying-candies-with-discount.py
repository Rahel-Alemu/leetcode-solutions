class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True

    def minimumCost(self, cost):
        cost.sort(reverse=True)
        res = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                res += cost[i]
        return res