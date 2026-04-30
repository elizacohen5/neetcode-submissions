class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        
        for count in num_count.values():
            if count > 1:
                return True
        return False
        