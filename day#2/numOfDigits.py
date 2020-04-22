class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_num=map(str,nums)
        count=0
        for i in str_num:
            if len(i)%2==0:
                count=count+1
              
        return count
