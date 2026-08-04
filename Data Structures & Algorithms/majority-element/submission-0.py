class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}

        for num in nums:
            if num not in my_map:
                my_map[num] = 1;
            else:
                my_map[num] +=1;
        
        for key, value in my_map.items():
            if value > len(nums) // 2:
                return key
