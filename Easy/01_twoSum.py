# https://leetcode.com/problems/two-sum/

# o(n)
class Solution:
    def twoSum(self, nums, target):
        result = {}
        for index, value in enumerate(nums):
            if target - value in result:
                return [result[target - value], index]
            else:
                result[value] = index

# o(n^2)                
# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]