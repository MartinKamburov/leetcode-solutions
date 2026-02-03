class Solution:
    def combinationSum(self, candidates, target):
        results = []
        # Sort the array since we don't want to look at elements to the left since we only want distinct combinations
        candidates.sort()

        def backtrack(index, subset, curr_target):
            if curr_target == target:
                results.append(subset.copy())
                return 

            # When looping through the choices we must always start at the index in the range
            # This is because anything to the left of index should not be looked at
            # Only indexes to the right of the candidates should be looked at this is why we sorted candidates
            for i in range(index, len(candidates)):
                # if add the current index is > target just skip that path
                if (candidates[i] + curr_target) > target:
                    continue

                subset.append(candidates[i])
                backtrack(i, subset, candidates[i] + curr_target)
                subset.pop()

        backtrack(0, [], 0)

        return results