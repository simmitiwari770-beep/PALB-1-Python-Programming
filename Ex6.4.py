#Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return the minimum difference in seconds between any two time strings in the arr[].
class Solution:
    def minDifference(self, arr):
        times = []
        
        # convert to seconds
        for t in arr:
            h, m, s = map(int, t.split(':'))
            total = h * 3600 + m * 60 + s
            times.append(total)
        
        times.sort()
        
        # find min diff
        ans = float('inf')
        
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i-1])
        
        # circular case (last → first)
        ans = min(ans, 86400 - times[-1] + times[0])
        
        return ans
