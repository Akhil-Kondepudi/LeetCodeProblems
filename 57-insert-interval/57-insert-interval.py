class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        inserted = False
        for n in range(len(intervals)):
            if newInterval[0] > intervals[n][0] and newInterval[0] < intervals[n][1]:
                inserted = True
                intervals[n] = [intervals[n][0], max(newInterval[1], intervals[n][1])]
            elif newInterval[1] > intervals[n][0] and newInterval[1] < intervals[n][1]:
                inserted = True
                intervals[n] = [min(newInterval[0], intervals[n][0]), intervals[n][1]]
        if not inserted:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])
        index = 0
        while(index < len(intervals) - 1):
            if(intervals[index][1] >= intervals[index + 1][0]):
                intervals[index] = [min(intervals[index][0], intervals[index + 1][0]),
                                    max(intervals[index + 1][1], intervals[index][1])]
                intervals.pop(index + 1)
                index = 0
            else:
                index += 1
        return intervals