class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the list to make it easier to avoid duplicates and apply two-pointer technique
        nums.sort()
        result = []

        # Iterate through the list
        for i in range(len(nums)):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initialize two pointers: left starts just after i, right starts at the end of the list
            left = i + 1
            right = len(nums) - 1

            # Narrow down the potential triplet
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                # If the sum is less than zero, move the left pointer to the right to increase the sum
                if threeSum < 0:
                    left += 1

                # If the sum is greater than zero, move the right pointer to the left to decrease the sum
                elif threeSum > 0:
                    right -= 1

                # If the sum is zero, add the triplet to the result list
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # Skip the same element to avoid duplicate triplets
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        # Return the list of triplets that sum to zero
        return result
