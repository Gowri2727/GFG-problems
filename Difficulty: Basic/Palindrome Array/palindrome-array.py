
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        return arr==arr[::-1]
        
