class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        best = 0
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                count = 0
                for i in range(n):
                    ni = i + dx
                    if ni < 0 or ni >= n:
                        continue
                    for j in range(n):
                        nj = j + dy
                        if nj < 0 or nj >= n:
                            continue
                        if img1[i][j] == 1 and img2[ni][nj] == 1:
                            count += 1
                if count > best:
                    best = count
        return best