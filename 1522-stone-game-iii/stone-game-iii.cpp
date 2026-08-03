class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            int best = INT_MIN;
            int s = 0;
            for (int k = 1; k <= 3; k++) {
                if (i + k > n) break;
                s += stoneValue[i + k - 1];
                best = max(best, s - dp[i + k]);
            }
            dp[i] = best;
        }
        if (dp[0] > 0) return "Alice";
        else if (dp[0] < 0) return "Bob";
        else return "Tie";
    }
};