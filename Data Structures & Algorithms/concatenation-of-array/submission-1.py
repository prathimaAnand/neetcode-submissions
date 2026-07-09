class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2): # loops twice
            for num in nums:
                ans.append(num) # add each number
        return ans