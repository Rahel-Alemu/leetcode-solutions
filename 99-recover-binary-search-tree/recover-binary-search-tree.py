class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            
            if node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            
            traverse(node.right)
            
        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val