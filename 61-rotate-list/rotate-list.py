class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
            
        last.next = head
        
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head