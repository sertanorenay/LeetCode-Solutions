/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    let numberString = String(n)
    for (let i = numberString.length; i - 3 > 0; i -= 3) {
        numberString = numberString.slice(0, i-3) + '.' + numberString.slice(i-3);
    }
    return numberString;
};