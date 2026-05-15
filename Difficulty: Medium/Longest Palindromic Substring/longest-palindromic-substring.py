class Solution:
    def getLongestPal(self, s):
        # code here
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                rev = s[j:j+i]
                
                if rev == rev[::-1]:
                    return rev