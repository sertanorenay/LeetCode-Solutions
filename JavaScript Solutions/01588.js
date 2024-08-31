/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    let sum = 0;
    for (let step = 1; step <= arr.length; step += 2) {
        for (let i = 0; i < arr.length; i++) {
            if (i+step <= arr.length) {
                let subArray = arr.slice(i, i+step);
            
                for (let j = 0; j < subArray.length; j++) {
                    sum += subArray[j];
                }
            }
        }
    }
return sum;
};

/**
 * @sertanorenay Not the best approach but works fine.
 */