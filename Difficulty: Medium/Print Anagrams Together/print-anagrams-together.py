#User function Template for python3
from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        t=defaultdict(list)
        for i in arr:
            t["".join(sorted(i))].append(i)
        return list(t.values())
