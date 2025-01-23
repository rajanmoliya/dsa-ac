import heapq
class Solution:

    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
        res = []
        Ksmallest = None
        
        for i in range(k):
            Ksmallest = heapq.heappop(arr)
        
        return Ksmallest