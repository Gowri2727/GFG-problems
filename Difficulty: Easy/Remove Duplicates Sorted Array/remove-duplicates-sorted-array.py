class Solution:
    def removeDuplicates(self, arr):
        # code here
        ans=set(arr)
        return sorted(ans)