class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        sett = set(nums)
        count = 0
        for num in sett:
            if (num + diff in sett) and (num + diff + diff in sett):
                count += 1
        return count
