class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find an intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]           # one step
            fast = nums[nums[fast]]     # two steps
            if slow == fast:
                break
        # Phase 2: find the entrance to the cycle (the duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        