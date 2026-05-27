class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if the number in the middle is greater than the number on the right, 
        # it means that the sorted array "started" somewhere to the right of the middle 
        # if the number in the middle is less than the number on the right, then the 
        # array started somewhere to the left of the middle 
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        