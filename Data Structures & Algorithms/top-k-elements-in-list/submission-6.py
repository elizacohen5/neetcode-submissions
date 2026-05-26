class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # buckets of length nums + 1 that store the number at the COUNT of that number 
        num_counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in num_counts.items():
            buckets[count].append(num)
        
        ans = []
        for bucket in reversed(buckets):
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
