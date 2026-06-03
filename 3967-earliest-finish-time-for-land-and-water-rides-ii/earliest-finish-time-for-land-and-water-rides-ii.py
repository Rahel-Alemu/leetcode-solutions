class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_L_finish = min(landStartTime[i] + landDuration[i] for i in range(len(landStartTime)))
        ans1 = min(max(min_L_finish, waterStartTime[j]) + waterDuration[j] for j in range(len(waterStartTime)))
        
        min_W_finish = min(waterStartTime[j] + waterDuration[j] for j in range(len(waterStartTime)))
        ans2 = min(max(min_W_finish, landStartTime[i]) + landDuration[i] for i in range(len(landStartTime)))
        
        return min(ans1, ans2)