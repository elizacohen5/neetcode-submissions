class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(int)

        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in sums.keys():
               return sorted([i, sums[goal]])
            sums[nums[i]] = i
        