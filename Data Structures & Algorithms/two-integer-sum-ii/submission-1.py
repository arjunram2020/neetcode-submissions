class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #this is sliding window problem... two sum with just 1 solution
        if not numbers:
            return None
        left = 0
        right = len(numbers)-1
        while left < right: #cannot be the same
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
        