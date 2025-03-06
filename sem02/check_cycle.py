class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()

def check_cycle(linked):
    slow = fast = linked.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False


check_cycle(ll)
