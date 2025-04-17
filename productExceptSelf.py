from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums)) # Creating a result array in which we are going to store 1 on all positions of the array initially.

        prefix = 1 # Initialize prefix as 1
        for i in range(len(nums)): # Iterate a for loop from start to end
            result[i] = prefix # Store prefix in result index
            prefix *= nums[i] # Calculate prefix by multiplying prefix with ith element

        postfix = 1 # Initialize postfix as 1
        for i in range(len(nums) - 1, -1, -1): # Iterate a for loop from end to start
            result[i] *= postfix 
            postfix *= nums[i]

        return result

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))