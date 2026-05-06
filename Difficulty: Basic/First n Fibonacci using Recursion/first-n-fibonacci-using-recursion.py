#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        l=[0,1]
        if n==1:
            return [0]
        elif n==2:
            return [0,1]
        else:
            for i in range(2,n):
                f=l[i-1]+l[i-2]
                l.append(f)
            return l