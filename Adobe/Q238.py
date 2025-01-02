# Product of Array Except Self

# Approach 1: Using division

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if zero_count > 1:
                answer[i] = 0
            elif zero_count == 1:
                answer[i] = prod if nums[i] == 0 else 0
            else:
                answer[i] = prod // nums[i]

        return answer

# Approach 2: Using left and right product lists

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer