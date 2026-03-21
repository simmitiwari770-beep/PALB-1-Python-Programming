#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()   # sort by starting time

        merged = []

        for interval in intervals:
            # If merged is empty OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping case → merge
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
