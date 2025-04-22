from typing import List

class Solution:
    # Search Unique elements
    def search(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if (arr[mid] == target):
                return mid

            # Left half is sorted
            if (arr[low] <= arr[mid]):
                if(arr[low] <= target and target <= arr[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if(arr[mid] <= target and target <= arr[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1

    # Search in Duplicate elements
    def searchInDuplicates(self, arr: List[int], target: int) -> bool:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if (arr[mid] == target):
                return True

            if (arr[low] == arr[mid] and arr[mid] == arr[high]):
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if (arr[low] <= arr[mid]):
                if (arr[low] <= target and target <= arr[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if(arr[mid] <= target and target <= arr[high]):
                    low = mid + 1
                else:
                    high = mid - 1

        return False

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(sol.search([1], 0))             # Output: -1

print(sol.searchInDuplicates([3,3,1,3,3,3,3], 3))
