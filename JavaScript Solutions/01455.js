/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
    const words = sentence.trim().split(' ');
    for (let i = 0; i < words.length; i++) {
        let isSubstring = true;

        for (let j = 0; j < searchWord.length; j++) {
            if (searchWord[j] !== words[i][j]) {
                isSubstring = false;
            }
        }

        if (isSubstring) {
            return i + 1;
        }
    }

    return -1
};
