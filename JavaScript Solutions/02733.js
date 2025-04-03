/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    if (nums.length < 3) return -1;

    const first3 = nums.slice(0, 3);
    const max = Math.max(...first3);
    const min = Math.min(...first3);

    return first3.find(item => item !== max && item !== min);
};
