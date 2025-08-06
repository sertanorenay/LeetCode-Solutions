class Solution {
    public int removeDuplicates(int[] nums) {
        int uniqueElementCount = 1; // Because the given array is not empty.
        int lastUniqueElement = nums[0];
        int indexOfLastUniqueElement = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != lastUniqueElement) {
                nums[++indexOfLastUniqueElement] = nums[i];
                lastUniqueElement = nums[i];
                uniqueElementCount++;
            }
        }
        
        return uniqueElementCount;
    }
}