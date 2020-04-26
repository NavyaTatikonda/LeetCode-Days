class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.isspace():
            return 0                   
        elif len(s)>=2:
            return(len(s.split()[-1]))
        elif len(s)<2:
            return(len(s))
        else:
            return 0
