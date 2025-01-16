class Solution:
    def get_min_max(self, arr):
        arr.sort()
        
        return arr[0], arr[-1]