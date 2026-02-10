#User function Template for python3
class Solution:
    def fib (self,N):
        #code here
        if N==0:
            return 0
        if N==1:
            return 1
        a,b=0,1
        for i in range(2,N+1):
            a,b=b,(a+b)%10
        return b