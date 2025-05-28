class Solution:
    def combinationSum1(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.combinationSum1([2,3,6,7], 7))  # Output: [[2,2,3],[7]]

