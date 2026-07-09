class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting method - space: O(s + t) time: O(n log n)
        '''if (len(s) != len(t)):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_t[i] != sorted_s[i]:
                return False
        
        return True'''

        # Using hash maps - space: O(s + t) time: O(n)
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        # store key as char and value as count
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        if count_s != count_t:
            return False
        else:
            return True
