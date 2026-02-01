class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, curr_subset):
            # Base case: when the index is at the end of the nums array
            if index == len(nums):
                result.append(curr_subset.copy())
                return 

            # Backtracking always has decisions you must make and to get all subsets we must choose whether to include or not include an element at each step
            # Decision 1: include nums[index]
            curr_subset.append(nums[index])
            backtrack(index + 1, curr_subset)
            curr_subset.pop()

            # Decision 2: skip nums[index] we skip it by popping like we did above
            # This is the actual backtracking part 
            backtrack(index + 1, curr_subset)

        backtrack(0, [])

        return result