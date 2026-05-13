class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        n=len(arr)
        for i in range(n):
            low=i+1
            high=n-1
            while low<high:
                total=arr[i]+arr[low]+arr[high]
                if total==target:
                    return True
                elif total>target:
                    high=high-1
                elif total <target:
                    low=low+1
        return False