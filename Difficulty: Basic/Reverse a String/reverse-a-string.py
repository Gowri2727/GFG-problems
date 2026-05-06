#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        if len(s)<=1:
            return s
        else:
            return s[::-1]