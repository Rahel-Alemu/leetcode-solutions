class Solution(object):
    def braceExpansionII(self, expression):
        s = expression

        def parse_seq(i):
            result = {""}
            while i < len(s) and s[i] not in ',}':
                if s[i] == '{':
                    term_set, i = parse_braces(i)
                else:
                    term_set = {s[i]}
                    i += 1
                result = {a + b for a in result for b in term_set}
            return result, i

        def parse_braces(i):
            i += 1  # skip '{'
            union_set = set()
            while True:
                part, i = parse_seq(i)
                union_set |= part
                if s[i] == ',':
                    i += 1
                else:  # '}'
                    i += 1
                    break
            return union_set, i

        result, _ = parse_seq(0)
        return sorted(result)