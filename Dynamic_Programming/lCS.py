class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1), len(text2) # Store length of text1 and text2 in m, and n.
        dp = [[0] * (n + 1) for _ in range(m + 1)] # Define a 2D matrix to store the common subsequence.

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # If the character of text1 and text2 matches then
                    dp[i][j] = 1 + dp[i - 1][j - 1] # Increase 1 in the length of the common subsequence
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n] # Return the length of the common subsequence

sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(sol.longestCommonSubsequence("abc", "abc"))    # Output: 3
print(sol.longestCommonSubsequence("abc", "def"))    # Output: 0
