class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

sol = Solution()
print(sol.reverseBits(0b00000010100101000001111010011100))
# Output: 964176192
