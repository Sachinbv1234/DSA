class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        big = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num

            if current_sum > big:
                big = current_sum

            if current_sum < 0:
                current_sum = 0

        return big
        