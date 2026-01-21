class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                cur = num
                index = 0
                while( num >> 1 & (num >> (index + 1))) % 2:
                    index += 1
                mask = 1 << index
                cur ^= mask
                ans.append(cur)
        return ans