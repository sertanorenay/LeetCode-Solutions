# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:

        new_list = ListNode()
        dummy = new_list
        l1, l2 = list1, list2

        while l1 or l2:
            if l1 and l2:  
                if l1.val <= l2.val:
                    dummy.next = ListNode(l1.val)
                    l1 = l1.next
                else: 
                    dummy.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next
        return new_list.next