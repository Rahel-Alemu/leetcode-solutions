class Solution {
    const long long MOD = 1e9 + 7;
    vector<vector<long long>> C;

    long long count(vector<int>& arr) {
        int n = arr.size();
        if (n <= 2) return 1;
        vector<int> l, r;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[0]) l.push_back(arr[i]);
            else r.push_back(arr[i]);
        }
        return C[n - 1][l.size()] * count(l) % MOD * count(r) % MOD;
    }

public:
    int numOfWays(vector<int>& nums) {
        int n = nums.size();
        C.assign(n + 1, vector<long long>(n + 1, 0));
        for (int i = 0; i <= n; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
        return (count(nums) - 1 + MOD) % MOD;
    }
};