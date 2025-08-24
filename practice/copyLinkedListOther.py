class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.other = None

def copy_linked_list(head):
    if head is None:
        return None

    # Create a mapping from original nodes to their copies
    old_to_new = {}
    current = head
    while current:
        old_to_new[current] = LinkedListNode(current.value)
        current = current.next

    # Set the next and other pointers for the copied nodes
    current = head
    while current:
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        if current.other:
            old_to_new[current].other = old_to_new[current.other]
        current = current.next

    return old_to_new[head]


