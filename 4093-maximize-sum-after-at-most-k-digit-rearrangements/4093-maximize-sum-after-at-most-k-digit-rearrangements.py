class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains = []

        for num in nums:
            digits = sorted(str(num), reverse = True)
            rearrange = int(''.join(digits))
            gains.append(rearrange - num)

        gains.sort(reverse = True)

        return sum(nums) + sum(gains[:k])