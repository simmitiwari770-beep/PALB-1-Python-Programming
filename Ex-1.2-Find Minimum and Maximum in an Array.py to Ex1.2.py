class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < minimum:
                minimum = arr[i]

            if arr[i] > maximum:
                maximum = arr[i]

        return [minimum, maximum]


# Example usage
arr = [3, 5, 1, 8, 2]
solution = Solution()
print(solution.getMinMax(arr))
