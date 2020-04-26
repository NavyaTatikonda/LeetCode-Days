from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
          
        de=deque(nums)
        de.rotate(k)
        nums[:]=list(de)
        
        
  class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            rev=nums[-1]
            for j in range(len(nums)):
                nums[j],rev=rev,nums[j]
            
