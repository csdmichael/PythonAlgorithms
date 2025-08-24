import json
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        else:
            return self.divideAndConquer(lists, 0, len(lists) - 1)

    def divideAndConquer(self, lists: List[Optional[ListNode]], left, right) -> Optional[ListNode]:
        if (left == right):
            return lists[left]
        
        mid = left + (left - right) // 2
        l1 = self.divideAndConquer(lists, left, mid)
        l2 = self.divideAndConquer(lists, mid+1, right)

        return self.mergeLists(l1, l2)
    
    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            res = ListNode(l1.val)
            res.next = self.mergeLists(l1.next, l2)
            return res
        else:
            res = ListNode(l2.val)
            res.next = self.mergeLists(l1, l2.next)
            return res

x = [
        ListNode(3, ListNode(5)),
        ListNode(1, ListNode(4))
]
y = Solution.mergeKLists(x)
r = json.dumps(y)
print(r)