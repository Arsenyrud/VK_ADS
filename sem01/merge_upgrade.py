def merge(lst1, lst2):
    l1 = len(lst1) - len(lst2) - 1
    l2 = len(lst2) - 1
    l3 = len(lst1) - 1
    
    while l1 >= 0 and l2 >= 0:
        if lst1[l1] > lst2[l2]:
            lst1[l3] = lst1[l1]
            l3 -= 1
            l1 -= 1
        else:
            lst1[l3] = lst2[l2]
            l3 -= 1
            l2 -= 1

    if l2 < 0:
        while l1 >= 0:
            lst1[l3] = lst1[l1]
            l3 -= 1
            l1 -= 1
    else:
        while l2 >= 0:
            lst1[l3] = lst2[l2]
            l3 -= 1
            l2 -= 1
    
    return lst1
        

ls1 = [10, 17, 115, 0, 0, 0]
ls2 = [13, 114, 116]

merge(ls1, ls2)
