class Solution:
    def canAliceWin(self, n: int) -> bool:
        cnt = 10
        crr = "Alice"
        while n >= cnt:
            n -= cnt
            cnt -= 1
            if crr == "Alice":
                crr = "Bob"
            else:
                crr = "Alice"
        
        return True if crr == "Bob" else False

