#User function Template for python3

class Solution:
    def nFibonacci(self,N):
        #code here
        result =[]
        a,b=0,1
        while a<=N:
            result.append(a)
            a,b=b,a+b
        return result