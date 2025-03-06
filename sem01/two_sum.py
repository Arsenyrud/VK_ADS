def two_sum(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return (l, r)
    return (-1, -1)

lst = [1, 4, 9, 16, 25, 36, 40]
target = 44
