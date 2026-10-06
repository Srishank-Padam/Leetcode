class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for f1 in s:
            if f1 not in d1:
                d1[f1] = str(s).count(str(f1))
        for f2 in t:
            if f2 not in d2:
                d2[f2] = t.count(f2)
        print(d1)
        print(d2)
        if d1 == d2:
            return True
        else:
            return False