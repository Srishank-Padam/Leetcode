class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign *= -1
            s = s[1:]
        elif s[0] == '+':
            sign *= 1
            s = s[1:]

        ans = 0
        for i in s:
            if i.isnumeric():
                ans = ans * 10 + int(i)
            else:
                break
        
        result = sign * ans

        int_min, int_max = -2**31, 2**31 - 1

        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result
            