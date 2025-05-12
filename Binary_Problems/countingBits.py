from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) # Initialize list for n + 1 elements with 0 on all places.

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1) 
        return res

sol = Solution()
print(sol.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
print(sol.countBits(10)) # Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
