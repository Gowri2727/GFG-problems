#User function Template for python3

class Solution:
    def nonFibonacci(self, N):
        # code here
        a,b=1,2
        while True:
            c=a+b
            gap=c-b-1
            if N<= gap:
                return b+N
            N-=gap
            a,b=b,c