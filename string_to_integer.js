/**
 * @param {string} str
 * @return {number}
 */
let myAtoi = function(str) {

    const FAIL = 0;

    // trim the initial whitespace characters
    str = str.trimStart();

    if (str.length === 0) return FAIL;

    // the first character may be the sign
    const first_char = str.charAt(0);

    // if first character is a sign
    if (first_char === '+' || first_char === '-') {
        // get rid of sign
        str = str.slice(1);
    }
    else if (isNaN(first_char)) {
        return FAIL;
    }

    // integer is positive unless there sign was a '-'
    const POSITIVE = first_char !== '-';

    const INDEX_OF_FIRST_NON_NUMERIC = str.search(/[^\d]/);

    // get the substring before the first non-numeric character.
    const INTEGER_STR = str.slice(
        0,
        // continue until first non-digit
        INDEX_OF_FIRST_NON_NUMERIC < 0 ? undefined : INDEX_OF_FIRST_NON_NUMERIC
    );

    if (INTEGER_STR.length === 0) return FAIL;

    // convert into a reversed array of digits
    let digits_rev = INTEGER_STR.split('').reverse().map(d => +d);

    // absolute value of integer
    const INTEGER_ABS_VAL = digits_rev.reduce((
        total, currentDigit, current_index
    ) => {
        return total + currentDigit * Math.pow(10,current_index);
    });

    const INTEGER = POSITIVE ? INTEGER_ABS_VAL : -INTEGER_ABS_VAL;

    if (POSITIVE) {
        const MAX = Math.pow(2,31) - 1;

        return MAX < INTEGER ? MAX : INTEGER;
    }
    else {
        const MIN = -Math.pow(2,31);

        return INTEGER < MIN ? MIN : INTEGER;
    }
};
