class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)-nums[0]
        if right == 0:
            return 0
        left = 0 
        for i in range(1,len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1