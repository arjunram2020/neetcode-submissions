class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #three sum with an extra loop iterating it...
        #have a loop iterating i, for the fourth number
        # inside that loop, make it like three sum, WITH the duplicate checks for i
        nums.sort()
        output = []
        if(len(nums) < 4):
            return []
        for i in range(len(nums)-2): #i is the 4th number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range (i+1, len(nums)-1):
                left = j + 1
                right = len(nums)-1
                if j > i+1 and nums[j] == nums[j - 1]:
                        continue
                while(left < right):
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: #handles the 2nd number duplicates
                            left+=1
        return output
        #there will be duplicates... 


