class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Initialize an empty dictionary to store numbers and their indices
        newDictionary: dict = {}

        # Iterate over the list with index and element
        for index, element in enumerate(nums):

            # Calculate the difference needed to reach the target
            difference = target - element

            # Check if the difference is already in the dictionary
            if difference in newDictionary:
                # If it is, return the indices of the two numbers
                return [newDictionary[difference], index]

            # Otherwise, store the element with its index in the dictionary
            newDictionary[element] = index

        # Return an empty list if no pair is found
        return []
