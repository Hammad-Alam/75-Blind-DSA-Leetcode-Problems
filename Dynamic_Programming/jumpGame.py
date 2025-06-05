class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)

        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))  # True
print(sol.canJump([3,2,1,0,4]))  # False
print(sol.canJump([0]))         # True (already at last index)
print(sol.canJump([2,0,0]))     # True
