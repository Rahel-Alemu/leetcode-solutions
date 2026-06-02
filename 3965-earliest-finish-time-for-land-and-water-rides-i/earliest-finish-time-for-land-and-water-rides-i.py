class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                ans = min(ans, max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j])
                ans = min(ans, max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i])
        return ans