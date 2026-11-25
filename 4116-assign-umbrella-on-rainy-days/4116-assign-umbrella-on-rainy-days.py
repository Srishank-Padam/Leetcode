class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        cnt_a = 0
        cnt_b = 0
        res = []
        for i in range(len(rain)-1):
            if rain[i] == 1 and rain[i+1] == 1:
                if cnt_a <= cnt_b:
                    res.append("Alice")
                    cnt_a +=1
                else:
                    res.append("Bob")
                    cnt_b += 1
            elif rain[i] == 1:
                res.append("Bob")
                cnt_b += 1
            else:
                res.append("None")

        if rain[len(rain)-1] == 1:
            res.append("Bob")
        else:
            res.append("None")
        
        return res

