class Solution:
    def isBalanced(self, s):
        # code here
        while True:
            if '[]' in s:
                s=s.replace('[]','')
            elif '{}' in s:
                s=s.replace('{}','')
            elif '()' in s:
                s=s.replace('()','')
            else:
                return not s