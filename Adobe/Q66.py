# Plus One

# Approach 1:

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def plus(i):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            elif digits[i] == 9 and i != 0:
                digits[i] = 0
                return plus(i-1)
            else:
                digits[i] = 0
                digits.insert(0 , 1)
                return digits

        return plus(len(digits)-1)
    
# Approach 2:

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits