class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue 
            
            curr_max = 1
            curr_num = num
            while curr_num + 1 in nums:
                curr_max += 1
                curr_num += 1

            longest = max(longest, curr_max)
        return longest 





         


         




        