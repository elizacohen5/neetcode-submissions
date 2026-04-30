class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = collections.Counter(nums)
      freq = [[] for _ in range(len(nums) + 1)]

      for num, count in count.items():
         freq[count].append(num)
      print(freq)

      ans = []
      for arr in reversed(freq):
         for num in arr:
            ans.append(num)
            if len(ans) == k:
               return ans
      return ans 



        