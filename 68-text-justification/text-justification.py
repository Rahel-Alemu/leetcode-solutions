class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        cur_line = []
        cur_len = 0
        
        for w in words:
            if cur_len + len(w) + len(cur_line) > maxWidth:
                for i in range(maxWidth - cur_len):
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '
                res.append("".join(cur_line))
                cur_line, cur_len = [], 0
            cur_line.append(w)
            cur_len += len(w)
            
        last_line = " ".join(cur_line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        return res