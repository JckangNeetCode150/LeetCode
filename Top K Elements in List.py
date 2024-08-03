class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        newDictionary = {}  # Creates a hashmap to store frequency of each number
        newList = []  # Creates a list to store the top k frequent numbers

        # Populate "newDictionary" with the count of each number in "nums"
        for num in nums:
            if num not in newDictionary:
                newDictionary[num] = 0
            newDictionary[num] += 1

        # Sort the dictionary items by their frequency in descending order
        # lambda denotes an anonymous function, syntax = lambda argument(s): expression
        sortedValues = sorted(newDictionary.items(),
                              key=lambda x: x[1], reverse=True)

        # Append the top k keys (numbers) to "newList"
        for i in range(k):
            newList.append(sortedValues[i][0])

        return newList
