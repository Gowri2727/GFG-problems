#User function Template for python3

class Solution:
    def checkBinary (self, s):
        # Your code here
        one_seen = False
        zero_after_one = False

        for ch in s:
            if ch == '1':
                if zero_after_one:
                    return False
                one_seen = True
            else:  # ch == '0'
                if one_seen:
                    zero_after_one = True

        return True