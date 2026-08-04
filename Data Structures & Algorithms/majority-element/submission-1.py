class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res
        
        # my_map = {}

        # for num in nums:
        #     if num not in my_map:
        #         my_map[num] = 1;
        #     else:
        #         my_map[num] +=1;
        
        # for key, value in my_map.items():
        #     if value > len(nums) // 2:
        #         return key
