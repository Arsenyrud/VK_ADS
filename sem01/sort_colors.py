def sort_colors(nums):
    l1 = 0
    l2 = 0
    l3 = len(nums) - 1

    while l2 <= l3:
            if nums[l2] == 2:
                nums[l2], nums[l3] = nums[l3], nums[l2]
                l3 -= 1
            if nums[l2] == 0:
                nums[l2], nums[l1] = nums[l1], nums[l2]
                l2 += 1
                l1 += 1
            if nums[l2] == 1:
                l2 += 1
        
    return nums


nums = [2, 1, 0, 2, 0, 2, 1, 1, 0]
sort_colors(nums)
