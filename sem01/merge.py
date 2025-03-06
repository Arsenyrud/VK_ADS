def merge(lst1, lst2):
    nums = []
    l = 0
    r = 0

    while l < len(lst1) and r < len(lst2):
        if lst1[l] < lst2[r]:
            nums.append(lst1[l])
            l += 1
        else:
            nums.append(lst2[r])
            r += 1
    if l == len(lst1):
        nums += lst2[r:]
    else:
        nums += lst1[l:]

    return nums

lst1 = [1, 4, 9, 25, 3]
lst2 = [1, 8, 27]

merge(lst1, lst2)
