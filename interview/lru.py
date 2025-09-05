class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = None
        self.hashMap = {}

    def get(self, k) -> int:
        if k not in self.hashMap:
            return None
        else:
            
        