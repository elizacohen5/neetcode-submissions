class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = defaultdict(int)

        for num in nums:
            if num in num_count.keys():
                return True
            num_count[num] += 1
      
        return False 
        