class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int max_difference = -1;

        for (int i = 1; i < nums.length - 1; i++) {
            int abs_difference = Math.abs(nums[i] - nums[i + 1]);
            if (abs_difference > max_difference) max_difference = abs_difference;
        }

        int first_last_difference = Math.abs(nums[0] - nums[nums.length - 1]);
        if (first_last_difference > max_difference) return first_last_difference;
        
        return max_difference;
    }
}