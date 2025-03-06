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


ll1 = LinkedList()
ll1.append(1)
ll1.append(4)
ll1.append(9)
ll1.append(16)
ll1.append(25)

ll1.display()

ll2 = LinkedList()
ll2.append(8)
ll2.append(27)
ll2.append(64)
ll2.append(125)

ll2.display()



def merge_sorted_arrays(linked1, linked2):
    dummy = ListNode(val=None)
    tail = dummy
    l = linked1.head
    r = linked2.head

    while l and r:
        if l.val < r.val:
            tail.next = l
            l = l.next
        else:
            tail.next = r
            r = r.next
        tail = tail.next

    tail.next = l if l else r

    linked1.head = dummy.next
    return linked1

