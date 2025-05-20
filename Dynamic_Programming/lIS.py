import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for num in nums:
            index = bisect.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num

        return len(tails)

sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # Output: 4