from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    nums_sum = 0
    for ele in nums:
        nums_sum += ele
    return nums_sum

def get_min(nums: List[int]) -> int:
    nums_min = nums[0]
    for i in range(len(nums)):
        nums_min = min(nums[i], nums_min)
    return nums_min

def get_max(nums: List[int]) -> int:
    nums_max = nums[0]
    for i in range(len(nums)):
        nums_max = max(nums[i], nums_max)
    return nums_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
