class Solution:
    def minimumCoinChange(self, coins: list[int], target: int) -> int:
        dp = [float("inf")] * (target + 1) # Initialize a DP array with the size target + 1 by setting infinity initially.
        dp[0] = 0 # Assign value 0 on index 0

        for a in range(1, target + 1): # Iterate the outer loop from 1 to target + 1
            for c in coins: # Iterate the loop over coins
                if (a - c) >= 0:
                    dp[a] = min(dp[a], dp[a -c] + 1) # find the minimum changes to make the target

        return dp[target] if dp[target] != float("inf") else -1 # return possible ways to make the target else return -1

sol = Solution()
print(sol.minimumCoinChange([1, 2, 5], 11))  # Output: 3
print(sol.minimumCoinChange([2], 3))        # Output: -1
print(sol.minimumCoinChange([1], 0))        # Output: 0
