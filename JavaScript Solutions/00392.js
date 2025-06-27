/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
  let i, j;
  for (i = 0, j = 0; i < t.length && j < s.length; i++) {
    if (t[i] == s[j]) j++;
  }
  return j == s.length;
};
