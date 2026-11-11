class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mn = min(need1, need2)
        mx = max(need1, need2)

        return min(
            cost1 * need1 + cost2 * need2,

            mn * costBoth + (need1 - mn)* cost1 + (need2 - mn)* cost2,

            mx * costBoth
        )