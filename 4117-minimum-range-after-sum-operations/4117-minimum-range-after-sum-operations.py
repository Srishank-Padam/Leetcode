class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        mn = min(a,b,c)
        mx = max(a,b,c)
        mid = a + b + c - mx - mn
        return min(mid, mx - mn) 