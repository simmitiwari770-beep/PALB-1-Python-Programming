#Given an array arr[], find the minimum number of operations required to make the sum of its elements less than or equal to half of the original sum
import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2
        
        # max heap using negative values
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        operations = 0
        current_sum = total
        
        while current_sum > target:
            largest = -heapq.heappop(heap)
            
            half = largest / 2
            current_sum -= half
            
            heapq.heappush(heap, -half)
            
            operations += 1
        
        return operations
