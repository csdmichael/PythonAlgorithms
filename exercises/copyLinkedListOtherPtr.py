class ListNode:
    def __init__(self, val, next = None, other = None):
        self.val = val
        self.next = next
        self.other = other

class LinkedList:
    def __init__(self, head):
        self.head = head

    def copy(self):
        hash = {}
        ptr = self.head
        while ptr:
            hash[ptr] = ListNode(ptr)
            ptr = ptr.next
        
        for key, value in hash.items():
            value.val = key.val
            if key.next:
                value.next = hash[key.next]
            if key.other:
                value.other = hash[key.other]
        
        dc = LinkedList(hash[self.head])

        return dc



Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

Node1.other = Node3
Node2.other = Node2
Node4.other = Node3

x = LinkedList(Node1)


y = x.copy()

ptr = y.head
while ptr:
    print(f"val = {ptr.val}, next = {ptr.next}, other = {ptr.other}")
    ptr = ptr.next
