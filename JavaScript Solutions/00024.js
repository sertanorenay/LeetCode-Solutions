/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if (head == null || head.next == null) {
        return head;
    }

    let dummy = new ListNode(0, head);
    let pointer = dummy

    while (pointer.next != null && pointer.next.next != null) {
        let first = pointer.next;
        let second = pointer.next.next;

        pointer.next = second;
        first.next = second.next;
        second.next = first;

        pointer = first;
    }

    return dummy.next;
};
