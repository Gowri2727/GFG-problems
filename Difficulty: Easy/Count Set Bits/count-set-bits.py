#User function Template for python3
class Solution:
	def setBits(self, n):
		setBits=0
		while(n>0):
		    n=n&(n-1)
		    setBits+=1
        return setBits