#User function Template for python3

class Solution:
    def isFactorial (self, N):
        # code here
        fact = 1
        i = 1

        while fact < N:
            i += 1
            fact *= i

        if fact == N:
            return 1
        return 0