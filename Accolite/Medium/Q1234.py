# You are given a string s of length n containing only four kinds of characters: 
# 'Q', 'W', 'E', and 'R'. A string is said to be balanced if each of its characters 
# appears n / 4 times where n is the length of the string. Return the minimum length 
# of the substring that can be replaced with any other string of the same length to 
# make s balanced. If s is already balanced, return 0.

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        count = Counter(s)
        
        # Check if already balanced
        if all(count[char] <= target for char in "QWER"):
            return 0

        min_length = n
        start = 0

        for end in range(n):
            count[s[end]] -= 1

            # Check if the remaining string is balanced
            while all(count[char] <= target for char in "QWER"):
                min_length = min(min_length, end - start + 1)
                count[s[start]] += 1
                start += 1

        return min_length