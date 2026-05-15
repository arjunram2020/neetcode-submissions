class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        #for us to actually start this method, we have to make s2 greater than or equal to s1, check for s2 < s1
        if len(s2) < len(s1):
            return False
        #fixed sliding window... 
        #now we know that len s2 is greater than len s1
        left = 0
        right = len(s1)
        freq = Counter(s2[left:right]) #substring dictionary
        s1_freq = Counter(s1) #s1 dictionary
        #check here to see if there is permutation - how to put that logic...?
        if freq == s1_freq:
            return True
        for right in range(len(s1), len(s2)):
            #now we have the substring, check if that is a permutation of s1
            freq[s2[left]] -= 1
            freq[s2[right]] += 1
            left += 1
            right += 1
            if freq == s1_freq:
                return True
        return False

        
