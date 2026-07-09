class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s, count_t = {}, {}
        # if length does not match then its clearly not an anagram
        if len(s) != len(t):
            return False
        
        # store variable as the key and count as value
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

            # if both hash map matches, its a anagram
        return count_s == count_t