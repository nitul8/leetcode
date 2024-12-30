# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

# Brute force solution:

def rev(num: int, ans: int) -> int:
    if num == 0:
        return ans
    else:
        res = num % 10
        ans = ans * 10 + res
        
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        
        return rev(num // 10, ans)

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -2**31:
            return 0
        
        num = abs(x)
        reversed_num = rev(num, 0)
        
        if x < 0:
            reversed_num = -reversed_num
        
        if reversed_num > 2**31 - 1 or reversed_num < -2**31:
            return 0
        return reversed_num
    
# Optimized solution:

class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            
            if (reversed_num > (2**31 - 1) // 10 or 
                (reversed_num == (2**31 - 1) // 10 and digit > 7)):
                return 0
            
            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num