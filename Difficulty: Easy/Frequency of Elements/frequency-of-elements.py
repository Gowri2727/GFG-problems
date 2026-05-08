class Solution:
    def countFreq(self, arr):
        #code here
        res={}
        for i in arr:
            res[i]=res.get(i,0)+1
        return [[k,v] for k,v in res.items()]