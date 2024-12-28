# Self Dividing Numbers

# Brute Force Solution;
def isSelfDividing(num):
    n = num
    while num > 0:
        digit = num % 10
        if digit == 0 or n % digit != 0 :
            return False
        num //=10
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            if isSelfDividing(num) == True:
                ans.append(num)
        return ans
    
    
# Optimized Solution:
def isSelfDividing(num: int) -> bool:
    num_str = str(num)
    for char in num_str:
        digit = int(char)
        if digit == 0 or num % digit != 0:
            return False
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                ans.append(num)
        return ans