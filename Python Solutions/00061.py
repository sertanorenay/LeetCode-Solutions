# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k is 0: 
            return head

        left = dummy_left = ListNode()
        right = dummy_right = ListNode()

        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1

        if length is 0: 
            return head
        
        count = 0
        ptr = head
        k %= length
        while ptr:    
            if count >= length - k:
                left.next = ListNode(ptr.val)
                left = left.next
            else:
                right.next = ListNode(ptr.val)
                right = right.next
            ptr = ptr.next
            count += 1

        left.next = dummy_right.next 
        return dummy_left.next