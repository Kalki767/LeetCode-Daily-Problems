from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # This array holds the height of consecutive 1s for the current row
        heights = [0] * cols
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                # If current cell is '1', increase height; otherwise reset to 0
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Calculate largest rectangle in histogram for the current row's heights
            # We append a 0 at the end to force the stack to empty out
            current_heights = heights + [0]
            stack = [-1]  # Stack stores indices; -1 is a dummy index for the left boundary
            
            for i, h in enumerate(current_heights):
                # While the current bar is lower than the bar at the top of the stack,
                # we calculate the area for the bar at the top of the stack.
                while stack[-1] != -1 and current_heights[stack[-1]] >= h:
                    height = current_heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                
                stack.append(i)
                
        return max_area