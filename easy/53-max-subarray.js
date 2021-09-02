/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    
    let sum = 0;
    let startnum = nums[0];
    
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (sum < startnum) {
            startnum = nums[i];
            sum = 0;
        }
    }
    
    return sum;
    
};