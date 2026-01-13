from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(cutting_point):
            below = above = 0
            for start_x, start_y, length in squares:
                if cutting_point <= start_y:
                    above += (length ** 2)
                elif cutting_point >= start_y + length:
                    below += (length ** 2)
                else:
                    below += ((cutting_point - start_y) * length)
                    above += ((start_y + length - cutting_point) * length)
            return below, above
        
        # Determine the search range
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        answer = float('inf')
        # Binary search with precision threshold
        while high - low > 1e-5:
            mid = (low + high) / 2
            below, above = check(mid)
            
            if below < above:
                low = mid
            else:
                high = mid
        
        return low  # Either low or high is fine within the precision limit