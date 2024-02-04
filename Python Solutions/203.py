# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        _list = ListNode()
        new_ptr = _list
        head_ptr = head

        while head_ptr:
            if head_ptr.val != val:
                new_ptr.next = ListNode(head_ptr.val)
                new_ptr = new_ptr.next
            head_ptr = head_ptr.next 
        return _list.next