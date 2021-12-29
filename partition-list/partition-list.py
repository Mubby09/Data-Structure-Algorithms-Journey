# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_head = before_iteration = ListNode(0)
        # equal_head = equal_iteration = ListNode(0)
        after_head = after_iteration = ListNode(0)
        #Populates the 3 lists 
        while head:
            if head.val < x:
                #into the starting point of the linked list lesser than x.
                before_iteration.next = head
                before_iteration = before_iteration.next
            # elif head.val == x:
                #into the starting point of the linked list equal to x.
                # equal_iteration.next = head
                # equal_iteration = equal_iteration.next
            else:
                #into the starting point of the linked list greater than x.
                after_iteration.next = head
                after_iteration = after_iteration.next
        
            head = head.next
        #Combine all 3 lists.
        after_iteration.next = None
        # equal_iteration.next = after_head.next
        before_iteration.next = after_head.next
        # before_iteration.next = equal_head.next
        
        return before_head.next