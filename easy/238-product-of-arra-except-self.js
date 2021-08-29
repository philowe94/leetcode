/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    let output = [];
    
    let runningProduct = 1;
    for(let i = 0; i < nums.length; i++) {
        output[i] = runningProduct;
        runningProduct *= nums[i];
    }
    
    runningProduct = 1;
    for(let i = nums.length - 1; i >= 0; i--) {
        output[i] *= runningProduct;
        runningProduct *= nums[i];
    }

    
    return output;
};