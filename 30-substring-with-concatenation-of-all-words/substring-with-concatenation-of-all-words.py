from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)
        target_counts = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0
            
            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len
                
                if word in target_counts:
                    current_counts[word] += 1
                    count += 1
                    
                    while current_counts[word] > target_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        result.append(left)
                else:
                    current_counts.clear()
                    count = 0
                    left = right
                    
        return result