#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # code here 
        count = 0
        
        while(str(n) != str(n)[::-1]):
            n += int(str(n)[::-1])
            count += 1
            
            if(count > 5):
                return -1
                break
        
        return n