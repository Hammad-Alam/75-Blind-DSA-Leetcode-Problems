from typing import List, Tuple

class Solution:
    def maximumSubArraySum(self, nums: List[int]) -> Tuple[int, List[int]]:
        maxSum = currentSum = nums[0] # Initialize maxSum, and currentSum = first element of list
        start = end = tempStart = 0 # Initialize start, end, and tempStart = 0

        for i in range(1, len(nums)): # Iterate a for loop from 1 till end
            if currentSum + nums[i] < nums[i]: # If currentSum + currentElement < currentElement then
                currentSum = nums[i] # Assign currentElement to currentSum
                tempStart = i 
            else:
                currentSum += nums[i] # Otherwise assign currentSum to the sum of currentSum and currentElement

            if currentSum > maxSum: # If currentSum is greater than maxSum then
                maxSum = currentSum # Assign maxSum to currentSum
                start = tempStart
                end = i

        return maxSum, nums[start : end + 1]

sol = Solution()
max_sum, subarray = sol.maximumSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Maximum Subarray Sum:", max_sum) # Output: 6
print("Subarray:", subarray) # Output: [4, -1, 2, 1]
