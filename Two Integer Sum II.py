class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers: left at the start and right at the end of the list
        left = 0
        right = len(numbers) - 1

        while True:
            # Calculate the sum of the current two numbers
            currentSum = numbers[left] + numbers[right]

            # If the current sum is less than the target, move the left pointer right
            if currentSum < target:
                left += 1

            # If the current sum is greater than the target, move the right pointer left
            elif currentSum > target:
                right -= 1

            # If the current sum equals the target, break the loop
            else:
                break

        # Return the 1-based indices of the two numbers
        return [left + 1, right + 1]
