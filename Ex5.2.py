#You are given an array arr[] of size n , where arr[i] denotes the range of working hours a person at position i can cover.
class Solution:
    def minMen(self, arr):   # ✅ change name here
        n = len(arr)
        intervals = []
        
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))
        
        intervals.sort()
        
        count = 0
        i = 0
        curr_end = 0
        farthest = 0
        
        while curr_end < n:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1
            
            if farthest == curr_end:
                return -1
            
            curr_end = farthest
            count += 1
        
        return count
