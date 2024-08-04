class Solution:

    def encode(self, strs: list[str]) -> str:
        singleString = ""  # Initializes an empty string to store the encoded result
        for s in strs:  # Iterates over each string in the list

            # Appends the length of the string, a delimiter '#', and the string itself to the result
            singleString = singleString + str(len(s)) + "#" + s

        return singleString

    def decode(self, s: str) -> list[str]:
        newList = []  # Initializes an empty list to store the decoded strings

        # Continue decoding while string "s" is not empty and starts with a digit
        while s != "" and s[0].isdigit():

            # Extracts the length of the element, starting from the first digit to the digit before "#"
            elementLength = int(s[s.index(s[0]): s.index("#")])

            # Number of '#' characters to skip is always 1
            skippableHashTagCount = 1

            # Calculate the digit count in "elementLength"
            digitCount = len(list(str(elementLength)))

            # Slices the "s" string for the element using "skippableHashTagCount" and "digitCount"
            currentElement = s[skippableHashTagCount +
                               digitCount: elementLength + skippableHashTagCount + digitCount]

            # Add the extracted element to the list
            newList.append(currentElement)

            # Remove the processed part from the string
            # Replace() syntax = string.replace(old, new, count)
            s = s.replace(str(elementLength) + "#" + currentElement, "", 1)

        return newList
