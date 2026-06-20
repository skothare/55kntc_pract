from collections import deque
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a list of lists to return
        anagrams = []
        # Options:
        """
        Option 1:
        1. We could iterate through the string word by word and group all words similar to the word
        at index i and create that group. Then, we can remove all words covered from the list and
        follow this procedure again for i+1 (the next word in the list that was not classified into an
        anagram group). IDEA: Use the previous isAnagram function.

        2. Use O(1) dictionary? Create a dictionary per word 
        """
        anagram_dict = {} # this is a dictionary of random indices (0 through length of dictionary)
        queue = deque(strs) # convert to a queue for O(1)

        while queue: # as long as queue is not empty
            current = queue.popleft() # pop the first element
            # Now, check if this element is an anagram
            # if len(anagrams) == 0: # if anagrams is empty, add the first word
            #     anagrams.append([current]) 
            for i, group in enumerate(anagrams): # iterate through every group
                # if current is an anagram of the first word in each group, then it belongs here
                if self.isAnagram(current, group[0]): 
                    anagrams[i].append(current) # append the current word to this group
                    current = None
                    break # exits the for loop
            # end for loop: either not an anagram or it was added

            # if added, check
            if current == None:
                # continue on to the next word in the queue
                continue # move on to the next while loop iteration
            else: # current word wasn't added and must be added to a new anagram group
                anagrams.append([current])
        
        return anagrams

        

    # Functions from previous example: tells you whether two strings are anagrams
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
        if len(s) != len(t):
            return False
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

# alternatively, could use "from collections import Counter" and do "count_s ="