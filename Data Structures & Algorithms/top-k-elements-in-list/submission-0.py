class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        # key = number and value = freq
        """ 
        nums = [9, 8, 8, 6, 6, 6]
        key/num:value/count
        9 : 1
        8 : 2
        6 : 3
        """
        # add everything to hashmap 
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # add to array
        for n, c in count.items():
            arr[c].append(n)
        res = []
        # trase arr in reverse order
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res