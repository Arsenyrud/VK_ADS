def even_first(nums):
    l = 0
    r = 1

    while r < len(nums):
        nums[l], nums[r] = nums[r], nums[l] 
        if nums[r] & 1:
            r += 1
        if not nums[l] & 1:
            l += 1
        
    return nums

lst = [4, 3, 2, 4, 1, 11, 8, 9]
transfer(lst)
