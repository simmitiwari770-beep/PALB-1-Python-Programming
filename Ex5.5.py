#You are given an integer array arr[ ]. Your task is to count the number of subarrays where the first element is the minimum element of that subarray.
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        
        # Find next smaller element index
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                next_smaller[i] = stack[-1]
            
            stack.append(i)
        
        # Count subarrays
        count = 0
        for i in range(n):
            count += (next_smaller[i] - i)
        
        return count
