#You will be given a vector of integers of size n containing the elements. Your task is to find the sum of all the integers present in the array.As the sum can be large you have to return a value in long long data type.
class Solution:
    def get_Sum(self, n, input):
        total = 0
        for i in input:
            total += i
        return total
