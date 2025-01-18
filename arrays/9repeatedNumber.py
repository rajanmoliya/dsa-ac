class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        freq = {}
        repeated = 0
        
        for n in A:
            freq[n] = freq.get(n, 0) + 1
        
        for idx, counter in freq.items():
            if counter > 1:
                repeated = idx
                
        n = len(A)
        expected = n * (n+1) // 2 
        actual = sum(A)
        
        missing = expected - actual + repeated
        
        return [repeated, missing]