from typing import List

class Solution:
    def mostWater(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        maxWater = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            area = width * height
            maxWater = max(maxWater, area)

            # Move shorter line's pointer
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return maxWater

sol = Solution()
print(sol.mostWater([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(sol.mostWater([1,1]))               # Output: 1