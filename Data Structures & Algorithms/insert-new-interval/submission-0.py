class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:

            # case 1: current interval is before new interval
            if interval[1] < newInterval[0]:
                result.append(interval)
            # case 2: New interval is after current interval
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            # case 3: Two intervals overlap, merge them
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
       
        result.append(newInterval)

        return result
        