class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        max_index = len(list) - 1
        min_index = 0 
        while min_index <= max_index:
            mid_index = (max_index + min_index) // 2
            if target == nums[mid_index]:
                return mid_index
            elif target > nums[mid_index]:
                min_index = mid_index + 1
            elif target < nums[mid_index]:
                max_index = mid_index - 1
        return min_index