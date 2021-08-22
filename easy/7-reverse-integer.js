/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    
    let reversed = "";

    let num;

    while ( x > 10 ) {
        num = x % 10;
        reversed += `${num}`;
        x = parseInt(x/10);
    }

    reversed += `${x}`;

    return eval(reversed);
};