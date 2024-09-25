class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutePoint = sorted(self.TTM(time) for time in timePoints)
        
        final = float('inf')
        lenth = len(minutePoint)

        for i in range(1, lenth):
            final = min(final, minutePoint[i] - minutePoint[i-1])

        newDayDiff = 24 * 60 - (minutePoint[-1] - minutePoint[0])

        final = min(final, newDayDiff)

        return final


    def TTM(self, time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
