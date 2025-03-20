# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return
        
        # find middle of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        revcurr = slow.next
        prev = None
        while revcurr:
            nextnode = revcurr.next
            revcurr.next = prev
            prev = revcurr
            revcurr = nextnode
        reverse = prev
        slow.next = None

        # insert each element of reversed into the first half of head
        curr = head
        while reverse:
            currtemp = curr.next
            revtemp = reverse.next

            curr.next = reverse
            reverse.next = currtemp

            curr = currtemp
            reverse = revtemp