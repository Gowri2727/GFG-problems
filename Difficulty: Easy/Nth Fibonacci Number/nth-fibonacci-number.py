class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        a=0
        b=1
        while(n>0):
            c=a+b
            a=b
            b=c
            n-=1
        return a