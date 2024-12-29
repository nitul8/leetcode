def nextNum(num):
    if num == 0:
        return 0
    else :
        return (num % 10) ** 2 + nextNum(num // 10)

class Solution:
    def isHappy(self, n: int) -> bool:
        while n < 2**31:
            if n == 1:
                return True
            else :
                n = nextNum(n)
        return False
    
print(Solution().isHappy(19)) # True
print(Solution().isHappy(2)) # False

# In second example the process is repeated indefinitely. 

# Another Approach: Using set to store the numbers
def nextNum(num):
    if num == 0:
        return 0
    else :
        return (num % 10) ** 2 + nextNum(num // 10)

class Solution:
    def isHappy(self, n: int) -> bool:
        check = []
        while n not in check:
            check.append(n)
            if n == 1:
                return True
            else :
                n = nextNum(n)
        return False

# Better Approach: Floyd's Cycle Detection Algorithm

class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(num):
            if num == 0:
                return 0
            else :
                return (num % 10) ** 2 + nextNum(num // 10)
        slow = n
        fast = nextNum(n)
        while fast != 1 and slow != fast:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
        return fast == 1