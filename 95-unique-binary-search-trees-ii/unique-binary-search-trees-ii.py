class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            
            res = []
            for i in range(start, end + 1):
                left_nodes = build(start, i - 1)
                right_nodes = build(i + 1, end)
                
                for l in left_nodes:
                    for r in right_nodes:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
            
        return build(1, n)