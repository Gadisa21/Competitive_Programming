class Solution(object):
    def timeRequiredToBuy(self,tickets, k):
        n = len(tickets)
        time = 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if i == k and tickets[i] == 0:
                        return time
        return time

