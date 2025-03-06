from collections import deque

lst1 = ['a', 'b', 'c']
lst2 = ['b', 'a', 'b', 'c', 'b']

def check_strings(str1, str2):
    heap = deque('')
    for i in lst1:
        heap.append(i)

    i = len(str2) - 1
    while i >= 0 and len(heap):
        a = heap.pop()
        if a != lst2[i]:
            heap.append(a)
        i -= 1
    return not(len(heap))

check_strings(lst1, lst2)
