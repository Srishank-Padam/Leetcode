class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 1
        ans = 0
        prefix = 0
        mod = 10**9 + 7

        for n in arr:
            prefix += n

            if prefix % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        
        return ans % mod