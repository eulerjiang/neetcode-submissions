
def totalHours(piles: List[int], rate: int) -> int:
    total = 0

    for num in piles:
        total += (num + rate - 1 ) // rate

    return total

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            total_hour = totalHours(piles, mid)
            if total_hour > h:
                l = mid + 1 
            else:
                r = mid

        return r



