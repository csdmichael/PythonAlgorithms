#Pattern: Fast / Slow Pointers

class LinkedListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def getMiddleElement(self, ll: LinkedListNode) -> int:
        middleIndex = 0
        if ll == None:
            return -1
        ptr1 = ll
        ptr2 = ll

        while ptr2 != None:
            ptr2 = ptr2.next
            if ptr2 != None:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
                middleIndex += 1
        print(f"Middle Index = {middleIndex}")
        return ptr1.val
    
i = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
y = Solution.getMiddleElement(Solution, i)
print(y)
