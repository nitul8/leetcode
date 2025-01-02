#Brute Force Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
#Optimized Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return []