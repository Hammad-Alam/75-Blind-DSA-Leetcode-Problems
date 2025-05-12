class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n % 2 # Taking mod to identify whether the current bit is either one or zero.
            n = n >> 1 # After taking mod, we will move the remaining bits shift right by 1.
        return res

sol = Solution()
print(sol.hammingWeight(0b00000000000000000000000000001011))  # Output: 3
print(sol.hammingWeight(0b00000000000000000000000010000000))  # Output: 1
