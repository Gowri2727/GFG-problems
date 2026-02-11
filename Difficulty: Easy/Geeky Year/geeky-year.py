#User function Template for python3

class Solution:
	def Count(self, a, b):
		def is_sunday(year):
            # For January, treat as month 13 of previous year
            q = 1
            m = 13
            y = year - 1
            
            K = y % 100
            J = y // 100
            
            h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
            
            # h = 1 means Sunday
            return h == 1
        
        count = 0
        for year in range(a, b + 1):
            if is_sunday(year):
                count += 1
        
        return count