def sort_zero(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        if not nums[r]:
            if nums[l]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if not nums[l]:
                l += 1
        else:
            r -= 1

    return nums

lst = [0, 1, 0, 1, 0, 0, 1]

