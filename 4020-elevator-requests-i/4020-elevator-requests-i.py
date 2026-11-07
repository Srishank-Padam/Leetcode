class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total = requests[0]
        for i in range(1,len(requests)):
            total += abs(requests[i] - requests[i-1])

        return total
