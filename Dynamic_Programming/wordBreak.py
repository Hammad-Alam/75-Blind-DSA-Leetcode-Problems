class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict) # Convert word Dictionary into set for faster lookups
        n = len(s) # Store the length of string in variable n
        dp = [False] * (n + 1) # Initialize a dp array with all values set to False initially
        dp[0] = True # Set the first index value as True

        for i in range(1, n + 1):
            for j in range(i):
                # This checks two conditions:
                # dp[j] is True, meaning the substring s[0:j] can be segmented into words
                # The substring s[j:i] is present in the word_set
                if dp[j] == True and s[j : i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

sol = Solution()
print(sol.wordBreak("Leetcode", ["Leet", "code"])) # Output: True
print(sol.wordBreak("applepenapple", ["apple", "pen"])) # Output: True
print(sol.wordBreak("catsandog", ["cats", "sand", "dog", "and", "cat"])) # Output: False