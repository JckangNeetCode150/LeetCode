# Method 1: Time Complexity = O(n)

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # Initialize two pointers, left at the start and right at the end of the list
        left = 0
        right = len(heights) - 1

        # Variable to store the maximum area found
        result = 0

        # Iterate until the two pointers meet
        while left < right:
            # Calculate the height of the container using the shorter pillar
            pillarHeight = min(heights[left], heights[right])

            # Calculate the width of the container
            pillarWidth = right - left

            # Calculate the area of the current container
            pillarArea = pillarHeight * pillarWidth

            # Update the maximum area found so far
            result = max(result, pillarArea)

            # Move the pointer pointing to the shorter pillar inward to potentially find a larger area
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left += 1

        # Return the maximum area found
        return result


# Method 2: Time Complexity = O(n^2)

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0  # Start with the leftmost index
        right = len(heights) - 1  # Start with the rightmost index
        result = 0  # Initialize the maximum area

        while left < right:

            # Determine the shorter pillar
            pillarHeight = min(heights[left], heights[right])

            pillarWidth = right - left  # Calculate the width between the pillars

            pillarArea = pillarHeight * pillarWidth  # Calculate the current area

            # Update the maximum area if the current one is larger
            result = max(result, pillarArea)

            if right == left + 1:
                left = 0  # Reset the left pointer if pillars are adjacent
                right -= 1  # Move the right pointer leftward

            else:
                left += 1  # Increment the left pointer if the pillars are not adjacent

        return result  # Return the maximum area found
