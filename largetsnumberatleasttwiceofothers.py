def twice(nums):

    if len(nums) == 1:
        return 0
    largest = max(nums)
    index = nums.index(largest)
    nums.remove(largest)
    second = max(nums)
    if largest >= 2 * second:
        return index
    else:
        return -1
    
n = [3, 6, 1, 0]
print(twice(n))