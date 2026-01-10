class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(left, right):
            if left == len(nums1) or right == len(nums2):
                return float('-inf')
            product = nums1[left] * nums2[right]
            curr = max(product, product + dp(left + 1, right + 1))
            
            curr = max(curr, dp(left, right + 1), dp(left + 1, right))
            return curr
        return dp(0,0)