class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp