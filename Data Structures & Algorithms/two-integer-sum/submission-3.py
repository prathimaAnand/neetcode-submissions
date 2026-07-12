class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums[i] - target = nums[j] => 3 - 7 = 4
        # guarentee to find a pair
        # not sorted != 2 pointers technique
        nums_map = {} # map value : index
        
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[nums[i]] = i
        


        # 2 pointers => left, right = left + right > 7 then right -- & vice versa
        
        # nums_len = len(nums)
        # l = 0
        # r = nums_len - 1

        # for i in range(nums_len - 1):
        #     if nums[l] + nums[r] == target:
        #         return [l, r]
        #     elif nums[l] + nums[r] > target:
        #         r = r - 1
        #     elif nums[l] + nums[r] < target:
        #         l = l + 1
            