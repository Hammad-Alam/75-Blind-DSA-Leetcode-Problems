class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer MAX
        MAX = 0x7FFFFFFF
        # Mask to get 32 bits
        MASK = 0xFFFFFFFF

        while b != 0:
            # XOR: Sum without carry
            temp = (a ^ b) & MASK

            # And + Shift: Handles carry
            b = ((a & b) << 1) & MASK
             a = temp

        # if a is negative, return its 2's complement
        return a if a <= MAX else ~(a ^ MASK)

sol = Solution()
print(sol.getSum(1, 2))    # Output: 3
print(sol.getSum(-2, 3))   # Output: 1
