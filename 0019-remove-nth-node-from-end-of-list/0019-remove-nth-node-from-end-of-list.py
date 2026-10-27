# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        fast_node=head
        cnt= 0
        while cnt != n:
            fast_node=fast_node.next
            cnt+=1
        if not fast_node:
            return head.next
        slow_node=head
        while fast_node.next:
            slow_node=slow_node.next
            fast_node=fast_node.next
        slow_node.next=slow_node.next.next
        return head



        