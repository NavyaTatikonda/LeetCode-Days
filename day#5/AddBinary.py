class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum=int(a,2)+int(b,2)
        
        sum = bin(sum)
        
        #sum_value=int(sum,2)
        #retbinary_sum = bin(integer_sum)urn sum_value
        return sum[2:]
