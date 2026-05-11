#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        s=str(n)
        result=0
        for i in range(len(s)):
            digits=int(s[i])
            result+=digits**3
        if n==result:
            return True