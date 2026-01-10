class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        prefix_s1 = [0]
        prefix_s2 = [0]
        for char in s1:
            prefix_s1.append(prefix_s1[-1]+ord(char))
        for char in s2:
            prefix_s2.append(prefix_s2[-1]+ord(char))
        @cache
        def dp(left, right):
            if left == len(s1) and right == len(s2):
                return 0
            if left == len(s1):
                return prefix_s2[-1] - prefix_s2[right]
            if right == len(s2):
                return prefix_s1[-1] - prefix_s1[left]
            mini = float('inf')
            if s1[left] == s2[right]:
                mini = min(mini, dp(left+1, right + 1))
            mini = min(mini, ord(s1[left]) + dp(left + 1, right), ord(s2[right]) + dp(left, right + 1))
            return mini
        
        ans = dp(0,0)
        return ans