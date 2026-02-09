#User function Template for python3
class Solution:

	def factorial(self,a, n):
    	# code here
    	MOD = 10**9 + 7
        
        max_val = max(a)
        
        # Step 1: Precompute factorials up to max(A)
        fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        
        # Step 2: Build answer list
        result = []
        for num in a:
            result.append(fact[num])
        
        return result
