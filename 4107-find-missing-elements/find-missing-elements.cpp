class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int lo = *min_element(nums.begin(), nums.end());
        int hi = *max_element(nums.begin(), nums.end());
        unordered_set<int> present(nums.begin(), nums.end());
        vector<int> result;
        for (int i = lo; i <= hi; i++) {
            if (!present.count(i)) result.push_back(i);
        }
        return result;
    }
};