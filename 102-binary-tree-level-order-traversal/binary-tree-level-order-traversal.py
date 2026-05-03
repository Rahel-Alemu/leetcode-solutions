import collections

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
            
        res = []
        queue = collections.deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            
        return res