class Solution {
public:
    int sortableIntegers(vector<int>& nums) {
        int n = nums.size();
        long long total = 0;
        for (int k = 1; k <= n; k++) {
            if (n % k) continue;
            bool ok = true;
            int prevMax = 0;
            for (int s = 0; s < n && ok; s += k) {
                int desc = 0, mn = INT_MAX, mx = 0;
                for (int i = 0; i < k; i++) {
                    int a = nums[s + i], b = nums[s + (i + 1) % k];
                    if (a > b) desc++;
                    mn = min(mn, a);
                    mx = max(mx, a);
                }
                if (desc > 1 || mn < prevMax) ok = false;
                prevMax = mx;
            }
            if (ok) total += k;
        }
        return (int)total;
    }
};