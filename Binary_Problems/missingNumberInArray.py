from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)

        total = n * (n + 1) // 2 # Do summation of length of an array
        result = total - sum(arr) # Subtract sum of an array from total

        return result
        
sol = Solution()
print(sol.missingNumber([3, 0, 1]))  # Output: 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8        