class Solution:
    def countBalanced(self, low: int, high: int) -> int:    
        
        def backtrack(diff, pos, prev):
            if pos == len(prefix):
                if diff == 0:
                    return 1
                return 0
            if (diff, pos, prev) in memo:
                return memo[(diff, pos, prev)]
            current = 0
            if not prev:
                limit = prefix[pos]
            else:
                limit = 9
            
            if pos % 2 == 0 :
                for i in range(limit + 1):
                    cur = prev
                    if prefix[pos] > i:
                        cur = True
                    diff += i
                    current += backtrack(diff, pos + 1, cur)
                    diff -= i
            else:
                for i in range(limit + 1):
                    cur = prev
                    if prefix[pos] > i:
                        cur = True
                    diff -= i
                    current += backtrack(diff,pos + 1, cur)
                    diff += i

            memo[(diff, pos, prev)] = current
            return current
        memo = {}
        prefix = []
        new_low, new_high = low - 1, high
        while new_low:
            prefix.append(new_low%10)
            new_low //= 10
        prefix.reverse()
        until_low = backtrack(0,0,False) - 1
        memo = {}
        prefix = []
        while new_high:
            prefix.append(new_high % 10)
            new_high //= 10
        prefix.reverse()
        until_high = backtrack(0,0,False) - 1
        return until_high - until_low
        