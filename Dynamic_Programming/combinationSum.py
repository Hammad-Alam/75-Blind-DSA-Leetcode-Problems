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

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.combinationSum1([2,3,6,7], 7))  # Output: [[2,2,3],[7]]
print(sol.combinationSum2([10,1,2,7,6,1,5], 8)) # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]