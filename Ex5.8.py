#Given two integers n and k, the task is to find all valid combinations of k numbers that adds up to n based on the following conditions:
class Solution:
    def combinationSum(self, n, k):
        res = []
        
        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return
            
            for i in range(start, 10):
                if total + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        
        backtrack(1, [], 0)
        return res
