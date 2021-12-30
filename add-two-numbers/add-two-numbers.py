# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode()
        current_answer = dummy_head
        carry = 0
        while l1 or l2:
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            current_answer.next = ListNode(val % 10)
            carry = val // 10
            current_answer = current_answer.next
        if carry == 1:
            current_answer.next = ListNode(carry)
            
        return dummy_head.next
            
        