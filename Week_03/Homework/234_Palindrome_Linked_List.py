# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True

        # fast and slow ptr to get to middle
        # at each slow increment, store curr.val in a list
        # start at slow, check curr.val == list[backwards]

        lst = list()
        slow = head
        fast = head
        while fast and fast.next:
            lst.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            lst.append(slow.val)

        i = len(lst)-1
        while slow:
            if not slow.val == lst[i]:
                return False
            i -= 1
            slow = slow.next

        return True