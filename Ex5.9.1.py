#Given a sorted array arr[] containing distinct non negative integers that has been rotated at some unknown pivot, and a value x. Your task is to count the number of elements in the array that are less than or equal to x.
class Solution:
    def countLessEqual(self, arr, x):
        count = 0
        for num in arr:
            if num <= x:
                count += 1
        return count
