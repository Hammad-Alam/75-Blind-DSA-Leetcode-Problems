class Solution:
    def printLCS(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Backtrack to find the LCS
        lcs = []
        i , j = m , n
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcs.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else: 
                j -= 1

        # Return the longest common subsequence in the correct order
        return "".join(reversed(lcs))

sol = Solution()
text1 = "AGGTAB"
text2 = "GXTXAYB"
lcs = sol.printLCS(text1, text2)
print("Longest Common Subsequence:", lcs)