#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        if n%400==0:
            return True
        if n%100==0:
            return False
        if n%4==0:
            return True
        return False