#User function Template for python3

class Solution:
    def factorSum(self, N):
        # code here
        total=0
        i=1
        while i*i<=N:
            if N%i==0:
                total+=i
                if i!=N//i:
                    total +=N//i
            i+=1
        return total