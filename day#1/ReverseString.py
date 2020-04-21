class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=-int(str(abs(x))[::-1])
        return x if  x <= 2147483647 and x >= -2147483648 else 0
        
