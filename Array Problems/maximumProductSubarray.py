from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = suff = 1
        result = 0

        for i in range(len(nums)):
            if pre == 0:
                pre = 1

            if suff == 0:
                suff = 1

            pre *= nums[i]
            suff *= nums[i]

            result = max(result, max(pre, suff))

        return result

sol = Solution()
print(sol.maxProduct([2, 3, -2, 4])) # Output: 6 (subarray [2, 3])
print(sol.maxProduct([-2, 0, -1]))   # Output: 0 (subarray [0])
print(sol.maxProduct([-2, 3, -4]))   # Output: 24 (subarray [3, -4])
