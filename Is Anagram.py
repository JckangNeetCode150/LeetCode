class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create dictionaries to count the occurrences of each character in both strings.
        sDictionary, tDictionary = {}, {}

        # Loop through each character in the strings.
        for i in range(len(s)):
            # Increment the count for the character in sDictionary and tDictionary.
            sDictionary[s[i]] = sDictionary.get(s[i], 0) + 1
            tDictionary[t[i]] = tDictionary.get(t[i], 0) + 1

        # Compare the character counts in both dictionaries.
        for keyCharacter in sDictionary:
            if sDictionary[keyCharacter] != tDictionary.get(keyCharacter, 0):
                return False

        # If all character counts match, the strings are anagrams.
        return True
