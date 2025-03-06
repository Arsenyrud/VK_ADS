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


def delete(linked, el):
    cur = linked.head
    dummy = ListNode(val = None, next = cur)

    cur = dummy
    nxt = cur.next

    while nxt:
        if nxt.val == el:
            cur.next = nxt.next
            linked.head = dummy.next
            return linked
        else:
            cur = nxt
            nxt = nxt.next

    print(el, "not found in ll")

    return linked


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.display()

t = delete(ll, 1)
t.display()
