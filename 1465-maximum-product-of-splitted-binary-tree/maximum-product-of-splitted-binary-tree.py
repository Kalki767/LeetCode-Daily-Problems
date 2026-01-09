# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        left_sum = defaultdict(int)
        right_sum = defaultdict(int)
        total_sum = 0

        def dfs(node):
            nonlocal total_sum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_sum[node] = left
            right_sum[node] = right
            total_sum += node.val
            return left + right + node.val
        dfs(root)
        
        maxi = 0
        def traverse(node):
            nonlocal maxi
            if node.left:
                cur = left_sum[node] * (total_sum - left_sum[node])
                maxi = max(maxi, cur)
                traverse(node.left)
            if node.right:
                cur = right_sum[node] * (total_sum - right_sum[node])
                maxi = max(maxi, cur)
                traverse(node.right)
            return 
        traverse(root)
        return maxi % (10**9 + 7)