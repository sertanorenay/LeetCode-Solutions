/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    let result = [];
    let i = 0, first, last;

    while (i < nums.length) {
        first = nums[i];
        if (i == nums.length - 1) {
            result.push(`${first}`);
            return result;
        } else {
            while (nums[i + 1] == nums[i] + 1) {
                last = nums[i + 1];
                i++;
            }
            if (nums[i] == first) result.push(`${first}`);
            else result.push(`${first}->${last}`);
        }
        i++;
    }

    return result;
};
