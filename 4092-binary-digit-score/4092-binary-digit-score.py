class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = 0
        s2 = 0
        while a > 0:
            r1 = a % 2
            a = a // 2
            if r1 != 0:
                s1 += 1
        
        while b > 0:
            r2 = b % 2
            b = b // 2
            if r2 != 0:
                s2 += 1

        return s1 * s2 if s1 >= s2 else s2 // s1