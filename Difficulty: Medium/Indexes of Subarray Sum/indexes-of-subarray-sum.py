#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        l=0
        currsum=0
        for r in range(len(arr)):
            currsum+=arr[r]
            while currsum>target:
                currsum-=arr[l]
                l+=1
            if currsum==target:
                return[l+1,r+1]
        return [-1]