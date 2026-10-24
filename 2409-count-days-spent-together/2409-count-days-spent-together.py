class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_arrival_day = sum(months[:int(arriveAlice[0:2]) - 1]) + int(arriveAlice[3:5])
        alice_leave_day = sum(months[:int(leaveAlice[0:2]) -1]) + int(leaveAlice[3:5])
        bob_arrival_day = sum(months[:int(arriveBob[0:2]) -1]) + int(arriveBob[3:5])
        bob_leave_day = sum(months[:int(leaveBob[0:2]) - 1]) + int(leaveBob[3:5])

        return max(0, min(alice_leave_day, bob_leave_day) - max(alice_arrival_day, bob_arrival_day)+1)