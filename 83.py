# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        _list = ListNode()
        current = _list
        current.val = head.val
        ptr = head
        while ptr.next:
            if ptr.val != ptr.next.val:
                current.next = ListNode(ptr.next.val)
                current = current.next
            ptr = ptr.next
        return _list