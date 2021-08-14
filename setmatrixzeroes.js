/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
 var setZeroes = function(matrix) {
    
    //search thru matrix for zeroes, when you find them,
    //replace all nonzero values in the same row and column
    //with "zero"
    for(let i = 0; i < matrix.length; i++ ) {
        for(let y = 0; y < matrix[0].length; y++){
            if (matrix[i][y] === 0) {
                for(let q = 0; q < matrix.length; q++) {
                    if(matrix[q][y] != 0){
                        matrix[q][y] = "zero";
                    }
                }
                for(let w = 0; w < matrix[0].length; w++) {
                    if(matrix[i][w] != 0){
                        matrix[i][w] = "zero";
                    }
                }
            }
        }
    }
    
    //replace all "zero"s with 0
    for(let i = 0; i < matrix.length; i++ ) {
        for(let y = 0; y < matrix[0].length; y++){
            if (matrix[i][y] === "zero") {
                matrix[i][y] = 0;
            }
        }
    }
    
    return matrix;
};