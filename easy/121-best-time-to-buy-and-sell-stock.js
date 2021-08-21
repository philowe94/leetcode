/**
 * @param {number[]} prices
 * @return {number}
 * *
 */
 var maxProfit = function(prices) {
    
    let minprice = prices[0];
    let maxprofit = 0;
    
    for(let i = 0; i < prices.length; i++) {
        if(prices[i] < minprice) {
            minprice = prices[i];
        }
        let profit = prices[i] - minprice;
        if(profit > maxprofit) {
            maxprofit = profit;
        }
    }
    
    return maxprofit;
};