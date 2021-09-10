var fib = function(n) {
    let fibseq = [1,1];
    
    for(let i = 0; i < n; i++){
        fibseq.push(fibseq[fibseq.length-1] + fibseq[fibseq.length-2])
    }
    
    return fibseq[n];
}


/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    let numways = 1;
    
    
    
    for(let i = 0; i < n-1; i++) {
        numways += fib(i);
        console.log(fib(i));
    }
    
    return numways;
    
};