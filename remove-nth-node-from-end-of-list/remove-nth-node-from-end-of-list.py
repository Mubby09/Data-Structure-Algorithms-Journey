# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0, head)
        first = dummy_head.next
        
        for _ in range(n):
            first = first.next
            
        second = dummy_head
        while first:
            first, second = first.next, second.next
            
        second.next = second.next.next
        return dummy_head.next
            