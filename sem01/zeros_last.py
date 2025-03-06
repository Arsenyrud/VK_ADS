def zeros_last(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        if not nums[l]:
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
            else:
                r -= 1
        else:
            l += 1
    return nums

lst = [0, 0, 0, 1]
zeros_last(lst)

