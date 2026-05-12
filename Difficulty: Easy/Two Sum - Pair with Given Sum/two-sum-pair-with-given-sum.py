class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()
		left=0
		right=len(arr)-1
		while left<right:
		    mid=(arr[left]+arr[right])
		    if mid<target:
		        left+=1
		    elif mid==target:
		        return True
		    else:
		        right-=1
		return False