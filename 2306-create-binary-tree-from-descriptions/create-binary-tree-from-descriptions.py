class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()
        
        for p, c, isL in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
                
            if isL:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
                
            children.add(c)
            
        for p in nodes:
            if p not in children:
                return nodes[p]