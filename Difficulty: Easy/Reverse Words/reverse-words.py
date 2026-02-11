class Solution:
    def reverseWords(self, s):
        # code here
        words=s.split('.')
        words=[w for w in words if w]
        words.reverse()
        return '.'.join(words)
        