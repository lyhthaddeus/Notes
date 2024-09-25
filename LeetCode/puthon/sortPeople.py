class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        sortedPears = sorted(zip(heights, names), reverse=True)
        return [name for height, name in sortedPears]
