class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right 

        while left <= right:
            mid = (left + right) // 2
            time_at_mid = sum((math.ceil(p / mid) for p in piles))
            
            if time_at_mid <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer 