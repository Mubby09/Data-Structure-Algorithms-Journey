# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous_node = None
        while head:
            next = head.next
            head.next = previous_node
            previous_node = head
            head = next
        return previous_node
        