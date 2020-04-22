class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sqrd_num=[]
        for i in A:
            sqr=i*i
            sqrd_num.append(sqr)
        return sorted(sqrd_num)
        
