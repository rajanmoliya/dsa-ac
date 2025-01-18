class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]

        curr_max = nums[0]
        curr_min = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            res = max(res, curr_max)
            
        return res