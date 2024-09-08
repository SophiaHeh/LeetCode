class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #prev, curr = None, head
        #while curr:
        #    next = curr.next #temporary variable 
        #    curr.next = prev
        #    prev = curr
        #    curr = next
        #return prev

        #recursive solution 
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next  = prev
                return reverse(next, cur)
        return reverse(head, None)
        
