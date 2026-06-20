class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # # METHOD 1: Does not pass s-"bbcc", t="ccbc" test case
        # # we know that len(s) == len(t) (not a string matching/substring problem)
        # # use convert to a set() to reduce repeated characters. Compare length of sets.
        # # Then compare the exact characters
        # set_s, set_t = set(s), set(t)
        # if len(set_s) != len(set_t) or len(s) != len(t):
        #     return False # immediately false as sets should also be of equal size (without common repeated elements)
        # if set_s == set_t:
        #     return True
        # else:
        #     return False

        # Method 2: Create a dictionary of counts and then compare
        count_s, count_t = self.dictionarize(s), self.dictionarize(t)
        return count_s == count_t # returns true or false if both the key and values match
    def dictionarize(self, string: str) -> dict:
        counts = {} # create a dictionary
        for i, char in enumerate(string):
            if char in counts:
                counts[char] += 1 # increment the existing value
            else:
                counts[char] = 1 # initialize if new
        return counts

        