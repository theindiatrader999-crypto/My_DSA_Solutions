class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''if len(nums) == 2 and nums[0] != nums[1]:
            return 2'''
        left=0
        for right in range(1,len(nums)):
            if nums[left] != nums[right] and right-left > 1:
                nums[left+1],nums[right] = nums[right],nums[left+1]
                left+=1
            elif nums[left] != nums[right] and right-left == 1:
                left+=1
        return left+1

        