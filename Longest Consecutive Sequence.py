# Method 1: Using the sort() method. Time complexity: nlog(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # If there are fewer than 2 elements (0 and 1 element), the longest consecutive sequence is the length of the list itself
        if len(nums) < 2:
            return len(nums)

        # Sort the list to bring consecutive numbers next to each other
        # The time complexity of the sorting method is nlog(n)
        nums.sort()

        internalResult = 1  # Current length of the consecutive sequence
        finalResult = 1  # Longest length found so far
        counter = 0  # Index to traverse the list

        while True:

            # If the current number is exactly 1 less than the next, increment "internalResult"
            if nums[counter] + 1 == nums[counter+1]:
                internalResult += 1

            # If the next number isn't consecutive and isn't a duplicate, reset the current sequence length
            elif nums[counter] + 1 != nums[counter+1] and nums[counter] != nums[counter+1]:
                internalResult = 1

            # Update the longest sequence length found
            finalResult = max(internalResult, finalResult)

            # Break the loop when reaching the second last element
            if (counter == len(nums) - 2):
                break

            # Move to the next element.
            counter += 1

        # Return the length of the longest consecutive sequence
        return finalResult


# Method 2: Segregate the elements of the list into different sequences, with each sequence's first element starting with a number that does not have its number - 1 in the list
# Time complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # Initializes the variable to store the length of the longest consecutive sequence
        longest = 0

        # Iterates through each number in the list
        for i in range(len(nums)):

            # Checks if the current number is the start of a sequence (i.e., no number one less than it exists in the list)
            if nums[i] - 1 not in nums:

                # Initializes the length of the current sequence
                length = 1

                # Checks for the next consecutive numbers in the sequence
                while (nums[i] + length) in nums:
                    length += 1

                # Update the longest sequence length if the current sequence is longer
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence
        return longest
