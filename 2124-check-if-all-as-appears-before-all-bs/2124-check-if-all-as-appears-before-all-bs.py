class Solution:
    def checkString(self, s: str) -> bool:
        i,j = 0, 1
        while j < len(s):
            if ord(s[i]) > ord(s[j]):
                return False
            else:
                i += 1
                j += 1
        
        return True