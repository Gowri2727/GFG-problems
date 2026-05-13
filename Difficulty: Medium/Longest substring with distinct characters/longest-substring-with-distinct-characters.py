class Solution:
   def longestUniqueSubstr(self, s):
        # code here
        freq = {}
        left = 0
        maxLength = 0
        
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right-left+1)
        return maxLength