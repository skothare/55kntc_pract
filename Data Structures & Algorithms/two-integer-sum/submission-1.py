class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnInd = []
        # METHOD 1: Non-hashmap
        # # First, iterate through the list
        # for i, num in enumerate(nums):
        #     findnum = target - num # this remainder should exist in the list
        #     if findnum in nums and nums.index(findnum) != i:
        #         # found findnum in nums, extract the index
        #         findnum_index = nums.index(findnum)
        #         returnInd = [i, findnum_index] if i < findnum_index else [findnum_index, i]
        # return returnInd

        # first, also create a hashmap of value and index of each element in the array
        map = {}
        for i, num in enumerate(nums):
            findnum = target-num # find this number in the map
            # we want to create the map but if we find the pair, we must return it
            if findnum in map:
                return [map[findnum], i] if i > map[findnum] else map[i, findnum]
            # not found, add the current i in the map
            map[num] = i
            