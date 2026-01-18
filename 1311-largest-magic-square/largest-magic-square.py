class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # 1. Row Prefix Sums
        row_sum = [[0 for _ in range(cols + 1)]]
        for row in range(rows):
            cur_sum = [0]
            for col in range(cols):
                cur_sum.append(cur_sum[-1] + grid[row][col])
            row_sum.append(cur_sum)
            
        # 2. Column Prefix Sums
        col_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for col in range(cols):
            for row in range(rows):
                col_sum[row + 1][col + 1] += col_sum[row][col + 1] + grid[row][col]
        
        # 3. Main Diagonal Prefix Sums
        diagonal_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                diagonal_sum[row + 1][col + 1] += diagonal_sum[row][col] + grid[row][col]
                
        # 4. Reverse Diagonal Prefix Sums (FIXED)
        # We increase size to cols + 2 to handle the "Up-Right" lookahead safely
        reverse_diagonal = [[0 for _ in range(cols + 2)] for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # Current grid value is grid[r-1][c-1]
                # We add it to the value found Up (r-1) and Right (c+1)
                reverse_diagonal[r][c] = reverse_diagonal[r - 1][c + 1] + grid[r - 1][c - 1]

        def check(k):
            # Loop range ensures we don't go out of bounds
            for row in range(1, rows + 1 - k + 1):
                for col in range(1, cols + 1 - k + 1):
                    
                    # Target sum is the sum of the first row in the candidate square
                    common_sum = row_sum[row][col + k - 1] - row_sum[row][col - 1]
                    
                    match = True
                    
                    # Check all Rows
                    for r in range(k):
                        current_row_sum = row_sum[row + r][col + k - 1] - row_sum[row + r][col - 1]
                        if current_row_sum != common_sum:
                            match = False
                            break
                    if not match: continue
                    
                    # Check all Columns
                    for c in range(k):
                        current_col_sum = col_sum[row + k - 1][col + c] - col_sum[row - 1][col + c]
                        if current_col_sum != common_sum:
                            match = False
                            break
                    if not match: continue
                    
                    # Check Main Diagonal
                    # Bottom-Right - Top-Left-Previous
                    d1 = diagonal_sum[row + k - 1][col + k - 1] - diagonal_sum[row - 1][col - 1]
                    if d1 != common_sum: continue

                    # Check Reverse Diagonal (FIXED)
                    # Bottom-Left - Up-Right-Previous
                    # Bottom-Left is at [row + k - 1][col]
                    # Up-Right-Previous is at [row - 1][col + k]
                    d2 = reverse_diagonal[row + k - 1][col] - reverse_diagonal[row - 1][col + k]
                    if d2 != common_sum: continue
                    
                    return True
            return False

        # Check sizes from largest possible (min dimension) down to 1
        maxi = min(rows, cols)
        for i in range(maxi, 0, -1):
            if check(i):
                return i
        return 1