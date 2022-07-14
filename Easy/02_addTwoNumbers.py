# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryValue = 0
        result = ListNode(0)
        pointer = result
        
        while (l1 or l2 or carryValue):
            
            firstNum = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0
            summation = firstNum + secondNum + carryValue
            num = summation % 10
            carryValue = summation // 10
            
            pointer.next = ListNode(num)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next