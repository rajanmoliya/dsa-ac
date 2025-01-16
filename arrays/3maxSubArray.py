class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            maxi = max(maxi, curr_sum)

        return maxi