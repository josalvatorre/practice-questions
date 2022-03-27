/**
 * @param {string} s
 * @return {boolean}
 */
let isNumber = function (s) {
  // get rid of surrounding whitespace
  s = s.trim();

  let validDecimalNumber = RegExp(
    // start
    "^" +
      // optional: + OR -
      "([+\\-]?)" +
      // mantissa
      "(" +
      // d
      "(\\d+)" +
      // OR
      "|" +
      // d.  OR  d.d
      "((\\d+)(\\.)(\\d*))" +
      // OR
      "|" +
      // .d
      "((\\.)(\\d+))" +
      ")" +
      // optional: exponent
      "((" +
      // e
      "e" +
      // optional: + OR -
      "([+\\-]?)" +
      // digits
      "(\\d+)" +
      ")?)" +
      // end
      "$"
  );

  return validDecimalNumber.test(s);
};
