class Solution:
    def lengthOfLIS(self, nums):
        lis = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for opp in range(i + 1, len(nums)):
                if nums[i] < nums[opp]:
                    lis[i] = max(lis[i], 1 + lis[opp])

        return max(lis) 