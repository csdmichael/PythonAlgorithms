class DoubleLinkedListNode:
    def __init__(self, val: int, previous = None, next = None):
        self.val = val
        self.previous = previous
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLinkedListNode(0)
        self.tail = DoubleLinkedListNode(0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def append(self, val: int)->DoubleLinkedListNode:
        newNode = DoubleLinkedListNode(val, self.tail.previous, self.tail)
        self.tail.previous = newNode
        newNode.previous.next = newNode
        return newNode

    def removeFirst(self) -> int:
        if self.head.next == self.tail:
            return False
        else:
            toDelete = self.head.next
            self.head.next = toDelete.next
            toDelete.next.previous = self.head
            nodeVal = toDelete.val
            del toDelete
            return nodeVal

    def remove(self, node: DoubleLinkedListNode)->int:
        node.next.previous = node.previous
        node.previous.next = node.next
        nodeVal = node.val
        del node
        return nodeVal

class LRUCache:
    def __init__(self, capacity):
        self.cache = DoubleLinkedList()
        self.hash = {}
        self.capacity = capacity

    def add(self, val):
        if val in self.hash:
            self.cache.remove(self.hash[val])
            del self.hash[val]
        
        if len(self.hash) == self.capacity:
            firstNodeVal = self.cache.removeFirst()
            del self.hash[firstNodeVal]
        
        node = self.cache.append(val)
        self.hash[val] = node
        print(self.hash)

    def get(self, val) -> bool:
        if val in self.hash:
            self.cache.remove(self.hash[val])
            node = self.cache.append(val)
            self.hash[val] = node
            return True
        else:
            return False
        
c = LRUCache(3)

c.add(5)
c.add(6)
c.add(8)
c.add(5)
c.add(12)
isFive = c.get(5)
print(f"isFive={isFive}")
isSix = c.get(6)
print(f"isSix={isSix}")