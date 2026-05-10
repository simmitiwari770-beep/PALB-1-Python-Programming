#Given an array arr[] of integers and an integer k, select k elements from the array such that the minimum absolute difference between any two of the selected elements is maximized. Return this maximum possible minimum difference.
class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def can_place(diff):
            count = 1
            last = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - last >= diff:
                    count += 1
                    last = arr[i]
                if count >= k:
                    return True
            return False
        
        left = 0
        right = arr[-1] - arr[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
