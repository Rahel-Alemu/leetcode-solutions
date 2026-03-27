class Solution:
    def areSimilar(self, mat, k):
        n = len(mat[0])
        k %= n
        if k == 0:
            return True
        
        for row in mat:
            for j in range(n):
                if row[j] != row[(j + k) % n]:
                    return False
        return True