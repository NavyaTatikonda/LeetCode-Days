class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val=0
        for i in range(1,len(nums)):
            if nums[val]!=nums[i]:
                val=val+1
                nums[val]=nums[i]
        return val+1
        
