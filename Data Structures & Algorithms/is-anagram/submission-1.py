class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # is s = t?, if not return false
        if (len(s) != len(t)):
            return False

        # 1. Sort and compare elements in s with t, if one of it not same return true
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_t[i] != sorted_s[i]:
                return False
        
        return True