class Solution:

    def findMinDiff(self, arr,M):
      
        arr.sort()
   
        if len(arr) < M or M == 0:
            return 0 
        
        mini = float("inf")
        
        for i in range(len(arr) - M + 1):
            curr_diff = arr[i + M - 1] - arr[i]
            mini = min(mini, curr_diff)
            
        return mini