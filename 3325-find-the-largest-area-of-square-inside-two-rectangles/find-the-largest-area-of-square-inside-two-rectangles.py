class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        merged = []
        max_area = 0
        n = len(bottomLeft)
        for i in range(n):
            merged.append([bottomLeft[i], topRight[i]])
        merged.sort()
        for i in range(n-1):
            ix1, iy1 = merged[i][0]
            ix2, iy2 = merged[i][1]
            for j in range(i+1,n):
                jx1, jy1 = merged[j][0]
                jx2, jy2 = merged[j][1]
                if ix2 <= jx1:
                    break
                if jy2 <= iy1 or jy1 >= iy2:
                    continue
                width = min(ix2,jx2) - jx1
                height = min(iy2, jy2) - max(iy1, jy1)
                side = min(width, height)
                if side > 0:
                    max_area = max(max_area, side ** 2)
        return max_area