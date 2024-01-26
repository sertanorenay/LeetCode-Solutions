# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next     
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _list = current  = ListNode()
        node1, node2 = l1, l2
        carry = 0

        while node1 or node2 or carry:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            _sum = val1 + val2 + carry
            carry = _sum // 10
            current.next = ListNode(_sum % 10)
            current = current.next

            if node1: node1 = node1.next
            if node2: node2 = node2.next
        return _list