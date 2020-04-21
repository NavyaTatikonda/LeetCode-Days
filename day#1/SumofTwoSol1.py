#brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j=i+1
            for j in range(len(nums)):
                if (nums[j]==target-nums[i]):
                    return i,j
