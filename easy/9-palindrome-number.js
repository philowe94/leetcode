/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    
    if (x < 0) {
        return false;
    }
    
    let rev = 0;
    let xcopy = x;
    
    while (xcopy > 0) {
        let lastdigit = parseInt(xcopy % 10);
        rev = (rev*10) + lastdigit;
        xcopy = parseInt(xcopy / 10 | 0);
    }
    
        console.log(rev);
        console.log(xcopy);

    
    return x === rev;
};