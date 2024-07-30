class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        emptySet: set = set()  # Initialize an empty set to track seen numbers
        nums.sort()  # Sort the list to enable early exit on finding a duplicate

        for num in nums:  # Iterate through each number in the sorted list
            if num in emptySet:  # If the number is already in the set
                return True  # A duplicate is found, return True
            emptySet.add(num)  # Add the number to the set

        return False  # No duplicates found, return False
