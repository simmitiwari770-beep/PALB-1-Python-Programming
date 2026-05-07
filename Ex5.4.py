#You are given an integer array arr[ ]. For every element in the array, your task is to determine its Previous Greater Element (PGE)
class Solution:
    def preGreaterEle(self, arr):
        stack = []
        result = []
        
        for i in arr:
            while stack and stack[-1] <= i:
                stack.pop()
            
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            stack.append(i)
        
        return result
