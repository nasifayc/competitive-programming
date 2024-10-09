# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, arr, start, end):
        if start >= end:
            return arr[start]
        
        mid = (start + end) // 2
        left = self.mergeSort(arr, start, mid)
        right = self.mergeSort(arr, mid + 1, end)
        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 < val2:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1: current.next = l1
        if l2: current.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        return self.mergeSort(lists,0, len(lists) - 1)
        