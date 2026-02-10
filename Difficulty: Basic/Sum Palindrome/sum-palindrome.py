#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # code here 
        def is_palindrome(x):
            return str(x) == str(x)[::-1]

        for _ in range(5):
            if is_palindrome(n):
                return n

            rev = int(str(n)[::-1])
            n = n + rev

            if is_palindrome(n):
                return n

        return -1