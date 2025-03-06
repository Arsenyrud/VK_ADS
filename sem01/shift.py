def reverse_from_to(nums, start, end):
    if start < 0 or end > len(nums) - 1:
        return -1
    l = start
    r = end
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums

def shift(nums, k):
    n = len(nums) - 1
    reverse_from_to(nums, 0, n-k)
    reverse_from_to(nums, n-k+1, n)
    reverse_from_to(nums, 0, n)

    return nums

lst = [1, 2, 3, 4, 5, 6, 7]
shift(lst, 3)
