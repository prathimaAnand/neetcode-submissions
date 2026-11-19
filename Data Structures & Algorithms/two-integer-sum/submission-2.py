class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 pointers => left, right = left + right > 7 then right -- & vice versa
        # nums[i] - target = nums[j] => 3 - 7 = 4
        nums_len = len(nums)
        l = 0
        r = nums_len - 1

        for i in range(nums_len - 1):
            if nums[l] + nums[r] == target:
                return [l, r]
            elif nums[l] + nums[r] > target:
                r = r - 1
            elif nums[l] + nums[r] < target:
                l = l + 1
            