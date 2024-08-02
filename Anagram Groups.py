# Method 1 (Using the defaultdict class)

from collections import defaultdict
# Importing defaultdict class from collections module
# defaultdict sets a default value of its provided data type for missing keys


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Creating a defaultdict where each value is initialized as an empty list
        newDefaultDictionary = defaultdict(list)

        for str in strs:

            # Creating a list of 26 zeros to count the frequency of each letter in the alphabet
            newList = [0] * 26

            for character in str:

                # Incrementing the count for the corresponding character in the list
                # ord() is a funciton that returns the character's Unicode value
                newList[ord(character) - ord("a")
                        ] = newList[ord(character) - ord("a")] + 1

            # Changing "newList" to a tuple because a tuple is immutable (dictionaries' keys can only be immutable)
            newDefaultDictionary[tuple(newList)].append(str)

        # Returns the grouped anagrams as a list of lists
        return newDefaultDictionary.values()


# Method 2 (Without using the defaultdict class)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Creating an empty hashmap
        newDictionary = {}

        for str in strs:

            # Creating a list of 26 zeros to count the frequency of each letter in the alphabet
            newList = [0] * 26

            for character in str:

                # Incrementing the count for the corresponding character in the list
                # ord() is a funciton that returns the character's Unicode value
                newList[ord(character) - ord("a")
                        ] = newList[ord(character) - ord("a")] + 1

            # Changing "newList" to a tuple because a tuple is immutable (dictionaries' keys can only be immutable)
            # If "newDictionary" does not contain tuple(newList), assign an empty list
            if tuple(newList) not in newDictionary:
                newDictionary[tuple(newList)] = []

            # Append str to "newDictionary[tuple(newList)]"
            newDictionary[tuple(newList)].append(str)

        # Returns the grouped anagrams as a list of lists
        return newDictionary.values()
