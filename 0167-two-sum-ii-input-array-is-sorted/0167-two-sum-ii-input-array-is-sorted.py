from collections import Counter
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dic={}
        for i in range(len(numbers)):
            if target - numbers[i] not in dic:
                dic[numbers[i]] = i+1
            else:
                return [dic[target-numbers[i]],i+1]

        