/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode current = head;
        int length = 1;

        while (current.next != null) {
            current = current.next; 
            length++;
        }

        current = head;
        ListNode newHead = current;

        if (length - n == 0) return head.next; 

        for (int i = 1; i < length; i++) {
            if (i == length - n) {
                if (n == 1) current.next = null;
                else current.next = current.next.next;
            }
            current = current.next;
        }

        return newHead;
    }
}
