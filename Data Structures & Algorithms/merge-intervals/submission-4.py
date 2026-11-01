class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # (1, 3) (2, 5)
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            prev_interval = result[-1]
            if interval[0] <= prev_interval[1]:
                prev_interval[1] = max(interval[1], prev_interval[1])
            else:
                result.append(interval)

        return result


