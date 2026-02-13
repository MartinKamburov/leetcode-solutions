class Solution:
    def climbStairs(self, n):
        one, two = 1, 1

        # This would be like a fibonacci sequence except bottom-up where theres one way
        # to get to the final and option before the final
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one