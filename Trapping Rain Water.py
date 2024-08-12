class Solution:
    def trap(self, height: list[int]) -> int:
        # Initialize two pointers to track the left and right ends of the height array
        left, right = 0, len(height) - 1

        # Initialize the maximum heights on the left and right sides
        maxLeft, maxRight = height[left], height[right]

        # Initialize the result to store the total amount of trapped water
        result = 0

        # Iterate until the two pointers meet
        while left < right:
            # If the left maximum height is less than the right maximum height
            if maxLeft < maxRight:
                # Move the left pointer to the right
                left += 1

                # Update the left maximum height
                maxLeft = max(height[left], maxLeft)

                # Add the trapped water at the current left position
                result += maxLeft - height[left]

            else:
                # Move the right pointer to the left
                right -= 1

                # Update the right maximum height
                maxRight = max(height[right], maxRight)

                # Add the trapped water at the current right position
                result += maxRight - height[right]

        # Return the total amount of trapped water
        return result
