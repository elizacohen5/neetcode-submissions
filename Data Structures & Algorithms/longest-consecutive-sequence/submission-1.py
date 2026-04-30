class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      nums = set(nums)
      longest = 0

      for num in nums:
         if num - 1 in nums:
            continue 
         
         curr = num
         streak = 1
         while curr + 1 in nums:
            curr += 1
            streak += 1
         longest = max(longest, streak)
      return longest 


         


         




        