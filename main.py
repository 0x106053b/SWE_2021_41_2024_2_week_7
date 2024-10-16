from typing import List

def twoSum(nums : List[int], target : int) -> List[int] :
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                return [i, j]

nums = [3, 3]
target = 6
twoSum(nums, target)