def pivotindex(nums):

    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

nums = [1, 7, 3, 6, 5, 6]
print(pivotindex(nums))


def pivotindex1(nums):
    left , right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1

nums = [1, 7, 3, 6, 5, 6]
print(pivotindex1(nums))
