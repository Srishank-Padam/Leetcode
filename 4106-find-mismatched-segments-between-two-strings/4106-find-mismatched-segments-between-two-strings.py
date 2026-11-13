class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        i = j = 0
        result = []
        res1, res2 = "", ""
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                if res1 or res2:
                    result.append([res1, res2])
                    res1 = ""
                    res2 = ""
            else:
                res1 += s1[i]
                res2 += s2[j]
            i += 1
            j += 1

        if res1 or res2:
            result.append([res1, res2])
        return result