class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq_buckets = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            freq_buckets[count].append(num)
      
        ans = []

        for freq in range(len(freq_buckets) - 1, -1, -1):
            for num in freq_buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans 