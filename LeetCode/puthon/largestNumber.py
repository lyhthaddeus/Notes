class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(self.compare))
        if nums[0] == "0":
            return "0"
        return ''.join(nums)

    def compare(self, x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
