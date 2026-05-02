class Solution:
    def simplifyPath(self, path):
        stack = []
        parts = path.split("/")
        
        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or not part:
                continue
            else:
                stack.append(part)
                
        return "/" + "/".join(stack)