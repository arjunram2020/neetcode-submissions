class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter #for frequency of letters
        #do a sliding window
        #for every window, 1st check the maximum occuring letter in the window
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        #how to adjust the window though... 
        #check if the windor is valid... otherwise keep adjusting left...
        #every iteration, change right until right is all the way to the right
        left = 0
        right = 1
        #have a hashset storing all the frequencies for all letters.... add or delete
        frequencies = Counter()
        length = 0
        max_len = 0
        for right in range (len(s)):
            frequencies[s[right]] += 1
            length += 1


            max_freq = max(frequencies.values())

            while length - max_freq > k:
                frequencies[s[left]]-=1
                length-=1
                left+=1

            max_len = max(length, max_len)
        return max_len
            
