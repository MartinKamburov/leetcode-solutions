class Solution:
    def permute(self, nums):
        results = []

        def backtrack(index, curr):
            # Since permutation when the length of the current set == nums 
            # thats when you append the result
            if len(curr) == len(nums):
                results.append(curr.copy())
                return

            for index in range(len(nums)):
                # This is the constraint check if the current nums[index] is in the current set
                # if it is in the current set continue we only want distinct nums[index] values
                if index > len(nums) or nums[index] in curr:
                    continue

                # Add nums[index] and just pop it after 
                curr.append(nums[index])
                backtrack(index + 1, curr)
                curr.pop()

        backtrack(0, [])

        return results