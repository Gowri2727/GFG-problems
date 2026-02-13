#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        product=1
        for n in arr:
            product*=n
        return product