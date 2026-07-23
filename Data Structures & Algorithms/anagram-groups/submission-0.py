class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq of chars
        output = defaultdict(list) # special dict automatically creates empty list 
        
        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord("a")] += 1

            output[tuple(freq)].append(s)
        return list(output.values())
