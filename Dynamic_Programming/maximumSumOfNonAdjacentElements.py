class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev2, prev1 + nums[i])
            prev1, prev2 = prev2, current

        return prev2

sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12
