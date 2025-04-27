from typing import List

class Solution:
    def checkDuplicate(self, nums: List[int]) -> bool:
        num_map = {}

        for i in nums:
            if i in num_map:
                return True
            else:
                num_map[i] = i

        return False

sol = Solution()
print(sol.checkDuplicate([1, 2, 3, 4])) # Output: False
print(sol.checkDuplicate([1, 2, 3, 1])) # Output: True
