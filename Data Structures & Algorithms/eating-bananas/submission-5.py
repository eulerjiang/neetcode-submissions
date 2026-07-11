class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        every hour:  x bananas

        x < max(piles)
        total_hours = math.ceil(piles[i]/x) + ...
        total_hours <= h

        (0, max(piles)]
        """

        max_k = max(piles)
        l, r = 1, max_k

        while l < r:
            x = (l + r) // 2

            eating_hours = [(piles[i] + x - 1) // x for i in range(len(piles))]
            total_hours = sum(eating_hours)

            if total_hours > h:
                l = x + 1
            else:
                r = x

        return r

            




        