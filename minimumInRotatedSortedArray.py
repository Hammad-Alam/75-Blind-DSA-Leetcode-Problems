from typing import List

class Solution:
    def findMin(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        result = arr[0]

        while low < high:
            mid = (low + high) // 2

            if(arr[low] <= arr[high]): # Check if the entire array is sorted, if yes find minimum and break it
                result = min(result, arr[low])
                break

            if (arr[low] < arr[mid]): # Check if low is less than mid, if yes find minimum and update low
                result = min(result, arr[low])
                low = mid + 1
            else: # find minimum and update high
                result = min(result, arr[mid])
                high = mid - 1


        return result

sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))       # Output: 1
print(sol.findMin([4, 5, 6, 7, 0, 1, 2])) # Output: 0
print(sol.findMin([11, 13, 15, 17]))      # Output: 11
