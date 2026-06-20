import numpy as np

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # checkarr = []
        # for (i, num) in enumerate(nums):
        #     if num in checkarr:
        #         # return the boolean immediately
        #         return True
        #     else:
        #         # add the number to the checkarr
        #         checkarr.append(num)
        # return False

        # First, create a duplicate array and then divide the two arrays

        # Second, in the division of those two arrays, find if there are numerous "1"s
        # If numerous 1s, then duplicates exist

        #return True if len(nums) > len(set(nums)) else False

        return len(nums) > len(set(nums))

