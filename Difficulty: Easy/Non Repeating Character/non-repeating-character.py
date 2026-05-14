class Solution:
    def nonRepeatingChar(self,s):
        #code here
        lis=[]
        repeated=set()
        for ch in s:
            if ch not in lis and ch not in repeated:
                lis.append(ch)
            elif ch in lis:
                lis.remove(ch)
                repeated.add(ch)
        if not lis:
            return "$"
        return lis[0]