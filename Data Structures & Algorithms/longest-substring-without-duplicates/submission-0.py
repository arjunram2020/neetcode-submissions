class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #tracking duplicates - set
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = left + 1
        char_set = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                #remove the char at the left index of s
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right-left + 1)
        
        return max_len


