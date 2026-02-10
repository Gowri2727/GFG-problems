#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        if n==1:
            return[0]
        if n==2:
            return [0,1]
        res=[0,1]
        for i in range(2,n):
            res.append(res[i-1]+res[i-2])
        return res