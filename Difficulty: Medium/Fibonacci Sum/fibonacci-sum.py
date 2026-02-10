#User function Template for python3

class Solution:
    def fibSum (self,N):
        #code here
        MOD=1000000007
        def fib(n):
            if n==0:
                return (0,1)
            a,b=fib(n//2)
            c=(a*((2*b-a)%MOD))%MOD
            d=(a*a+b*b)%MOD
            if n%2==0:
                return (c,d)
            else:
                return (d,(c+d)%MOD)
        fn_plus_2=fib(N+2)[0]
        return (fn_plus_2-1)%MOD