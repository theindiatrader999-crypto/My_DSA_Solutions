# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        l=0
        temp_head=head
        t_head = head
        dummy_node=head


        while temp_head:
            l+=1
            temp_head=temp_head.next
        node_num=l-n
        cnt=1
        if node_num < cnt:
            return dummy_node.next

        while t_head:
            if cnt == node_num:
                t_head.next=t_head.next.next
                return head
            else:
                t_head=t_head.next
                cnt+=1
            


        

