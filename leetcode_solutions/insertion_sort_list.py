# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next:
            return head
        dummy = ListNode(0)
        curr = head

        while curr:
            
            next_node = curr.next
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                prev = prev.next 

            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next