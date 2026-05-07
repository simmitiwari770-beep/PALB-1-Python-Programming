#You are given an array arr[]. The task is to determine whether the array contains a 132 pattern, i.e., three indices i,  j and k such that i < j < k , arr[i] < arr[j] > arr[k] and arr[i] < arr[k].
#Return true if such a triplet exists, otherwise return false.
class Solution:
    def has132Pattern(self, arr):
        stack = []
        third = float('-inf')   # this will act as "2" in 132
        
        # Traverse from right
        for i in range(len(arr) - 1, -1, -1):
            
            # If current is less than "third", we found 132
            if arr[i] < third:
                return True
            
            # Maintain decreasing stack
            while stack and stack[-1] < arr[i]:
                third = stack.pop()
            
            stack.append(arr[i])
        
        return False
