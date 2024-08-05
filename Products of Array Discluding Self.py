class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the result array with 1s, same length as nums
        result = [1] * len(nums)

        # Initialize prefix and postfix multipliers
        prefix, postfix = 1, 1

        # Calculate prefix products and store them in result
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            result[i + 1] *= prefix

        # Calculate postfix products and store them in result
        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            result[i - 1] *= postfix

        # Return the result array which contains product of array except self
        return result
