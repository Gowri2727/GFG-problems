class Solution:
    def isPalindrome(self, n):
		# code here
		s=str(n)
		if s==s[::-1]:
		    return True