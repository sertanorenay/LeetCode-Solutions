/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canAliceWin = function(nums) {
    let singleDigitSum = 0;
    let doubleleDigitSum = 0;

    for (let num of nums) {
        if (num < 10) {
            singleDigitSum += num;
        } else {
            doubleleDigitSum += num;
        }
    }
    return singleDigitSum != doubleleDigitSum;
};
