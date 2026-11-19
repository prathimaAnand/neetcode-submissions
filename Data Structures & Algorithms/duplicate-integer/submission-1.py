class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return true
            unique.add(num)
        # then no duplicate, so return false
        return false