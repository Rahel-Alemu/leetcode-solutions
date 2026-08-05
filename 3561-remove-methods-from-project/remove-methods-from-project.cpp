class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);
        for (auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        vector<bool> suspicious(n, false);
        suspicious[k] = true;
        stack<int> st;
        st.push(k);
        while (!st.empty()) {
            int u = st.top(); st.pop();
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    st.push(v);
                }
            }
        }

        for (auto& inv : invocations) {
            int a = inv[0], b = inv[1];
            if (suspicious[b] && !suspicious[a]) {
                vector<int> all(n);
                for (int i = 0; i < n; i++) all[i] = i;
                return all;
            }
        }

        vector<int> result;
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) result.push_back(i);
        }
        return result;
    }
};