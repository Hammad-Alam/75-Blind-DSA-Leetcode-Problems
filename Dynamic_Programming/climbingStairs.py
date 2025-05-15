class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: # If there are 1 or 2 stairs then
            return n # There will be 1 or 2 ways to climb

        dp = [0] * (n + 1) # Initialize a dp array with n+1 size to store 0 on all places initially.
        dp[1], dp[2] = 1, 2 # Store 1, and 2 on index 1 and 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # For each stair i, sum the taken step by 1 and taken step by 2

        return dp[n]

sol = Solution()
print(sol.climbStairs(5))  # Output: 8
print(sol.climbStairs(10)) # Output: 89
