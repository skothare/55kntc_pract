class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnInd = []
        # First, iterate through the list
        for i, num in enumerate(nums):
            findnum = target - num # this remainder should exist in the list
            if findnum in nums and nums.index(findnum) != i:
                # found findnum in nums, extract the index
                findnum_index = nums.index(findnum)
                returnInd = [i, findnum_index] if i < findnum_index else [findnum_index, i]
        return returnInd
