# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_depth = defaultdict(int)
        def depthCalc(node,depth):
            if not node:
                return
            node_depth[node] = depth
            if node.left:
                depthCalc(node.left, depth + 1)
            if node.right:
                depthCalc(node.right, depth + 1)
            return
        depthCalc(root,0)
        maxi = 0
        for key, val in node_depth.items():
            maxi = max(maxi,val)
        deepest_nodes = set()
        count = 0
        for key in node_depth:
            if maxi == node_depth[key]:
                deepest_nodes.add(key)
                count += 1
        smallest_node = root
        flag = False
        def dfs(node):
            nonlocal smallest_node, flag, count
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            is_deeper = 1 if node in deepest_nodes else 0
            if left + right + is_deeper == count and not flag:
                smallest_node = node
                flag = True
            return left + right + is_deeper
        dfs(root)
        return smallest_node
                