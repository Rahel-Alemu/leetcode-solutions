class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        res = 0
        p1 = head
        p2 = prev
        while p2:
            if p1.val + p2.val > res:
                res = p1.val + p2.val
            p1 = p1.next
            p2 = p2.next
            
        return res