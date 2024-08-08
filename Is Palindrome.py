# Method 1: Using RegEx

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert string to lowercase, find all alphanumeric characters and spaces, join them into a single string
        s = "".join(re.findall(r"[\w\s]+", s)).lower().replace(" ", "")

        # Check if the processed string is equal to its reverse
        return s == s[::-1]


# Method 2: Using a "Two Pointers" method with a self-defined "isAlphaNum()" method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase to ensure case insensitivity
        s = s.lower()
        leftIndex = 0
        rightIndex = len(s) - 1

        # Iterate until the two indices meet in the middle
        while leftIndex < rightIndex:

            # Move leftIndex to the right until an alphanumeric character is found
            while self.isAlphaNum(s[leftIndex]) == False and leftIndex < rightIndex:
                leftIndex += 1

            # Move rightIndex to the left until an alphanumeric character is found
            while self.isAlphaNum(s[rightIndex]) == False and rightIndex > leftIndex:
                rightIndex -= 1

            # Check if the characters at the current indices are different
            if s[leftIndex] != s[rightIndex]:
                return False

            # Move both indices towards the center
            leftIndex += 1
            rightIndex -= 1

        # If all characters matched, the string is a palindrome
        return True

    def isAlphaNum(self, char):
        # Check if the character is alphanumeric
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z") or
                ord("0") <= ord(char) <= ord("9"))
