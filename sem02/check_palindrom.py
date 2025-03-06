from collections import deque

lst1 = ['a']
lst2 = ['b', 'a', 'b', 'c', 'b']

def check_palindrom(str1):
    heap = deque('')
    for i in range(len(str1)//2):
        heap.append(str1[i])
        heap.appendleft(str1[len(str1) - 1 - i])

    while len(heap) > 0:
        if heap.pop() != heap.popleft():
            return False
    return True

check_palindrom(lst1)
