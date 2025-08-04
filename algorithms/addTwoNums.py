# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res: Optional[ListNode] = None
        reminder = 0
        resPtr = None
        ptr1 = l1
        ptr2 = l2
        while ptr1 != None or ptr2 != None:
            if ptr1 == None:
                val1 = 0
            else:
                val1 = ptr1.val
            if ptr2 == None:
                val2 = 0
            else:
                val2 = ptr2.val
            sum = val1 + val2 + reminder
            if sum < 10:
                reminder = 0
            else:
                reminder = 1
            val = sum % 10
            
            if res == None:
                res = ListNode(val)
                resPtr = res
            else:
                resPtr.next = ListNode(val)
                resPtr = resPtr.next
            if ptr1 != None:
                ptr1 = ptr1.next
            
            if ptr2 != None:
                ptr2 = ptr2.next

        if reminder == 1:
            resPtr.next = ListNode(reminder)
        return res
    
l1 = ListNode(2,
        ListNode(4, 
            ListNode(3))
)

l2 = ListNode(5,
        ListNode(6, 
            ListNode(4))
)

l1 = ListNode(9,
        ListNode(9, 
            ListNode(9))
)

l2 = ListNode(9)


y = Solution.addTwoNumbers(Solution, l1, l2)
#print(ser._serialize(y))
ptr = y
while ptr != None:
    print(ptr.val)
    ptr = ptr.next