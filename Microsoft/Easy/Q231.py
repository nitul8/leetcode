#Power of two
#Given a number, check if it is a power of 2.

# First Approach: Using recursive method - 
def powerOfTwo(n):
    if n == 1:                  # Check if n is 1, then return True
        return True
    elif n % 2 != 0 or n == 0:  # Check if n is 0 or n is not divisible by 2, then return False
        return False
    else:
        return powerOfTwo(n/2) # Recursively call the function with n/2
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return powerOfTwo(n)
    
# Same approach using iterative method -

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:            # Check if n is 0, then return False
            return False
        while n % 2 == 0:     # Check if n is divisible by 2, then divide n by 2
            n = n / 2
        return n == 1         # Check if n is 1, then return True else False


# Optimized Approach: Using bitwise operator -

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n & n-1 == 0 and n>=1:
            return True
        else:
            return False