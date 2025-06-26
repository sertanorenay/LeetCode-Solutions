/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let explored = {}

    for (let i = 0; i < nums.length; i++) {
        if (explored[nums[i]] != undefined) {
            explored[nums[i]]++;
            if (explored[nums[i]] >= nums.length / 2) {
                return nums[i];
            }
        } else explored[nums[i]] = 1; 
    }
    return nums[0]; // Single element array
};
