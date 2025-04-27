from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i

        # No solution found return empty List
        return []

sol = Solution()
print(sol.twoSum([2, 6, 5, 8, 11], 14))  # Output: [1, 3]
