class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        
        # Swap elements from start and end
        for i in range(n // 2):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        
        return arr


# Example usage
arr = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.reverseArray(arr))
