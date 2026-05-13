#User function Template for python3
from itertools import combinations
class Solution:
    def threeSum(self, arr, t):
        # Your code here
        y = combinations(arr, 3)
        z = []
        for i in y:
            if t == sum(i):
                z.append(sorted(i))
        return z