class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            y=int(str(x)[::-1])
        else:
            y= int(str(abs(x))[::-1])
        return True if x==y else False
        
        
