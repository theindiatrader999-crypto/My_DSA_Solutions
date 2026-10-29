class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        j=len(nums)-1
        if i == j and nums[i]==val:
            return 0
        while i <= j:
            if nums[j] == val:
                j-=1
            elif nums[j] != val and nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
                i+=1
            elif nums[j] != val and nums[i]!= val:
                i+=1
        return j+1 