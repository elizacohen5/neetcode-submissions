class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      nums = set(nums)
      longest = 0

      for num in nums:
         if num - 1 in nums:
            continue 
         
         streak = 1
         current = num 
         while current + 1 in nums:
            streak += 1
            current += 1
         longest = max(longest, streak)
      return longest 

         




        