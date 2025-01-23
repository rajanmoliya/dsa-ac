class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res