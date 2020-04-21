#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in nums:
                    return nums.index(diff),j

#Time complexity - O(n^2)
#Space Complexity - O(1)
