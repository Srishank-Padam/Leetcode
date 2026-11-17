class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # while len(s) > k:
        #     s = ''.join(str(sum(map(int, g))) for g in batched(s, k))
        # return s
        while len(s) > k:
            tem = []

            for i in range(0,len(s),k):
                val = 0
                for j in range(i, min(i+k, len(s))):
                    val += int(s[j])
                tem.append(str(val))
            
            s = ''.join(tem)

        return s
