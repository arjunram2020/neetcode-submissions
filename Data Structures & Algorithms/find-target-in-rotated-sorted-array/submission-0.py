class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##here once you search for a target, then you are fine.... do the normal algorithm...
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            