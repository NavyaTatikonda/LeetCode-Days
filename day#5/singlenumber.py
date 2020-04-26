from collections import Counter
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        duplicates=[]
        for i in nums:
            if i not in duplicates:
                duplicates.append(i)
            else:
                duplicates.remove(i)
        return duplicates.pop()
            
        '''
        if len(nums) == 1:
            return nums[0]
        
        nums = sorted(nums)
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        for i in range(2, len(nums)-1):
            if (nums[i] != nums[i-1]) and (nums[i] != nums[i+1]):
                return nums[i]'''
