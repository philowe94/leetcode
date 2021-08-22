/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    
    let reversed = "";
    let num;
    let neg = false;
     
    if(x < 0) {
        x *= -1;
        neg = true;
    }

    while ( x >= 10 ) {
        num = x % 10;
        reversed += `${num}`;
        x = parseInt(x/10);
    }

    reversed += `${x}`;

    x = parseInt(reversed);
    if(neg) {
        x *= -1;
    }
     
    if ((x > 2**31 - 1) || (x < -(2**31))) {
        return 0;
    }
     
    return x;
};