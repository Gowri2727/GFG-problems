class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        if not k in arr:
            return -1
        n=len(arr)-1
        for idx in range(n):
            if k==arr[idx]:
                return idx