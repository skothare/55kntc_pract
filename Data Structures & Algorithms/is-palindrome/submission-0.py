import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip all spaces and punctuation
        s = s.replace(" ", "")
        s = s.lower()
        s = re.sub(r'[^\w\s]', '', s)
        

        reverse_s = s[: : -1]

        print(f"string is {s} and reverse is {reverse_s}")

        for char1, char2 in zip(s, reverse_s):
            if ord(char1) - ord(char2) != 0:
                print(f"char1 is {char1} and char2 is {char2} giving us a non-zero val of ord(char1) - ord(char2)")
                return False # not a palindrome if the subtraction of ASCII doesn't give 0
            else:
                print(f"char1 is {char1} and char2 is {char2} giving us 0 ({ord(char1) - ord(char2)})")
                continue # current character difference is 0 so continue
        return True # all character differences are 0, so it is a palindrome.