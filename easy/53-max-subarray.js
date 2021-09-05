/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    
    let runningSum = nums[0];
    let largestSum = nums[0];
    let startingNum = nums[0];
    
    for(let i = 1; i < nums.length; i++) {
        runningSum = Math.max(runningSum + nums[i], nums[i]);
        largestSum = Math.max(runningSum, largestSum)
        
    }
    
    return largestSum;
    
};

/*
sum= 0
startnum = -2

sum=-2



*/