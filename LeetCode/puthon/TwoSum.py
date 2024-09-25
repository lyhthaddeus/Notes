def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map = {}
    for i, number in enumerate(nums):
        complement = target - number
        if complement in map:
            return [map[complement], i]
        map[number] = i

assert twoSum([3,2,4], 6) == [1, 2], 'Test failed'
